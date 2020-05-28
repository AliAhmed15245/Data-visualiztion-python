import pygal

years = ['2011','2012','2013','2014','2015','2016']
python = [15, 31, 89, 200, 356, 900]
java = [15, 45, 76, 80,  91,  95]
c = [5,  51, 54, 102, 150, 201]
othres = [5, 15, 21, 55, 92, 105]

graph = pygal.Line()

graph.title = "Percentage of users increase of programming languages."
graph.x_labels = years
graph.x_title = "Years"
graph.y_title = "Languages(%)"
graph.add("python", python)
graph.add("Java", java)
graph.add("C++", c)
graph.add("All other languages compined", othres)

graph.render_to_file("langauges.svg")