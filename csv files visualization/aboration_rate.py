import matplotlib.pyplot as plt
import csv, random
from datetime import datetime

filename= 'aboration_rate.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, data in enumerate(header_row):
        print(index, data)

    abortion, ages, period = [], [], []

    for row in reader:
        period.append(row[0])
        abortion.append(float(row[2]))
        ages.append(row[1])

fig = plt.figure(dpi=128)
colors = ['red', 'blue', 'green', 'lightblue', 'yellow', 'darkgreen', 'darkblue', 'violet']
x=0
y=9
year = 2000
for i in range(19):
    plt.plot(ages[x:y], abortion[x:y], c=random.choice(colors), label=str(year))
    x+=8
    y+=8
    year+=1

plt.title("Aboration rate from 2000 to 2018", fontsize=24)
plt.xlabel("Women age", fontsize=14)
plt.ylabel("Aboration Rate", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
fig.autofmt_xdate()
plt.legend()
plt.show()

