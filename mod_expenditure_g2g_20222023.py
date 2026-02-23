import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter

data = {
    "Country": ["Canada", "Estonie", "France", "Allemagne", "Indonésie", "Pays-bas",
                "Sri Lanka", "États-Unis"],
    "Amount": ["42", "14", "71", "12", "7", "7", "9", "1816"]
}

df = pd.DataFrame(data)

df["Amount"] = pd.to_numeric(df["Amount"])

df = df.sort_values("Amount", ascending=True)

fig, ax = plt.subplots(figsize=(9,6))
ax.barh(df["Country"], df["Amount"])

ax.set_xlabel("Dépenses (£ millions)")
ax.set_title("Dépenses G2G d'équipements de défense du Royaume-Uni 2022–2023")

ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))

max_value = df["Amount"].max()
padding = max_value * 0.01

for i, v in enumerate(df["Amount"]):
    ax.text(v + padding, i, f"{v:,.0f}", va='center')

ax.set_xlim(0, max_value * 1.08)

plt.tight_layout()
#plt.savefig("figure_bar.pdf", bbox_inches="tight")
#plt.savefig("figure_bar.png", dpi=300, bbox_inches="tight")
plt.show()
