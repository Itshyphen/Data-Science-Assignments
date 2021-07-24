#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


#read csv file
fundamental = pd.read_csv('fundamentals.csv')


# In[3]:


fundamental


# In[4]:


#1.Select columns ‘Ticker Symbol’, ‘Total Revenue’, and ‘Earnings Before Tax’
df = fundamental[['Ticker Symbol', 'Total Revenue','Earnings Before Tax']]


# In[5]:


df


# In[6]:


#2.Select only two companies google ( ‘Ticker Symbol’ ==’GOOG’) and Apple (‘Ticker Symbol’ ==’AAPL’)
df2 = fundamental.loc[(fundamental['Ticker Symbol']=='GOOG') | (fundamental['Ticker Symbol']=='AAPL' )]


# In[7]:


df2


# In[8]:


#3.Find the Earning Per Share of ‘GOOG” and “AAPL” = Earnings Before Tax’/’Total Equity’
df2['Earning Per Share'] = df2['Earnings Before Tax']/df2['Total Equity']


# In[9]:


df2


# In[10]:


#5.Select companies with Negative earning (with loss)
df3 = fundamental.loc[fundamental['Earnings Before Tax']<0]


# In[11]:


df3


# In[12]:


#4.
df4 = fundamental.loc[fundamental['Total Revenue']>1e9]


# In[13]:


df4


# In[14]:


df5 = fundamental.loc[fundamental['Total Revenue']<1e9]


# In[15]:


df5


# In[16]:


df6 = df4.loc[df4['Total Revenue']<1e10]


# In[17]:


df6


# In[18]:


#top 10 companies on the basis of total revenue
df7 = fundamental.sort_values('Total Revenue')['Ticker Symbol'].head(10)


# In[19]:


df7


# In[20]:


#Dropp and remove null values if found
fundamental.dropna()


# In[21]:


fundamental.groupby(by = 'Ticker Symbol')


# In[22]:


fundamental.sort_values('Period Ending', ascending = False)


# In[23]:


fundamental.rename(columns = {'Ticker Symbol':'Symbol'})


# In[24]:


fundamental.drop(columns = ['Ticker Symbol','Accounts Payable'])


# In[25]:


fundamental.filter(regex = '^Capital')


# In[ ]:





# In[ ]:





# In[ ]:





# In[29]:


sns.boxplot(data=df)


# In[30]:


sns.swarmplot(x='Earnings Before Tax',y='Total Revenue',data = df)


# In[31]:


corr = df.corr()


# In[33]:


sns.heatmap(corr)


# In[ ]:





# In[ ]:




