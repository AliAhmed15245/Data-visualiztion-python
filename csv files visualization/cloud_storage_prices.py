import pygal
import csv

filename = 'cloud storage prices.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header = next(reader)

    year, amazon, azura, google = [], [], [], []
    for row in reader:
        year.append(row[0])
        amazon.append(float(row[1]))
        azura.append(float(row[2]))
        google.append(float(row[3]))



chart = pygal.Line()
chart.title = 'Cloud prices for Amazon, Azura and Google'
chart.x_labels = year
chart.x_title = 'year'
chart.y_title = 'price'
chart.add("Amazon", amazon)
chart.add("Azura", azura)
chart.add("Google", google)
chart.render_to_file('cloud_prices.svg')

