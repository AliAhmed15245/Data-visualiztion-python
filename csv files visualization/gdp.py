import pygal, csv

filename = "gdp.csv"
with open(filename) as  f:
    reader = csv.reader(f)
    header_row = next(reader)

    cc_gpd, cc_gdp1, cc_gpd2, cc_gpd3= [], [], [], []
    years = []
    for row in reader:
        if row[0] == "Saudi Arabia":
            years.append(int(row[2]))
            cc_gpd.append(float(row[3]))
        if row[0] == "Egypt, Arab Rep.":
            cc_gdp1.append(float(row[3]))
        if row[0]=="China":
            cc_gpd2.append(float(row[3]))
        if row[0] == "United States":
            cc_gpd3.append(float(row[3]))


chart = pygal.Line()
chart.title = "Some countries GDP {}-{}".format(str(min(years)), str(max(years)))
chart.x_labels= years
chart.x_title = "Years"
chart.y_title="Population"
chart.add("Saudi Arabia", cc_gpd)
chart.add("Egypt", cc_gdp1)
chart.add("China", cc_gpd2)
chart.add("USA", cc_gpd3)

chart.render_to_file("gdp.svg")
