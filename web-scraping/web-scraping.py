# https://www.crummy.com/software/BeautifulSoup/
# conda install beautifulsoup4

from urllib.request import urlopen

import pandas as pd
from bs4 import BeautifulSoup
from matplotlib import pyplot as plt

# %matplotlib inline

url = "https://www.hubertiming.com/results/2018MLK"  # open link
html = urlopen(url)

soup = BeautifulSoup(html)
title = soup.title
print(title.text)

links = soup.find_all('a', href=True)
for link in links:
    print(link['href'])

data = []
allrows = soup.find_all("tr")
# print(allrows)
# print(allrows[:10])
for row in allrows:
    row_list = row.find_all("td")
    dataRow = []
    for cell in row_list:
        dataRow.append(cell.text)
    data.append(dataRow)
# titles = data[0]
data = data[4:]
# print(titles)
print(data[-2:])

df = pd.DataFrame(data)
print(df)
print(df.head(2))
print(df.tail(2))

header_list = []
col_headers = soup.find_all("th")
for col in col_headers:
    header_list.append(col.text)
# print(col_headers)
print(header_list)

df.columns = header_list
print(df.head())
print(df.info())
print(df.shape)
df2 = df.dropna(how='any')
print(df2.shape)

# df2['ChipTime_minutes'] = pd.to_timedelta(df2['Time'])
# df2['ChipTime_minutes'] = df2['ChipTime_minutes'].astype('timedelta64[s]')/60
# print(df2['ChipTime_minutes'].info())
print(df2['Time'].info())
print(df2[['Gender', 'Time']].tail())
#
# plt.bar(df2['Gender'], df2['Time'])
# plt.xlabel('Gender')
# plt.ylabel('Time')
# plt.title('comparison of average minutes run by male and female')
# print(df2.describe(include=[np.number]))
# print(df2.boxplot(column='Time', by='Gender'))
# plt.title('')
# print(plt.ylabel('Run Time'))

# age vs Chip time in minutes
df2['Age_i'] = round(pd.to_numeric(df2['Age'], errors='coerce'))
df2.dropna(how='any', inplace=True)
plt.scatter(df2['Time'], df2['Age_i'])
plt.show()
