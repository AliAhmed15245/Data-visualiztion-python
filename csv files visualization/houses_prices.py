import matplotlib.pyplot as plt
import csv

filename = 'houses prices.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)
    date, prices = [], []
    for row in reader:
        date.append(row[0])
        prices.append(int(row[1]))


fig = plt.Figure(figsize=(7, 7))
plt.subplot(211)
plt.plot( prices, c='black')
plt.title('houses prices in UK ({})-({})'.format(date[0], date[-1]), fontsize=26)
plt.xlabel("Date", fontsize=16)
fig.autofmt_xdate()
plt.ylabel("Prices", fontsize=15)
plt.tick_params(axis='both', labelsize=14)

plt.subplot(212)
plt.bar(date, prices)

plt.show()