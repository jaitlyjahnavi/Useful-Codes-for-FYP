import matplotlib.pyplot as plt
from matplotlib.pyplot import pie, axis, show

import pandas as pd

plt.style.use('bmh')
df=pd.read_csv('County_2020.csv')

x=df['Country']
y=df['Commits 2020']

plt.xlabel('Country',fontsize=18)
plt.ylabel('Commits 2020',fontsize=16)
plt.bar(x,y)

#plt.pie(y,labels=x,radius=1.2,autopct='%0.01f%%',shadow=True)
#sums=df.groupby(df["Country"])["Commits 2020"].sum()
#axis('equal')
#pie(sums, labels=sums.index)


plt.show()