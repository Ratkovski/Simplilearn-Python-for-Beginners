from matplotlib import pylab
from pandas.core.computation import align

print(pylab.__version__)

"""Use NumPy to generate random data
"""

import numpy as np

x = np.linspace(0, 10, 25)
y = x * x + 2
print(x)
print(y)
print(np.array([x, y]).reshape(25, 2).reshape(2, 25))

"""It only takes 1 command to draw 
"""
print(pylab.plot(x, y, 'r'))  # 'r'stands for red

"""Drawing a subgraph 
"""

pylab.clf()

pylab.subplot(1, 1, 1)  # the contents of the brackets represent(rows, columns,indexes)
pylab.plot(x, y, 'r--')  # the third parameter here determines color and line style
# pylab.subplot(1, 2, 1)
pylab.plot(x, y, 'g*-')

# operator description
# fig_add_axes() = Initializes subplor a = fig.add_subplot()
# fig,b = plt.subplots(nrows=3,nclos=2) = Adds subplot
# plt.subplots(2,2) = Creates.subplot

from matplotlib import pyplot as plt

fig = plt.figure()
axis = fig.add_axes([0.5, 0.1, 0.8, 0.8])  # control the left, right, width, height of the canvas (from 0 to 1)
print(axis.plot(x, y, 'r'))

# again we can draw subgraphics

fig, axes = plt.subplots(nrows=1, ncols=2)  # submap is of 1 row, 2 colums
for ax in axes:
    print(ax.plot(x, y, 'r'))

# we can also draw a picture, or graph inside another graphic
fig = plt.figure()
# Control the left, right, width and height of the canvas (from 0 to 1)
axes1 = fig.add_axes([0.1, 0.1, 0.8, 0.8])
axes2 = fig.add_axes([0.2, 0.5, 0.4, 0.3])
axes1.plot(x, y, 'r')  # big axes
axes2.plot(x, y, 'g')  # small canvas

fig = plt.figure(figsize=(16, 9), dpi=300)  # new graphic object
fig.add_subplot()
plt.plot(x, y, 'r')

# fig = plt.subplot(figsize=(16,9), dpi=50)
# axes.plot(x,y,'r')

ax.legend(["label1", "label2"])
fig, axes = plt.subplots()
axes.set_xlabel("x-label")
axes.set_ylabel("y-label")

axes.set_title("Title of graph")

# axes.plot(x, y, 'r')
axes.plot(x, x ** 2)
axes.plot(x, x ** 3)

axes.legend(["y = x**2", "y = x**3"], loc=2)

# In matplotlib, you can set other properties such as line color, transparency, and more
fig, axes = plt.subplots(dpi=150)
# axes.plot(x, x + 1, color='red', alpha=.5)
axes.plot(x, x ** 2, color='red', alpha=.8)
axes.plot(x, x + 2, color='#1155dd', alpha=.8)
axes.plot(x, x + 3, color='#15cc55', alpha=.8)

fig, ax = plt.subplots(dpi=100)
# Line width
ax.plot(x, x + 1, color='blue', linewidth=0.25)
ax.plot(x, x + 2, color='blue', linewidth=1)
ax.plot(x, x + 3, color='blue', linewidth=1.5)
ax.plot(x, x + 4, color='blue', linewidth=2)

fig, ax = plt.subplots(dpi=100)
# Line width
ax.plot(x, x + 1, color='blue', lw=2, linewidth='-')
ax.plot(x, x + 2, color='blue', lw=2, linewidth='-.')
ax.plot(x, x + 3, color='blue', lw=2, linewidth=':')

line, = ax.plot(x, x + 4, color='black', lw=1.50)
line.set_dashes([5, 10, 15, 10])

line, = ax.plot(x, x + 5, color='black', lw=1.50)
line.set_dashes([5, 10, 15, 3])

line, = ax.plot(x, x + 6, color='black', lw=1.50)
line.set_dashes([5, 10, 4, 10])

fig, ax = plt.subplots(dpi=100)
# Line width
ax.plot(x, x + 1, color='blue', marker='o')
ax.plot(x, x + 2, color='blue', marker='+')
ax.plot(x, x + 3, color='blue', marker='s')
ax.plot(x, x + 4, color='blue', marker='1')

ax.plot(x, x + 5, color='blue', marker='o', markersize=5)
ax.plot(x, x + 6, color='blue', marker='s', markerfacecolor='red')
ax.plot(x, x + 6, color='blue', marker='s', markersize=15, markerfacecolor='green')

""" Set the canvas grid and axis range
"""

fig, Axes = plt.subplots(1, 2, figsize=(10, 5))
Axes[0].plot(x, x ** 2, x, x ** 3, lw=2)
Axes[0].grid(True)

Axes[1].plot(x, x ** 2, x, x ** 3, lw=2)
Axes[1].set_ylim([0, 60])
Axes[1].set_xlim([2, 5])
Axes[1].grid(True)

# other 2d graphics
n = np.array([0, 1, 2, 3, 4, 5])
fig, axes = plt.subplots(1, 4, figsize=(16, 5))

axes[0].set_title("scatter")
axes[0].scatter(x, x + 0.25 * np.random.randn(len(x)))

axes[1].set_title("step")
axes[1].step(n, n ** 2, lw=2)

axes[2].set_title("bar")
# axes[2].bar(n,n**2, align="center", width=0.5, height=0.5)
axes[2].bar(n, n ** 2, align="center", width=0.5)

axes[3].set_title("fill_between")
axes[3].fill_between(x, x ** 2, x ** 3, color="green", alpha=0.5)

"""Draw a radar chart 
"""
fig = plt.figure(figsize=(6, 6))
# ax = fig.add_axes([0.0, 0.0, .6, .6], polar=True)
ax = fig.add_axes([0.0, 0.0, 1, 1], polar=True)
t = np.linspace(0, 2 * np.pi, 100)
ax.plot(t, t * .5, color='blue', lw=3)

"""Draw a histogram"""
n = np.random.randn(10000)
fig, axes = plt.subplots(1, 2, figsize=(12, 4))
axes[0].set_title("Default histogram")
axes[0].hist(n)

axes[1].set_title("Cumulative detailed histogram")
axes[1].hist(n, cumulative=True, bins=50)

# Draw counter image
import matplotlib
import numpy as np
import matplotlib.cm as cm
import matplotlib.pyplot as plt

delta = 0.025
x = np.arange(-3.0, 3.0, delta)
y = np.arange(-2.0, 2.0, delta)
X, Y = np.meshgrid(x, y)
Z1 = np.exp(-X ** 2 - Y ** 2)
Z2 = np.exp(-(X - 1) ** 2 - (Y - 1) ** 2)
Z = (Z1 - Z2) * 2
print(X)
print(Y)

fig, ax = plt.subplots()
CS = ax.contour(X, Y, Z)
ax.clabel(CS, inline=1, fontsize=10)
ax.set_title('contour map')
