#!/usr/bin/env python
# coding: utf-8

# In[6]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[3]:


get_ipython().system('pip install numpy')


# In[5]:


get_ipython().system('pip install pandas')


# In[7]:


get_ipython().system('pip install seaborn')
get_ipython().system('pip install matplotlib')


# In[8]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')


# In[52]:


df = pd.read_csv('data/mydata1.csv')


# In[53]:


df.shape


# In[54]:


df.info(verbose=True)


# In[55]:


df.head()


# In[56]:


df.tail()


# In[57]:


df.describe()


# In[66]:


import pandas as pd

df = pd.read_csv('./Data/missing.csv')
display(df)
display(df.isnull())
df.isnull().any()


# In[69]:


df = pd.read_csv('./Data/missing.csv', na_values=['?','na'])
display(df)
df.isnull().any()


# In[70]:


df = pd.read_csv('./Data/missing.csv', na_values=['?','na'])
display(df)
df.dropna()


# In[71]:


df.dropna(axis=0)


# In[72]:


df.dropna(axis=1)


# In[74]:


df = pd.read_csv('./Data/missing.csv', na_values=['?','na'])
display(df)
df=df.fillna(value={'col1':df['col1'].mean(),'col2':df['col2'].mean()})
display(df)


# In[75]:


df = pd.read_csv('./Data/missing.csv', na_values=['?','na'])
display(df)
df=df.fillna(value={'col1':df['col1'].median(),'col2':df['col2'].median()})
display(df)


# In[76]:


df = pd.read_csv('./Data/missing.csv', na_values=['?','na'])
display(df)
df=df.fillna(value={'col1':100,'col2':200})
display(df)


# In[77]:


df = pd.read_csv('./Data/missing.csv', na_values=['?','na'])
display(df)
dummies = pd.get_dummies(df['col3'])
display(dummies)


# In[78]:


df = pd.concat([df,dummies],axis=1)
display(df)


# In[79]:


df.drop('col3', axis=1, inplace=True)
display(df)


# In[80]:


df=pd.read_csv('http://bit.ly/2vmLyvU')
all_mean = df.mean()
all_max = df.max()
all_min = df.min()
all_median = df.median()
all_std = df.std()
all_25_quantile = df.quantile(0.25)

print('The means of all data.')
print(all_mean)


# In[81]:


df=pd.read_csv('http://bit.ly/2vmLyvU')
target = 'radius_mean'


# In[82]:


max = df[target].max()
min = df[target].min()
range =  max - min
print('The max is %.1f, the min is %.1f and the range is %.1f' % (max, min, range))


# In[83]:


mean = df[target].mean()
median = df[target].median()
mode = df[target].mode()
print('The mean is %.1f, the median is %.1f and the mode is %.1f.' % (mean, median, mode))


# In[84]:


q1 = df[target].quantile(0.25)
q3 = df[target].quantile(0.75)
iqr = q3-q1
print('The lower quartile is %.1f, the upper quartile is %.1f and the interquartile range is %.1f' % (q1, q3, iqr))


# In[85]:


df[target].plot()


# In[86]:


df[target].plot(kind='hist')


# In[87]:


df[target].plot.hist()


# In[88]:


df[target].plot.hist(bins=100)


# In[89]:


df[target].plot(kind='box')


# In[92]:


data =[df['radius_mean'],df['texture_mean'],df['texture_worst']]
green_diamond = dict(markerfacecolor='g', marker='D')
fig7, ax7 = plt.subplots()
ax7.set_title('Multiple Samples with Different sizes')
ax7.boxplot(data,flierprops=green_diamond)
plt.show()


# In[93]:


plt.hist([df['radius_mean'], 
          df['texture_mean']], 
         histtype='barstacked',
         orientation='horizontal',bins=20)
plt.show()


# In[94]:


sns.boxplot(x='diagnosis', y='perimeter_mean', data=df)


# In[ ]:




