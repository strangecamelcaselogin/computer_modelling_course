from pathlib import Path
import csv

from PyQt5.QtWidgets import QFileDialog

from app.core.abstract_dataset_loader import AbstractDatasetLoader
from app.core.dataset import Dataset


class FSCSVLoader(AbstractDatasetLoader):
    """
    Загрузит датасет из .csv файла вида:

    type	class	0	1	2	3	4	5	6
    train	0	3	3	0.588658071	0.108916731	0.098766498	0.348669801	0.061671953
    train	0	3	3	0.57840739	0.113558019	0.091052115	0.317832763	0.137982935
    train	0	2	2	0.652519888	0.046648935	0.300783577	0.043434637	0.025101673
    train	0	3	3	0.577604727	0.11379719	0.091737188	0.313239207	0.138697284
    train	1	2	2	0.652519888	0.046648935	0.300783577	0.043434637	0.025101673
    train	1	1	2	0.687389869	0.056448984	0.305828505	0.043711539	0.022024498
    train	1	1	1	0.659170962	0.082716783	0.271939362	0.048655794	0.043457038
    train	1	1	2	0.668346043	0.064070268	0.306771498	0.048937987	0.03055405
    test	0	3	3	0.588658071	0.108916731	0.098766498	0.348669801	0.061671953
    test	0	3	3	0.57840739	0.113558019	0.091052115	0.317832763	0.137982935
    test	0	2	2	0.652519888	0.046648935	0.300783577	0.043434637	0.025101673
    test	0	3	3	0.577604727	0.11379719	0.091737188	0.313239207	0.138697284
    test	1	2	2	0.652519888	0.046648935	0.300783577	0.043434637	0.025101673
    test	1	1	2	0.687389869	0.056448984	0.305828505	0.043711539	0.022024498
    test	1	1	1	0.659170962	0.082716783	0.271939362	0.048655794	0.043457038
    test	1	1	2	0.668346043	0.064070268	0.306771498	0.048937987	0.03055405
    """
    def __init__(self, data_path, sample_dimensions=()):
        """
        :param data_path: путь до папки с датасетами
        :param sample_dimensions: размерность данных
        """
        super().__init__(data_path, sample_dimensions)

    @staticmethod
    def get_dialog(parent, data_path: str):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog

        file_name, _ = QFileDialog.getOpenFileName(
            parent,
            'Загрузить данные из CSV',
            data_path, 'Text CSV (*.csv)', options=options)

        return file_name

    def load(self, path):
        name = Path(path).relative_to(self.data_path).name

        train_data, train_labels = [], []
        test_data, test_labels = [], []
        with path.open() as f:
            reader = csv.DictReader(f)

            dimensions = None
            for row in reader:
                # todo support of empty strings
                # todo better assertion
                is_train, cls, *x = row.values()

                is_train = is_train == 'train'
                cls = int(cls)

                if dimensions is None:
                    dimensions = len(x)
                elif len(x) != dimensions:
                    raise Exception('CSV parsing goes totally wrong! (line dimensions mismatch)')  # fixme

                if is_train:
                    train_data.append(tuple(map(float, x)))
                    train_labels.append(cls)
                else:
                    test_data.append(tuple(map(float, x)))
                    test_labels.append(cls)

        if set(train_labels) != set(test_labels):
            raise Exception('Different set of classes between test and train data!')  # fixme

        if not train_data or not test_data:
            raise Exception('Train and test data must be presented')   # fixme

        return Dataset(
            name,
            train_data, train_labels,
            test_data, test_labels,
            list(set(train_labels)),
            sample_dimensions=tuple([None for _ in range(dimensions)])
        )
