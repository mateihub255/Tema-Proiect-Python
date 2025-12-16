import pandas as pd
import matplotlib.pyplot as plt
X=9   
Y=8   
df = pd.read_csv("data.csv")

print("Primele randuri din fisier:")
print(df.head())

#  Toate valorile 

plt.plot(df.index, df["Durata"], label="Durata",color="hotpink")
plt.plot(df.index, df["Puls"], label="Puls",color="purple")
plt.plot(df.index, df["MaxPuls"], label="MaxPuls",color="#3F1898")
plt.plot(df.index, df["Calorii"], label="Calorii",color="#AECFF7")
plt.title("Toate valorile ")
plt.xlabel("Index")
plt.ylabel("Valoarea")
plt.grid(True)
plt.legend()
plt.show()

# Primele X valori Durata & Puls
df_firstX = df.head(X)

plt.plot(df_firstX.index, df_firstX["Durata"], label=f"Durata",color="hotpink",marker='*',linestyle = 'dotted')
plt.plot(df_firstX.index, df_firstX["Puls"], label=f"Puls",color="purple",marker='*',linestyle = 'dotted')
plt.plot(df_firstX.index, df_firstX["MaxPuls"], label=f"MaxPuls",color="#3F1898",marker='*',linestyle = 'dotted')
plt.plot(df_firstX.index, df_firstX["Calorii"], label=f"Calorii",color="#AECFF7",marker='*',linestyle = 'dotted')

plt.title(f"Primele {X} valori")
plt.xlabel("Index")
plt.ylabel("Valoarea")
plt.grid(True)
plt.legend()
plt.show()

# Ultimele Y valori Durata & Puls
df_lastY = df.tail(42)

plt.plot(df_lastY.index, df_lastY["MaxPuls"], label=f"MaxPuls",color="k",marker='^',ms=10,mec="k",linestyle = 'dotted')
plt.plot(df_lastY.index, df_lastY["Calorii"], label=f"Calorii",color="r",marker='v',ms=10,mec="k",linestyle = 'dotted')
plt.title(f"Ultimele {Y} valori MaxPuls & Calorii")
plt.xlabel("Index")
plt.ylabel("Valoarea")
plt.grid(True)
plt.legend()
plt.show()

