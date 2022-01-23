#!/usr/bin/env python
# coding: utf-8

# # Project of Seattle Airbnb
# 
# ## Questions:
# ### 1. What is the average price of the Airbnbs in Seattle?
# ### 2. Which variable have the stongest correlation to the price of an Airbnb?
# ### 3. Which price range has the most number of Airbnb?

# In[1]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# ### Prepare the dataset

# In[2]:


calender = pd.read_csv("calendar.csv")
listings = pd.read_csv("listings.csv")


# In[3]:


calender.head()


# In[4]:


listings.head()


# In[5]:


df1 = pd.merge(calender, listings, left_on='listing_id', right_on='id', how='left').drop('id', axis=1)


# In[6]:


df1 = df1.fillna(-1)


# In[7]:


df1.head()


# ## 1. What is the average price of the Airbnbs in Seattle?

# In[8]:


import plotly.offline as py
import plotly.express as px
import plotly.graph_objects as go
import plotly.offline as pyo
from plotly.subplots import make_subplots
import seaborn as sns
from statistics import mean


# In[9]:


prices = [i for i in df1['price_x'] if not -1]

for i in list(df1['price_y']):
    if i != -1:
        prices.append(i)


# In[10]:


price = []

for i in prices:
    i = i[:-2]
    i = ''.join(e for e in i if e.isalnum())
    price.append(int(i))


# In[11]:


average = mean(price)


# In[12]:


average


# In[13]:


trace = go.Box(y=price, name='Price')

data = [trace]

layout = go.Layout(title='Boxplot of Price', hovermode='x')

fig = go.Figure(data=data, layout=layout)

fig.show()


# It is easy to see that the averge price of Aribnb in Seattle is $127.98

# ## 2. Which variable have the stongest correlation to the price of an Airbnb?

# In[14]:


fig=plt.figure(figsize=(12,8), dpi= 100, facecolor='w', edgecolor='k')
M0 = sns.heatmap(df1.corr(), annot = True).set_title('Airbnb Seattle corresponding correlation')


# Based on the color of the heatmap. It is easy to see that all varibles related to reviews and availability. host_listings_count have very strong correlation to the price of an Airbnb.

# ## 3. Which price range has the most number of Airbnb?

# In[15]:


fig = px.histogram(price)
fig.show()


# So it is clearly to see that most of the price of airbnbs are between 35 to 175 and 150 has the most number of airbnbs

# In[ ]:




