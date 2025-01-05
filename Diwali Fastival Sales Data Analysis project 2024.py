#!/usr/bin/env python
# coding: utf-8

# # Installing packages, Loading and inspecting dataset to have a sneak peek
# 

# In[1]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


# In[3]:


df = pd.read_csv(r'D:\Diwali_Sales_dataset.csv',encoding = "unicode_escape")
df


# In[4]:


df.shape


# In[5]:


df.head()


# # Data Cleaning and Preparing for analysis

# In[6]:


df.info()


# In[12]:


df.drop(["Status", "unnamed1"], axis = 1, inplace = True)


# In[13]:


df.info()


# In[16]:


pd.isnull(df).sum()


# In[ ]:


#changing 


# In[57]:


#Checking data type after the conversion


# In[28]:


df["Amount"].dtypes


# In[29]:


df.columns


# In[30]:


df.rename(columns = {"Cust_name": "Customer_name", "Marital_Status": "Relationship_Status"}, inplace = True)


# In[32]:


df.columns


# In[33]:


df[["Orders", "Amount"]].describe()


# # Exploratory Data Analysis

# In[34]:


data = sns.countplot(x = "Gender", data = df)


for bars in data.containers:
    data.bar_label(bars)


# In[35]:


sales_gen = df.groupby(["Gender"], as_index = False) ["Amount"].sum().sort_values(by = "Amount", ascending = False)

data = sns.barplot(x = "Gender", y = "Amount", data = sales_gen)

for index, row in sales_gen.iterrows():
    data.text(index, row["Amount"], row["Amount"], ha="center")


# # Based on Age

# In[36]:


data = sns.countplot(x = "Age Group", data = df, hue = "Gender")

for bars in data.containers:
    data.bar_label(bars)


# In[37]:


sales_age = df.groupby(["Age Group"], as_index = False) ["Amount"].sum().sort_values(by = "Amount", ascending = False)

data = sns.barplot(x = "Age Group", y = "Amount", data = sales_age)

for index, row in sales_age.iterrows():
    data.text(index, row["Amount"], row["Amount"], ha="center")


# # Based on States

# In[38]:


sales_state = df.groupby(["State"], as_index = False) ["Orders"].sum().sort_values(by = "Orders", ascending = False).head(10)

sns.set(rc={"figure.figsize":(18,5)})
data = sns.barplot(x = "State", y = "Orders", data = sales_state)


# In[39]:


sales_state = df.groupby(["State"], as_index = False) ["Amount"].sum().sort_values(by = "Amount", ascending = False).head(10)

sns.set(rc={"figure.figsize":(18,5)})
data = sns.barplot(x = "State", y = "Amount", data = sales_state)


# # Based on Relationship Statsu

# In[42]:


data = sns.countplot(x = "Relationship_Status", data = df)

sns.set(rc={"figure.figsize":(8,5)})
for bars in data.containers:
    data.bar_label(bars)


# In[43]:


sales_state = df.groupby(["Relationship_Status", "Gender"], as_index = False) ["Amount"].sum().sort_values(by = "Amount", ascending = False)

sns.set(rc={"figure.figsize":(8,5)})
data = sns.barplot(x = "Relationship_Status", y = "Amount", data = sales_state, hue = "Gender")


# # Based on Occupation

# In[46]:


data = sns.countplot(x = "Occupation", data = df)

sns.set(rc={"figure.figsize":(18,5)})
for bars in data.containers:
    data.bar_label(bars)


# In[47]:


sales_state = df.groupby(["Occupation"], as_index = False) ["Amount"].sum().sort_values(by = "Amount", ascending = False)

sns.set(rc={"figure.figsize":(18,5)})
data = sns.barplot(x = "Occupation", y = "Amount", data = sales_state)


# # Based on Product Category

# In[48]:


data = sns.countplot(x = "Product_Category", data = df)

sns.set(rc={"figure.figsize":(20,5)})
for bars in data.containers:
    data.bar_label(bars)


# In[50]:


sales_state = df.groupby(["Product_Category"], as_index = False) ["Amount"].sum().sort_values(by = "Amount", ascending = False).head(10)

sns.set(rc={"figure.figsize":(22,5)})
data = sns.barplot(x = "Product_Category", y = "Amount", data = sales_state)


# In[53]:


sales_state = df.groupby(["Product_ID"], as_index = False) ["Orders"].sum().sort_values(by = "Orders", ascending = False).head(10)

sns.set(rc={"figure.figsize":(22,5)})
data = sns.barplot(x = "Product_ID", y = "Orders", data = sales_state)


# In[ ]:





# In[ ]:




