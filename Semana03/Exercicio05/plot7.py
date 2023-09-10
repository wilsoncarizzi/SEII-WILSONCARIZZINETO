import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv()

dados.head()

masculinos = dados.loc[dados['Sex']=='M']
a = masculinos['Height']
p = masculinos['Weight']
plt.scatter(a,p)
plt.show()