import csv
import matplotlib.pyplot as plt
from datetime import datetime

filename = "death_valley_2018_simple.csv"
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    dates= []
    highs = []
    lows = []
    print(header_row)
    for row in reader:
        try:
            current_date = datetime.strptime(row[2], "%Y-%m-%d")
            high =int(row[5])
            low =int(row[6])

        except ValueError:
            print(current_date, "missing data")
        else:
            dates.append(current_date)
            highs.append(high)
            lows.append(low)


fig = plt.figure(dpi=128, figsize=(10, 6))
plt.plot(dates, highs, c="red", label="highs", alpha=0.5)
plt.plot(dates, lows, c="blue", label="lows", alpha=0.5)
plt.fill_between(dates, highs, lows, facecolor="lightblue", alpha= 1)

plt.title("Highs and Lows of temperture of 2018", fontsize=24)
plt.xlabel("date", fontsize=14)
fig.autofmt_xdate()
plt.ylabel("Tempreture(F)", fontsize=14)
plt.tick_params(axis='both', labelsize=14, which="major")


plt.legend()
plt.show()
