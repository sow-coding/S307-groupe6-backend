import matplotlib.pyplot as plt
import numpy as np

countries = ["Royaume-Uni", "France", "Allemagne", "Suède"]
top1 = [0.784, 0.307, 0.579, 0.722]
hhi = [0.626, 0.221, 0.366, 0.541]

x = np.arange(len(countries))
width = 0.35

fig, ax = plt.subplots(figsize=(8, 5))
ax.bar(x - width/2, top1, width, label='Part du top-1 fournisseur')
ax.bar(x + width/2, hhi, width, label='IHH (Indice de Herfindahl-Hirschman)')

ax.set_xticks(x)
ax.set_xticklabels(countries)
ax.set_ylabel("Part / Indice")
ax.set_title("Part du premier fournisseur et indice IHH (importations SIPRI 2014–2024)")
ax.legend()
plt.tight_layout()
plt.show()