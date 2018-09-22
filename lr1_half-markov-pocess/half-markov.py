import json
import math
from datetime import datetime
from itertools import tee
from random import random
from typing import Tuple, List


def model(P, W, state: int, samples_count: int = 1000) -> List[Tuple[int, float]]:
    recorded_samples = []
    for i in range(samples_count):
        state_random = random()
        threshold = 0
        for new_state, new_state_p in enumerate(P[state]):
            threshold += new_state_p
            if state_random <= threshold:
                teta = (-1 / W[state][new_state]) * math.log(random())
                recorded_samples.append((new_state, teta))
                print(f'Teta: {round(teta, 3)}...', end='', flush=True)

                # sleep(teta)  # fixme debug

                state = new_state
                print(f'new state #{state}\n')

                break

    return recorded_samples


def model_by_samples(samples: List[Tuple[int, float]], states_count: int = 3, gist_resolution = 0.25, gist_width = 240):
    """
    :param states_count: Количество состояний процесса
    :param gist_resolution: Разрешение гистограммы по времени, с.
    :param gist_width: Количество отсчетов. Например 120 отсчетов при разрешении в 0.25с. - интервал 0-30с.
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


def assert_matrix(m, eps=0.00001):
    assert len(m) == len(m[0]), 'Matrix should be square'
    for line in m:
        assert abs(sum(line) - 1) < eps, 'Wrong sum of matrix line (should be 1).'


if __name__ == '__main__':
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

    assert_matrix(P)

    initial_state = 0
    samples_count = 5000
    samples = model(P, W, initial_state, samples_count=samples_count)

    filename = f'{datetime.now().strftime("%y-%m-%d_%H-%M-%S")}.tmp'
    with open(filename, 'w') as f:
        json.dump(samples, f)

    new_P, new_W = model_by_samples(samples, states_count=3)

    assert_matrix(new_P)
