import matplotlib.pyplot as plt
import csv, random
from datetime import datetime

filename= 'employment-indicators.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, data in enumerate(header_row):
        print(index, data)

    industry_groups, period, data_value = [], [], []
    for row in reader:
        period.append(row[2])
        data_value.append(int(row[3]))
        industry_groups.append(row[1])
    industry_groups = list(dict.fromkeys(industry_groups))
    period = list(dict.fromkeys(period))


print(len(period))
colors = ['red', 'blue', 'green', 'lightblue', 'yellow', 'darkgreen', 'darkblue', 'violet']
x=0
y=11
for industry_group in industry_groups:
    plt.plot(period, data_value[x:y], c=random.choice(colors), label=industry_group)
    x+=11
    y+=11
plt.legend()
plt.show()