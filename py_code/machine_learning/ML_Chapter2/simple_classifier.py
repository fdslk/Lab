import numpy as np
import matplotlib.pyplot as plt

x = np.array([[3,1], [2,5], [1,8],[6,4],[5,2],[3,5],[4,7],[4,-1]])
y = [0, 1, 1, 0, 0, 1, 1, 0]
class_0 = np.array([x[i] for i in range(len(x)) if y[i] == 0])
class_1 = np.array([x[i] for i in range(len(x)) if y[i] == 1])
line_x = range(10)
line_y = line_x

plt.figure()
plt.scatter(class_0[:,0], class_0[:,1], color='black', marker='s')
plt.scatter(class_1[:,0], class_1[:,1], color='black', marker='x')
plt.plot(line_x, line_y, color='black', linewidth=4)
plt.show()