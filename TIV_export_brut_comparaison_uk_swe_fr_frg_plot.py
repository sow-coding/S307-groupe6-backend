import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

pays = ["Royaume-Uni", "Suède", "France", "Allemagne"]
tiv = [11985730000, 2466030000, 27913250000, 18007480000]

ax = plt.gca()
bars = ax.bar(pays, tiv)

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1_000_000:,.0f}'))

plt.title("Exportations d’armes conventionnelles (TIV SIPRI, cumul 2014–2024)")
plt.ylabel("TIV SIPRI (millions)")
plt.tight_layout()
plt.show()