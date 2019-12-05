#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import Pandas & matplot
import pandas as pd
import matplotlib 
pd.set_option("display.max_column",50)


# In[2]:


#Import Dataset (Survey.csv)
raw_data = pd.read_csv("survey.csv")


# In[3]:


#Print dataset
print(raw_data.head())


# In[4]:


#select Country
unique_Country = raw_data["Country"].drop_duplicates()


# In[5]:


#Print list of Countries
print(unique_Country)


# In[6]:


# select specific Country (France)
country_df = raw_data[raw_data["Country"] == "France"]


# In[7]:


print(country_df)


# In[8]:


# selecting the associated column with menatal health
country_df_hist = country_df[["Age", "Gender","mental_health_consequence"]]


# In[9]:


#Print Gender 
print(country_df_hist.Gender.unique())


# In[10]:


# Replace 'm', 'male',M as Male
country_df_hist["Gender"]= country_df_hist.loc[:,"Gender"].replace(["M", "m","male"],["Male","Male","Male"])


# In[11]:


#Print Gender (Replaced)
print(country_df_hist.Gender.unique())


# In[12]:


# Count &Reset index 
country_df_hist.groupby(["Gender", "mental_health_consequence"])["Age"].count().reset_index()


# In[13]:


#Print define parameters
print(country_df_hist)


# In[14]:


print(country_df_hist.hist())


# In[15]:


# Print Age in ascending metal Health consequence
print(country_df_hist.sort_values("Age", ascending = False))


# In[16]:


#Bar Graph
country_df_hist.hist()

