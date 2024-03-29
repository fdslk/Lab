import matplotlib.pyplot as plt
from numpy.random import randn
plt.style.use('ggplot')
data1 = randn(50).cumsum()
data2 = randn(50).cumsum()
data3 = randn(50).cumsum()
data4 = randn(50).cumsum()
fig = plt.figure()
ax1 = fig.add_subplot(1,1,1)
ax1.plot(data1, marker='o', color='blue', linestyle='-', label='Blue Solid')
ax1.plot(data2, marker='+', color='red', linestyle='--', label='red dashed')
ax1.plot(data3, marker='*', color='green', linestyle='-.', label='green dashed dot')
ax1.plot(data4, marker='s', color='orange', linestyle=':', label='orange dotted')
ax1.xaxis.set_ticks_position('bottom')
ax1.yaxis.set_ticks_position('left')
plt.xlabel('Draw')
plt.ylabel('Random Number')
plt.savefig('line_plot.png', dpi=400, bbox_inches='tight')
plt.legend(loc='best')
plt.show()