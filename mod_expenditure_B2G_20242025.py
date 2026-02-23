import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import StrMethodFormatter
from collections import defaultdict

top10 = []

with open("Table_3a_MOD_trade_industry_contracts_2025_Table3a.csv") as f:
    reader = csv.reader(f, delimiter=",")
    for row in reader:
        if row[0].strip() == "#":
            top10.append({
                "company": row[1].strip(),
                "country": row[2].strip(),
                "amount": int(row[3].strip()),
            })

# Grouper par pays d'origine
country_totals = defaultdict(int)
for entry in top10:
    country_totals[entry["country"]] += entry["amount"]

# Trier par montant croissant (pour barh)
sorted_countries = sorted(country_totals.items(), key=lambda x: x[1])
countries = [c[0] for c in sorted_countries]
amounts = [c[1] for c in sorted_countries]

fig, ax = plt.subplots(figsize=(9, 6))
ax.barh(countries, amounts)

ax.set_xlabel("Dépenses (£ millions)")
ax.set_title("Dépenses B2G d'équipement de défenses du Royaume-Uni 2024-2025")

ax.xaxis.set_major_formatter(StrMethodFormatter("{x:,.0f}"))

max_value = max(amounts)
padding = max_value * 0.01

for i, v in enumerate(amounts):
    ax.text(v + padding, i, f"{v:,.0f}", va="center")

ax.set_xlim(0, max_value * 1.12)

plt.tight_layout()
plt.show()
