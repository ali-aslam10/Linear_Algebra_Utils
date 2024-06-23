#!/usr/bin/env python
# coding: utf-8

# In[2]:


import numpy as np
def is_rref(mat):
    row=mat.shape[0]
    pre_lead=-1
    for i in range(row):
        leading_index = np.argmax(mat[i, :] != 0)
        if(leading_index==0 and mat[i,leading_index]==0): #if  all row zero
            if(np.any(mat[i:]!=0)):   # then if it is not at last
                return False
            else:
                return True
        if(leading_index<pre_lead or mat[i,leading_index]!=1):   #pivot should be one
            return False
        pre_lead=leading_index
        for j in range(0,row):  #check above and below Zero
            if(j==i):
                continue
            if(mat[j,leading_index]!=0):
                return False
    return True



mat=np.array([[1,0,0],[0,0,1],[0,0,0]])
print(is_rref(mat))


# In[ ]:




