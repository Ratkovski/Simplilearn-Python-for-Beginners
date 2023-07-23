# Numpy
import matplotlib
import numpy as np

a = np.array([1, 2, 3])
print(type(a))
print(a.shape)
b = np.arange(12).reshape(3, 4)

# scipy

from scipy import constants

print(constants.c)  # speed of light
print(constants.h)  # plank's 'constant
print(constants.N_A)  # Avogadro's number


# Pandas
import pandas as pd
df = pd.DataFrame(np.random.randn(6,4), index=list(range(6)), columns=list('ABCD'))
print(df)
print(df.describe())


#matplotlib

import numpy as np
import matplotlib.pyplot as plt
#%matplotlib inline

np.random.seed(10)
N=30
x=np.random.rand(N)
y=np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N))**2
# area = (30 * np.random.rand(N)) grafico fica menor
plt.scatter(x, y, s=area, c=colors, alpha=0.4)
print(plt.show())

from matplotlib import style
style.use('ggplot')

x1 = [2,4,6]
y1= [12,14,16]

x2 = [3,3,4]
y2 = [7,14,5]

plt.bar(x1, y1, color='r', align='center')
plt.bar(x2, y2, color='b', align='center')

plt.title('Info')
plt.ylabel('Y axis')
plt.xlabel('X axis')
print(plt.show())


