#!/usr/bin/env python
# coding: utf-8

# In[11]:


import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

x=["2-tone", "Grey", "White", "Ash", "Navy Blue", "Black", "Black"]
y=["Mercedez-Benz Maybach GLS 600", "Mercedes Benz AMG G 63", "Mercedes Benz C-Class", "Mercedes Benz V-Class", "Mercedes Benz E-Class", "Mercedes-Benz GLA", "Mercedes-Benz S-Class"]

plt.bar(x,y, color="b", align="center")
plt.ylabel("Cars")
plt.xlabel("Colors")
plt.title("PRODUCT AND COLOR")
plt.show()


# In[8]:


x="White","Black","Ash","2-tone","Navy Blue", "Grey"
y=700,800,400,100,500,200

plt.bar(x,y, color="g", align="center")
plt.ylabel("Numbers sold so far")
plt.xlabel("Colors sold so far")
plt.title("Mercedes-Benz: Numbers & Colors sold")
plt.show()


# In[4]:


x="S-Class","C-Class","E-Class","GLA","Maybach", "GLS 600"
y=200,400,800,100,500,700

plt.bar(x,y, color="y", align="center")
plt.xlabel("Model")
plt.ylabel("Numbers sold")
plt.title("Mercedes-Benz: Models and the numbers sold")
plt.show()


# In[9]:


x="S-Class","C-Class","E-Class","GLA","Maybach", "GLS 600"
y=200,100,400,600,300,200

plt.bar(x,y, color="r", align="center")
plt.xlabel("Model")
plt.ylabel("Numbers available for sale")
plt.title("Mercedes-Benz: Models and the numbers available")
plt.show()


# In[ ]:




