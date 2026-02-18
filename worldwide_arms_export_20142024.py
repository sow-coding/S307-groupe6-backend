import csv
import numpy as np

units = []

# row 15 et non 8 car on mesure en TIV unité de Sipri et non en unité classique

with open('trade-register-worldwide.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in reader:
        units.append(float(row[15]))

unitsNp = np.array(units)

print(np.sum(unitsNp))