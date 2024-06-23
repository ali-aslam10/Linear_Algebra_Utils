#!/usr/bin/env python
# coding: utf-8

# In[2]:


import copy

def matrix_inverse_gausssian_elimination(A):
    if(A.shape[0]!=A.shape[1]):
        return "Matrix is not invertible"
    flag=False
    N=A.shape[0]
    inverse_matrix = np.zeros((N,N))

    for n in range(N):
        inverse_matrix[n][n] = 1.0
        
        
    # Make copy of the test matrix for modifications
    test_matrix_copy = copy.deepcopy(A)
    

    # Make the test matrix upper triangular
    if(not flag):
        
        for i in range(N): # Row
            # The diagonal element
            coeff = test_matrix_copy[i][i] + 0.0 
            
            if(not flag):

                for j in range(i+1, N):
                    # How should we add ith row to jth, to eliminate the ith element
                    mult = -test_matrix_copy[j][i] / coeff


                    test_matrix_copy[j] =test_matrix_copy[j]+ (mult * test_matrix_copy[i])
                    inverse_matrix[j] =inverse_matrix[j]+ (mult * inverse_matrix[i] )
                    if(is_rref(test_matrix_copy)):
                            flag=True
                            break
                   
            factor=test_matrix_copy[i][i]        
            test_matrix_copy[i] =test_matrix_copy[i]/ factor
            inverse_matrix[i] =inverse_matrix[i]/ factor
            if(is_rref(test_matrix_copy)):
                
                flag=True
                break
           
   
    # Diagonalize (same as triangulation but in the opposite direction)
    if(not flag):     
        for i in range(N-1, -1, -1): # Row
            coeff = test_matrix_copy[i][i] + 0.0
            if(not flag):
                for j in range(i-1, -1, -1):
                    mult = -test_matrix_copy[j][i] / coeff


                    test_matrix_copy[j] =test_matrix_copy[j]+ (mult * test_matrix_copy[i])
                    inverse_matrix[j] =inverse_matrix[j] + (mult * inverse_matrix[i] )
                    if(is_rref(test_matrix_copy)):
                            flag=True
                            break

    c=0;
    for row in test_matrix_copy:
        leading_index = np.argmax(row[:] != 0)
        if(row[leading_index]!=0):
            c+=1
    if(c!=A.shape[0]):
        return "Matrix is not invertible"
    else:
        return inverse_matrix

    
matrix=np.array([[4.,3.],[3.,2.]])
matrix_inverse_gausssian_elimination(matrix)


# In[ ]:




