import matplotlib.pylab as plt
import pygal

years = ['2011','2012','2013','2014','2015','2016']
python = [15, 31, 89, 200, 356, 900]
java = [15, 45, 76, 80,  91,  95]
c = [5,  51, 54, 102, 150, 201]
othres = [5, 15, 21, 55, 92, 105]


fig, ax = plt.subplots(figsize=(7, 7))
plt.plot(years, python, c='yellow', label="Python")
plt.plot(years, java, c="red", label="Java")
plt.plot(years, c, c="blue", label="C++")
plt.plot(years, othres, c="black", label="All other languages compined")

plt.title("Percentage of users increase of programming languages.", fontsize=14)
plt.xlabel("Years", fontsize=14)
plt.ylabel("languages", fontsize=14)
plt.tick_params(axis='both', labelsize=14)
#ax.axhline(400, ls='--', color='r')

plt.legend()
plt.show()


