import pandas as ps
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import LabelEncoder
from sklearn.utils import shuffle
from sklearn.model_selection import train_test_split


class Trainer():
    def __init__(self, csvPath):
        self.csvPath = csvPath


    def getFeaturesLabels(self, pdDataset):
        pass

    def oneHotEncoder(self):
        labels = 12
        n_label = len(labels)
        n_unique_labels = len(np.unique(labels))
        one_hot_encoder = np.zeros((n_label, n_unique_labels))
        one_hot_encoder[np.arange(n_label), labels] = 1
        return one_hot_encoder

    def readCsv(self):
        dataset = ps.read_csv(self.csvPath)
        self.getFeaturesLabels()
        X = dataset[dataset.columns[0:1024]].values



if __name__ == "__main__":
    Trainer("../dataset.csv")