import pandas as pd

def load_sipri_register(path):
    return pd.read_csv(path, dtype=str, encoding="latin-1", header=None)

def supplier_metrics(path):
    df = load_sipri_register(path)

    tiv = (df[15]
           .astype(str).str.replace("?", "", regex=False).str.strip())
    df["_tiv"] = pd.to_numeric(tiv, errors="coerce")

    by_sup = df.groupby(1)["_tiv"].sum().sort_values(ascending=False)
    total = by_sup.sum()
    shares = by_sup / total

    top1_share = shares.iloc[0]
    top1_supplier = shares.index[0]
    top3_share = shares.iloc[:3].sum()
    hhi = float((shares**2).sum())
    return total, len(shares), top1_supplier, top1_share, top3_share, hhi, shares

# Exemple d’appel
for name, path in {
    "UK": "uk-import-arms.csv",
    "France": "fr-import-arms.csv",
    "Germany": "frg-import-arms.csv",
    "Sweden": "swe-import-arms.csv",
}.items():
    total, n, top1_sup, top1, top3, hhi, shares = supplier_metrics(path)
    print(name, top1_sup, top1, hhi)