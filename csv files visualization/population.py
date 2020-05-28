import pygal, csv

filename = "population.csv"
with open(filename) as  f:
    reader = csv.reader(f)
    header_row = next(reader)

    cc_pop, cc_pop1= [], []
    years = []
    for row in reader:
        if row[0] == "Saudi Arabia":
            years.append(int(row[2]))
            cc_pop.append(int(row[3]))
        if row[0] == "Egypt, Arab Rep.":
            cc_pop1.append(int(row[3]))


chart = pygal.Line()
chart.title = "Some arab countries population {}-{}".format(str(min(years)), str(max(years)))
chart.x_labels= years
chart.x_title = "Years"
chart.y_title="Population"
chart.add("Saudi Arabia", cc_pop)
chart.add("Egypt", cc_pop1)

chart.render_to_file("population.svg")
