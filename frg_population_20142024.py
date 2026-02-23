import csv
import numpy as np

populations = []

with open("frg-population-dataset-20142024.csv") as f:
    reader = csv.reader(f, delimiter=";")
    for row in reader:
        if (row[0] == "source"):
            continue
        populations.append(int(row[1]))

populationsNp = np.array(populations)

print(np.sum(populationsNp)/11)
