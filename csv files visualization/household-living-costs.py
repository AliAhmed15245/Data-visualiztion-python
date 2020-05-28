import matplotlib.pyplot as plt
import csv
from datetime import datetime

filename= 'household-living-costs-price-indexes-march-2020-quarter-group-facts.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    for index, data in enumerate(header_row):
        print(index, data)

    years = []
    income = []
    expenditure = []
    for row in reader:
        years.append(int(row[1]))
        income.append(int(row[11]))
        expenditure.append(int(row[12]))
print(years)
fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(years, income, c="green", label="Income")
plt.plot(years, expenditure, c="red", label="Expenditure")
plt.fill_between(years, income, expenditure, facecolor="lightblue")

plt.title("income and expenditure of {} families".format(len(income)), fontsize=24)
plt.xlabel("years", fontsize=14)
fig.autofmt_xdate()
plt.ylabel("value", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
plt.legend()
plt.show()

