import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename= 'covid19.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, data in enumerate(header_row):
        print(index, data)

    values = []
    date =[]
    for row in reader:
            values.append(int(row[9]))
            date.append(datetime.strptime(row[4], "%d/%m/%Y"))


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.scatter(date, values, c=values, s=30, cmap=plt.cm.Blues, edgecolor='none')
fig.autofmt_xdate()
plt.ylabel("Values", fontsize=14)
plt.xlabel("Date", fontsize=14)
plt.title("COVID-19 damage value", fontsize=24)
plt.tick_params(axis='both', labelsize=14)
plt.show()


