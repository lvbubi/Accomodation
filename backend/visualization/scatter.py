import matplotlib.pyplot as plt
from pandas import np

from service.csv_parser import parse_data_to_dict


dict = parse_data_to_dict()

values = dict['county']['vegzettseg.csv']['A'].values

x = np.arange(start=0, stop=len(values), step=1)
y = values

plt.scatter(x, y)

ax = plt.gca()
ax.axes.xaxis.set_visible(False)
#ax.axes.yaxis.set_visible(False)

plt.grid(True)
plt.show()
