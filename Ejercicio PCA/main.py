import sklearn as skl
import pandas as pd
import numpy as np
from sklearn.decomposition import PCA


data = pd.read_csv('europe.csv')
pd.set_option("display.max_columns", 8)
dict_data = data.to_dict("list")
print(dict_data)

# estandarizaciones

std_value_matrix = [dict_data.get("Country")]
std_value_matrix_only_numbers = []

for key in dict_data.keys():

    if key != 'Country':
        variable = dict_data.get(key)
        average = np.average(np.array(variable))
        std = np.std(np.array(variable))

        std_data = []
        for value in variable:
            std_data.append((value - average) / std)

        std_value_matrix.append(std_data)
        std_value_matrix_only_numbers.append(std_data)


print("std matrix", std_value_matrix)

# cov_matrix = np.cov(std_value_matrix_only_numbers)
# print()
# print("cov matrix: ", cov_matrix)
# print()

pca = PCA(n_components=4)
test = pca.fit_transform(np.array(std_value_matrix_only_numbers).T)

print(test)
# print()
# print(pca.components_)

# eigenvals, eigenvecs = np.linalg.eig(cov_matrix)
#
# print()
# print(eigenvals)
# print()
# print(eigenvecs)

