TIV = {
    "Royaume-Uni": [11985730000, 6299300000],
    "Suède": [2466030000, 787120000],
    "Allemagne": [18007480000, 1398070000],
    "France": [27913250000, 1250970000]
}

for country, values in TIV.items():
    ratio = values[0] / values[1]
    print(country, ratio)