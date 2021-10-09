import sklearn as skl
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
from sklearn.decomposition import PCA

def standarize_data(path):
    data = pd.read_csv(path)
    pd.set_option("display.max_columns", 8)
    dict_data = data.to_dict("list")

    countries = list(dict_data.get("Country"))
    #std_value_matrix = [dict_data.get("Country")]
    std_value_matrix_only_numbers = []
    labels = []

    for key in dict_data.keys():

        if key != 'Country':
            variable = dict_data.get(key)
            average = np.average(np.array(variable))
            std = np.std(np.array(variable))
            labels.append(key)

            std_data = []
            for value in variable:
                std_data.append((value - average) / std)

            #std_value_matrix.append(std_data)
            std_value_matrix_only_numbers.append(std_data)

    return countries, std_value_matrix_only_numbers, labels

# estandarizaciones


# cov_matrix = np.cov(std_value_matrix_only_numbers)
# print()
# print("cov matrix: ", cov_matrix)
# print()

countries, std_value_matrix, labels = standarize_data('europe.csv')

pca = PCA(n_components=3)
test = pca.fit_transform(np.array(std_value_matrix).T)

variance = pca.explained_variance_  # the amount of variance explained by each of the selected components.
# imprime [3.34669033 1.23109094 1.10256796 0.79888768 0.47480597 0.17492107 0.13029529]

def biplot(score, coeff, labels):
    xs = score[:, 0]                        # todas las filas, columna 0 de la matriz test
    ys = score[:, 1]                        # filas, columna 1 de la matriz test
    n = coeff.shape[0]
    scalex = 1.0 / (xs.max() - xs.min())
    scaley = 1.0 / (ys.max() - ys.min())
    plt.scatter(xs * scalex, ys * scaley, s=5)
    for i in range(len(labels)):
        plt.arrow(0, 0, coeff[0, i], coeff[1, i], color='r', alpha=0.5)
        plt.text(coeff[0, i] * 1.15, coeff[1, i] * 1.15, labels[i], color='g', ha='center', va='center')

    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.grid()

biplot(test[:, :], np.transpose(test[:, :]), labels)
plt.show()



