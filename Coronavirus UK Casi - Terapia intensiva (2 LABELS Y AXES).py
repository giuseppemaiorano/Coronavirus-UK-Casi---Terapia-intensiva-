#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[5]:


df = pd.read_csv("overview_2021-07-04 (2).csv")
df.head(10)


# In[6]:


df = df.drop(['areaCode'], axis=1)
df = df.drop(['areaType'], axis=1)
df = df.drop(['areaName'], axis=1)
df


# In[7]:


df = df.sort_values(by=['date'])


# In[8]:


for i in range(0,df.shape[0]-13):
    df.loc[df.index[i+13],'SMA_14'] = np.round(((df.iloc[i,1]+ df.iloc[i+1,1] +df.iloc[i+2,1]+df.iloc[i+3,1]+ df.iloc[i+4,1]+ df.iloc[i+5,1]+ df.iloc[i+6,1]+ df.iloc[i+7,1]+ df.iloc[i+8,1]+ df.iloc[i+9,1]+ df.iloc[i+10,1]+ df.iloc[i+11,1]+ df.iloc[i+12,1]+ df.iloc[i+13,1])/14),1)


# In[9]:


df['pandas_SMA_14'] = df.iloc[:,1].rolling(window=14).mean()


# In[12]:


plt.figure(figsize=[15,10])
plt.style.use('ggplot')
plt.grid(True)
plt.plot(df['date'], df['SMA_14'], label='Casi Giornalieri media mobile 14', linewidth=3, color = 'blue')
plt.xticks([0, 100, 200, 300, 400, 500], rotation=30)
plt.axis([0, 525, 0, 60000])
plt.xlabel('Giorni')
plt.ylabel('Casi Giornalieri')
plt.title("Casi Giornalieri UK", fontsize=20)
plt.legend(loc=2)


# In[19]:


df2 = pd.read_csv("overview_2021-07-04 (1).csv")
df2.head(10)


# In[20]:


df2 = df2.drop(['areaCode'], axis=1)
df2 = df2.drop(['areaType'], axis=1)
df2 = df2.drop(['areaName'], axis=1)


# In[21]:


df2


# In[22]:


df2 = df2.sort_values(by=['date'])


# In[23]:


df2


# In[25]:


plt.figure(figsize=[15,10])
plt.style.use('ggplot')
plt.grid(True)
plt.plot(df2['date'], df2['covidOccupiedMVBeds'], label='Casi Giornalieri', linewidth=2, linestyle='--')
plt.xticks([0, 100, 200, 300, 400], rotation=30)
plt.axis([0, 460, 0, 5000])
plt.xlabel('Giorni')
plt.ylabel('Casi Giornalieri')
plt.title("Casi Giornalieri UK", fontsize=20)
plt.legend(loc=2)


# In[ ]:





# In[29]:


df3 = df.drop(df.index[0:65])


# In[30]:


df3


# In[44]:


fig, ax1 = plt.subplots()
fig.set_figheight(15)
fig.set_figwidth(15)
plt.style.use("ggplot")
plt.grid(False)

color = 'tab:red'
ax1.set_xlabel('Data')
ax1.set_ylabel('Casi', color=color)
ax1.plot(df3['date'], df3['SMA_14'], color=color, linewidth=4, label='Casi')
ax1.tick_params(axis='y', labelcolor=color)


ax2 = ax1.twinx() 

color = 'tab:blue'
ax2.set_ylabel('terapia intensiva', color=color) 
ax2.plot(df3['date'], df2['covidOccupiedMVBeds'], color=color, linewidth=4, label='Terapia intensiva')
ax2.tick_params(axis='y', labelcolor=color)

fig.tight_layout()  
plt.xticks([0, 100, 200, 300, 400], rotation=30)
plt.axvspan(201.8, 202.5, color='green', alpha=0.5)
plt.axvspan(455.8, 456.2, color='purple', alpha=0.5)
plt.axhspan(300, 750, color='orange', alpha=0.5)
plt.title("Casi e Terapia Intensiva UK", fontsize=20)
plt.show()


# In[ ]:





# In[ ]:




