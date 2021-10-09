# Programa de prueba extraido de https://ostwalprasad.github.io/machine-learning/PCA-using-python.html
import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd  
import seaborn as sns 
from sklearn.datasets import load_boston
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA


boston_dataset = load_boston() #carga de datos
boston = pd.DataFrame(boston_dataset.data, columns=boston_dataset.feature_names)
boston.head()

print(boston)
x = StandardScaler().fit_transform(boston)  #estandarizacion de datos
x = pd.DataFrame(x, columns=boston_dataset.feature_names)

pcamodel = PCA(n_components=5)      #calculo de componentes principales
pca = pcamodel.fit_transform(x)

print(pca.shape)

print(pcamodel.explained_variance_)
print(pcamodel.explained_variance_ratio_)

plt.scatter(pca[:, 0], pca[:, 1])               #graficos
plt.show()

def myplot(score,coeff,labels=None):
    xs = score[:,0]
    ys = score[:,1]
    n = coeff.shape[0]
    scalex = 1.0/(xs.max() - xs.min())
    scaley = 1.0/(ys.max() - ys.min())
    plt.scatter(xs * scalex,ys * scaley,s=5)
    for i in range(n):
        plt.arrow(0, 0, coeff[i,0], coeff[i,1],color = 'r',alpha = 0.5)
        if labels is None:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, "Var"+str(i+1), color = 'green', ha = 'center', va = 'center')
        else:
            plt.text(coeff[i,0]* 1.15, coeff[i,1] * 1.15, labels[i], color = 'g', ha = 'center', va = 'center')
 
    plt.xlabel("PC{}".format(1))
    plt.ylabel("PC{}".format(2))
    plt.grid()

myplot(pca[:,0:2],np.transpose(pcamodel.components_[0:2, :]),list(x.columns))
plt.show()
