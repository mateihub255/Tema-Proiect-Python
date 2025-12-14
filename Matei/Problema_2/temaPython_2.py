import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data.csv")

X = 13
Y = 5 

df.plot()
plt.title("Toate valorile afisate grafic")
plt.xlabel("Index")
plt.ylabel("Valoare")

firstX_values = df.head(X)

firstX_values.plot()
plt.title("Primele X valori afisate grafic")
plt.xlabel("Index")
plt.ylabel("Valoare")

lastY_values = df.tail(Y)
a = lastY_values[['Durata']]
b = lastY_values[['Puls']]
# lastY_values[['Durata']].plot( color = 'r', marker = '+', ms = 20 )
# lastY_values[['Puls']].plot( color = 'k', marker = 'v', ms = 20 )
plt.plot( a, color = 'r', marker = '+', ms = 20 )
plt.plot( b, color = 'k', marker = 'v', ms = 20 )
plt.title("Ultimele Y valori pentru Durata si Puls afisate grafic")
plt.xlabel("Index")
plt.ylabel("Valoare")

plt.show()