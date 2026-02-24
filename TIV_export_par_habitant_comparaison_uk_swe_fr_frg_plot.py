import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

pays = ["Royaume-Uni", "Suède", "France", "Allemagne"]
tiv_par_habitant = [(11985730000/66668327), (2466030000/10251285), (27913250000/67311180), (18007480000/82856090)]

ax = plt.gca()
bars = ax.bar(pays, tiv_par_habitant)

plt.title("Exportations d’armes conventionnelles par habitant (TIV SIPRI, moyenne 2014–2024)")
plt.ylabel("TIV SIPRI par habitant")
plt.tight_layout()
plt.show()