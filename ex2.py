import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("date.csv")

plt.figure()
plt.plot(df["Durata"],marker='o', color='blue',label="Durata")
plt.plot(df["Puls"],marker='o', color='pink', label="Puls")
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Toate valorile")
plt.legend()
plt.show()


X=len("Alexia-Georgiana")
plt.figure()
plt.plot(df["Durata"].head(X),marker='o', color='blue', label="Durata")
plt.plot(df["Puls"].head(X),marker='o', color='pink', label="Puls")
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Primele {X} valori: Durata și Puls")
plt.legend()
plt.show()

Y=len("Ghimpeteanu")
plt.figure()
plt.plot(df["Durata"].tail(Y),marker='o', color='blue', label="Durata")
plt.plot(df["Puls"].tail(Y),marker='o', color='pink', label="Puls")
plt.xlabel("X")
plt.ylabel("Y")
plt.title(f"Ultimele {Y} valori: Durata și Puls")
plt.legend()
plt.show()
