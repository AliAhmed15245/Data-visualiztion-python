import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import FuncFormatter

data = {'Barton LLC': 109438.50,
        'Frami, Hills and Schmidt': 103569.59,
        'Fritsch, Russel and Anderson': 112214.71,
        'Jerde-Hilpert': 112591.43,
        'Keeling LLC': 100934.30,
        'Koepp Ltd': 103660.54,
        'Kulas Inc': 137351.96,
        'Trantow-Barrows': 123381.38,
        'White-Trantow': 135841.99,
        'Will LLC': 104437.60}
group_data = list(data.values())
group_names = list(data.keys())
group_mean = np.mean(group_data)



fig, ax = plt.subplots()
plt.style.use('fivethirtyeight')
plt.rcParams.update({'figure.autolayout': True})
plt.barh(group_names, group_data)
labels = ax.get_xticklabels()
plt.setp(labels, rotation=45)
plt.xlabel("Revenue", fontsize=15)
plt.ylabel("Company", fontsize=15)
plt.title("Companies Revenue", fontsize=25)
plt.tick_params(axis='both', labelsize=14)
plt.xlim(-10000, 140000)
ax.axvline(group_mean, ls='--', color='r')
for group in [3, 5, 8]:
    ax.text(145000, group, "New Company", fontsize=10,
            verticalalignment="center")
plt.text(group_mean+3000, "Will LLC", "mean", c="red")
fig.savefig('sales.png', transparent=False, dpi=80, bbox_inches="tight")
plt.show()