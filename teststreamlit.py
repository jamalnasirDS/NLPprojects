#!/usr/bin/env python
# coding: utf-8

# In[15]:


##good effort 

import streamlit as st
import numpy as np
import pandas as pd

df = pd.read_csv('d:test2.csv')
st.table(df)

st.dataframe(df)

st.dataframe(df.style.highlight_max(axis=0))


# In[ ]:





# In[ ]:





# In[ ]:




