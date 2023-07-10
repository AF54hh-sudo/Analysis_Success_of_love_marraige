#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[2]:


data = pd.read_csv('C:\\Users\\Lenovo\\Desktop\\love marriage data.csv')
print(data)


# In[3]:


data.head(15)


# In[4]:


data.tail(15)


# In[5]:


data.info()


# In[6]:


data.dropna(axis=0)


# In[7]:


data.describe(include="all")


# In[8]:


data.columns


# In[9]:


data.groupby('age')['gender'].mean().sort_values()


# In[10]:


title =  sns.scatterplot(data=data['status'].head(10))
rating = sns.scatterplot(data=data['gender'].head(10))
title=['age']
Rating=['gender']
plt.title("love Relationship")
plt.ylabel("status")
plt.xlabel("age")
bar_width=0.70
plt.legend(["gender", "orange - age"], loc ="lower right")
plt.plot(Rating,title,bar_width,color='red')
plt.show()


# In[11]:


sns.scatterplot(data=data['religion'].head(10))

plt.ylabel( "Gender")
plt.xlabel('Names ')
plt.title("Love sucess")
plt.show()


# In[12]:


plt.figure(figsize = (30,10))
plt.title('religion distribution')
sns.countplot(x=data['religion'].head(30), data = data )
plt.show()


# In[13]:


sns.lineplot(x="age", y ="gender", data = data)
sns.set_style("dark")
plt.show()


# In[14]:


sns.relplot(x='religion', y='age', data = data)

plt.show()


# In[15]:


sns.scatterplot(x = 'age', y= 'religion', data = data)
plt.show()


# In[16]:


sns.stripplot(x='gender', y='age' , data =data)
plt.show()


# In[17]:


sns.histplot(x='religion', y='status', data=data)
plt.show()


# In[31]:


data = [15,15,30,12,40,20]
mylabels = ["Christianity","judaism","Islam","Budhidsm","Hindu","Sikh"]
myexplode = [0,0,0,0,0.2,0]
colors = ("cyan","brown","green","indigo","orange","grey")
plt.pie(data, labels = mylabels, explode = myexplode,shadow = True,
       colors = colors)
plt.show()


# In[ ]:




