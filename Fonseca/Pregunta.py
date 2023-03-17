import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

url1="https://raw.githubusercontent.com/MinCiencia/Datos-CambioClimatico/main/output/temperatura_aire_ceaza/2023/2023_temperatura_aire_ceaza.csv"
df_1=pd.read_csv(url1)
df_2023 = pd.DataFrame(df_1)
df_2023['etiqueta'] = '2023'



url2= "https://raw.githubusercontent.com/MinCiencia/Datos-CambioClimatico/main/output/temperatura_aire_ceaza/2020/2020_temperatura_aire_ceaza.csv"
df_2= pd.read_csv(url2)
df_2020= pd.DataFrame(df_2)
df_2020['etiqueta'] = '2020'

#Se pasa a datetime la fecha
df_2023['time'] = pd.to_datetime(df_2023['time'])
df_2020['time'] = pd.to_datetime(df_2020['time'])

#seleccionamos solo los datos de abril
df_abril_2023 = df_2023[df_2023['time'].dt.month == 3]

df_abril_2020 = df_2020[df_2020['time'].dt.month == 3]

#Concatenamos los dataframe
#df = pd.concat([df_abril_2020,df_abril_2023])



#GRAFICO

sns.kdeplot(data=df_abril_2023, x='prom', label='2023')
sns.kdeplot(data=df_abril_2020, x='prom', label='2020')
plt.xlabel('Temperatura (°C)')
plt.ylabel('Densidad de probabilidad')
plt.title('Promedio de la temperatura en la Región Metropolitana en marzo')
plt.legend()
plt.show() 
