import matplotlib.pyplot as plt
import matplotlib.ticker as ticker

pays = ["Royaume-Uni", "Suède", "France", "Allemagne"]
tiv = [6299300000, 787120000, 1250970000, 1398070000]

ax = plt.gca()
bars = ax.bar(pays, tiv)

ax.yaxis.set_major_formatter(ticker.FuncFormatter(lambda x, _: f'{x / 1_000_000:,.0f}'))

plt.title("TIV d'import d'armes conventionnelles brut par pays (2014–2024)")
plt.ylabel("TIV SIPRI (millions)")
plt.tight_layout()
plt.show()