#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import pandas_datareader.data as web
import datetime


# In[2]:


stockdata = pd.read_csv('csv/prices.csv')


# In[3]:


stockdata


# In[4]:


stockdata.sort_values(by='date')


# In[5]:


desc=stockdata.describe()


# In[6]:


desc


# In[ ]:





# In[22]:


google = stockdata[stockdata['symbol']=='GOOG']
google = google.set_index('date')


# In[23]:


google


# In[9]:


tesla = stockdata[stockdata['symbol']=='TSLA']


# In[10]:


tesla.set_index('date')


# In[11]:


microsoft = stockdata[stockdata['symbol']=='MSFT']
microsoft = microsoft.set_index('date')


# In[12]:


microsoft


# In[13]:


ge = stockdata[stockdata['symbol']=='GE'].set_index('date')


# In[14]:


ge


# In[24]:


google['open'].plot(label = 'GOOGL opening rate',legend = True, figsize = (12,5),title='Google Stock Prices')
google['close'].plot(label = 'GOOGL closing rate',legend = True, figsize = (12,5))
google['high'].plot(label = 'GOOGL maximum rate',legend = True, figsize = (12,5))
google['low'].plot(label = 'GOOGL minimum rate',legend = True, figsize = (12,5))


# In[16]:


ge['open'].plot(label = 'GE opening rate',legend = True, figsize = (12,5),title='GE Stock Prices')
ge['close'].plot(label = 'GE closing rate',legend = True, figsize = (12,5))
ge['high'].plot(label = 'GE maximum rate',legend = True, figsize = (12,5))
ge['low'].plot(label = 'GE minimum rate',legend = True, figsize = (12,5))


# In[17]:


microsoft['open'].plot(label = 'MSFT opening rate',legend = True, figsize = (12,5),title='Microsoft Stock Prices')
microsoft['close'].plot(label = 'MSFT closing rate',legend = True, figsize = (12,5))
microsoft['high'].plot(label = 'MSFT maximum rate',legend = True, figsize = (12,5))
microsoft['low'].plot(label = 'MSFT minimum rate',legend = True, figsize = (12,5))


# In[18]:


sns.pairplot(google)


# In[19]:


sns.pairplot(microsoft)


# In[20]:


sns.pairplot(stockdata)


# In[57]:


google['close'].plot(label = 'GOOGL',legend = True, figsize = (12,5),title='CLosing Stock Prices')
microsoft['close'].plot(label = 'MSFT',legend = True, figsize = (12,5))
tesla['close'].plot(label = 'TSLA',legend = True, figsize = (12,5))
ge['close'].plot(label = 'GE',legend = True, figsize = (12,5))


# In[52]:


newdf = pd.DataFrame(columns=["GOOG","MSFT","GE"])
newdf['GOOG'] =google['close']
newdf['MSFT'] = microsoft['close']
newdf['GE'] = ge['close']


# In[53]:


newdf


# In[62]:


#Calculating Simple moving average
newdf['GOOG'].plot(label = 'No moving average',legend = True, figsize = (12,5),title='CLosing Stock Prices')
newdf['GOOG20'] = newdf['GOOG'].rolling(20).mean()
newdf['GOOG20'].plot(label = 'GOOG20',legend = True, figsize = (12,5),title='CLosing Stock Prices')
newdf['GOOG50'] = newdf['GOOG'].rolling(50).mean()
newdf['GOOG50'].plot(label = 'GOOG50',legend = True, figsize = (12,5),title='CLosing Stock Prices')
newdf['GOOG90'] = newdf['GOOG'].rolling(90).mean()
newdf['GOOG90'].plot(label = 'GOOG90',legend = True, figsize = (12,5),title='MOVING AVERAGE')


# In[63]:


#Calculating Simple moving average
newdf['GE'].plot(label = 'No moving average',legend = True, figsize = (12,5),title='CLosing Stock Prices')
newdf['GE20'] = newdf['GE'].rolling(20).mean()
newdf['GE20'].plot(label = 'GE20',legend = True, figsize = (12,5),title='CLosing Stock Prices')
newdf['GE50'] = newdf['GE'].rolling(50).mean()
newdf['GE50'].plot(label = 'GE50',legend = True, figsize = (12,5),title='CLosing Stock Prices')
newdf['GE90'] = newdf['GE'].rolling(90).mean()
newdf['GE90'].plot(label = 'GE90',legend = True, figsize = (12,5),title='MOVING AVERAGE')


# In[65]:






