import json
import math
from datetime import datetime
from itertools import tee
from random import random
from time import sleep
from typing import Tuple, List


def model(P, W, state: int, samples_count: int = 1000, W_is_gist=False, debug=False, W_gist_resolution=None) -> List[Tuple[int, float]]:
    """
    Прямое моделирование полумарковского процесса.
    :param P: Матрица вероятностей перехода
    :param W: Матрица, задающая интенсивности переходов
    :param state: Начальное состояние
    :param samples_count: Количество итераций/переходов
    :param W_is_gist: Определяет каким образом задана W
    :param debug: Отладочный вывод
    :param W_gist_resolution: Разрешение гистограммы по времени, с.
    :return: Запись переходов в формате (<состояние>, <время в этом состоянии>)
    """
    assert_matrix(P)

    states_count = len(P)
    assert 0 <= state <= states_count, 'wrong initial state'

    if W_is_gist:
        assert W_gist_resolution is not None, 'if W_is_gist, gist_resolution must be set'

    recorded_samples = []
    for i in range(samples_count):
        new_state = pick_index(P[state])

        # в зависимости от того, как задана интенсивность переходов
        #  (коэффициенты лямбда или гистограммы, снятые с входного сигнала), выберем teta
        if W_is_gist:
            teta = pick_index(W[state][new_state]) * W_gist_resolution
        else:
            teta = (-1 / W[state][new_state]) * math.log(random())

        recorded_samples.append((new_state, teta))
        print(f't: {round(teta, 3)}...', end='', flush=True)

        if debug:
            sleep(teta)

        state = new_state
        print(f'new state: #{state}\n')

    return recorded_samples


def model_by_samples(samples: List[Tuple[int, float]], states_count: int = 3, gist_resolution = 0.25, gist_width = 240):
    """
    Обратная задача. Определение вероятностей перехода и интенсивности переходов по записи процесса.
    :param samples: Запись полумарковского процесса.
    :param states_count: Количество состояний процесса
    :param gist_resolution: Разрешение гистограммы по времени, с.
    :param gist_width: Количество отсчетов. Например 120 отсчетов при разрешении в 0.25с. - интервал 0-30с.
    :return Матрицу вероятностей переходов (P) и матрицу гистограм распределений времени нахождения в состояниях.
    """
    state_stat = [[0] * states_count for _ in range(states_count)]
    time_gist = [
        [[0 for _ in range(gist_width)] for _ in range(states_count)] for _ in range(states_count)
    ]

    for (p, teta), (v, _) in pairs(samples):
        # подсичтаем коичество переходов из состояния p в состояние v
        state_stat[p][v] += 1

        # учтем в гистограмме распределения времени время перехода из состояния p в v
        gist_index = int(teta / gist_resolution)
        if gist_index < gist_width:
            time_gist[p][v][gist_index] += 1
        else:
            print(f'warn: rare teta: {teta}')
            time_gist[p][v][gist_width - 1] += 1

    for i in range(states_count):
        same_initial_state_total = sum(state_stat[i])
        for j in range(states_count):
            # переведем статистику переходов в вероятности переходов (P)
            state_stat[i][j] /= same_initial_state_total

            # нормирование гистограм распределения времени teta перехода из i в j состояние
            gist_sum = sum(time_gist[i][j])  # количество образцов в гистограмме перехода i-j
            time_gist[i][j] = list(map(lambda v: v / gist_sum, time_gist[i][j]))

    return state_stat, time_gist


def pairs(iterable):
    a, b = tee(iterable)
    next(b, None)
    return zip(a, b)


def assert_matrix(m):
    assert len(m) == len(m[0]), 'Matrix should be square'
    for line in m:
        assert abs(sum(line) - 1) < EPS, 'Wrong sum of matrix line (should be 1).'


def pick_index(probabilities):
    """
    :param probabilities: - список, гистограмма распределения, прим. - [.5, .25, .20, .5]
    :return: случайно выбранный индекс в гистограмме probabilities
    """
    assert abs(sum(probabilities) - 1) < EPS

    r = random()
    threshold = 0
    for idx, p in enumerate(probabilities):
        threshold += p
        if r <= threshold:
            return idx


if __name__ == '__main__':
    EPS = 0.000001

    P = [
        [.5, .25, .25],
        [.25, .5, .25],
        [.25, .25, .5],
    ]

    W = [
        [.1, .2, .3],
        [.2, .1, .3],
        [.3, .1, .2],
    ]

    debug = False
    initial_state = 0
    samples_count = 5000

    samples = model(P, W, initial_state, samples_count=samples_count, debug=debug)

    filename = f'{datetime.now().strftime("%y-%m-%d_%H-%M-%S")}.tmp'
    with open(filename, 'w') as f:
        json.dump(samples, f)

    #############
    gist_resolution = 0.25
    gist_width = 240
    new_P, new_W = model_by_samples(samples,
                                    states_count=3,
                                    gist_resolution=gist_resolution,
                                    gist_width=gist_width)

    new_samples = model(new_P, new_W, initial_state,
                        samples_count=samples_count,
                        W_is_gist=True,
                        W_gist_resolution=gist_resolution,
                        debug=debug)

    print('done.')
