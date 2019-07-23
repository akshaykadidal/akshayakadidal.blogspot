#!/usr/bin/env python
# coding: utf-8

# In[6]:


from sklearn.preprocessing import MinMaxScaler
import pandas as pd
from scipy.spatial import distance_matrix
scaler = MinMaxScaler(feature_range=(0, 1))


# In[ ]:


import plotly
plotly.offline.init_notebook_mode(connected=True)
import plotly.offline as py
import plotly.graph_objects as go


# In[26]:


comp = pd.read_csv("companies.csv", delimiter = ',', engine='python')
cont = pd.read_csv("countries_budget.csv")


# In[27]:


cont = cont.set_index('Country')
comp = comp.set_index('Company')


# In[28]:


cont = cont.dropna()
comp = comp.dropna()


# In[29]:


dm = pd.DataFrame(distance_matrix(cont.values, comp.values), index=cont.index, columns=comp.index)


# In[ ]:


comp = pd.read_csv("companies.csv", delimiter = ',', engine='python')
cont = pd.read_csv("countries.csv")


# In[30]:


(dm.min(axis = 1).idxmin(axis=0), dm.min(axis = 0).idxmin(axis=0), dm.min(axis = 1).min())


# In[31]:


dm['Country']=dm.index


# In[32]:


melted_data = dm.melt(id_vars=['Country'], var_name='Compnay',value_name = 'Distance')


# In[33]:


melted_data[melted_data.Distance<30000].sort_values(by = ['Distance']).head(10)


# In[34]:


countries = melted_data[melted_data.Distance<30000].sort_values(by = ['Distance'])['Country'].head(50).unique()
companies = melted_data[melted_data.Distance<30000].sort_values(by = ['Distance'])['Compnay'].head(50).unique()


# In[35]:


x = cont[cont.index.isin(countries)]
y = comp[comp.index.isin(companies)]


# In[37]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=x.Rev, y=x.Employees,
                    mode='markers',
                    name='Countries',
                    text=x.index))
fig.add_trace(go.Scatter(x=y.Rev, y=y.Employees,
                    mode='markers',
                    name='Companies',
                    text=y.index))

fig.update_xaxes(title_text='Revenue')
fig.update_yaxes(title_text='Employee')

fig.show()


# In[42]:


x


# In[3]:


cont = cont.set_index('Country')
comp = comp.set_index('Company')


# In[4]:


cont = cont.dropna()
comp = comp.dropna()


# In[7]:


dm = pd.DataFrame(distance_matrix(cont.values, comp.values), index=cont.index, columns=comp.index)


# In[8]:


(dm.min(axis = 1).idxmin(axis=0), dm.min(axis = 0).idxmin(axis=0), dm.min(axis = 1).min())


# In[13]:


dm['Country']=dm.index


# In[14]:


melted_data = dm.melt(id_vars=['Country'], var_name='Compnay',value_name = 'Distance')


# In[15]:


melted_data[melted_data.Distance<30000].sort_values(by = ['Distance']).head(10)


# In[16]:


countries = melted_data[melted_data.Distance<30000].sort_values(by = ['Distance'])['Country'].head(50).unique()
companies = melted_data[melted_data.Distance<30000].sort_values(by = ['Distance'])['Compnay'].head(50).unique()


# In[17]:


x = cont[cont.index.isin(countries)]
y = comp[comp.index.isin(companies)]


# In[22]:





# In[25]:


fig = go.Figure()
fig.add_trace(go.Scatter(x=x.Rev, y=x.Employees,
                    mode='markers',
                    name='Countries',
                    text=x.index))
fig.add_trace(go.Scatter(x=y.Rev, y=y.Employees,
                    mode='markers',
                    name='Companies',
                    text=y.index))

fig.update_xaxes(title_text='Revenue')
fig.update_yaxes(title_text='Employee')

fig.show()


# In[ ]:




