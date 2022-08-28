import pandas as pd
df = pd.read_csv('data.csv')
x = df[['weight']]
y = df.height

"""1) Calcular SSxx"""
xmean = x.mean()
df['diffx'] = xmean - x
df['diffx_squared'] = df.diffx**2
SSxx = df.diffx_squared.sum()

"""2) Calcular SSxy"""
ymean = y.mean()
df['diffy'] = ymean - y
SSxy = (df.diffx * df.diffy).sum()

"""3) Calcular m"""
m = SSxy / SSxx

"""4) Calcular b"""
b = ymean - m * xmean

"""5) Predecir valores con el modelo"""
def predict(value):
    predict = m * value + b
    return predict
print(predict(140))
