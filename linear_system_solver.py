#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np

def find_nonzero_row(matrix, pivot_row, col):

    nrows = matrix.shape[0]

    for row in range(pivot_row, nrows):

        if matrix[row, col] != 0:

            return row

    return None
 
# Swapping rows so that we can have our non zero row on the top of the matrix

def swap_rows(matrix, row1, row2):

    matrix[[row1, row2]] = matrix[[row2, row1]]


    
def eliminate_below(matrix, pivot_row, col):

    nrows = matrix.shape[0]

    pivot_element = matrix[pivot_row, col]

    for row in range(pivot_row + 1, nrows):
        
        factor1=matrix[pivot_row,col]

        factor2 = matrix[row, col]
        
        matrix[row] = (factor1 * matrix[row]) - (factor2 * matrix[pivot_row])       

def row_echelon_form(matrix):

    ncols = matrix.shape[1]

    pivot_row = 0
# this will run for number of column times. If matrix has 3 columns this loop will run for 3 times

    for col in range(ncols):

        nonzero_row = find_nonzero_row(matrix, pivot_row, col)

        if nonzero_row is not None:

            swap_rows(matrix, pivot_row, nonzero_row)

            eliminate_below(matrix, pivot_row, col)

            pivot_row += 1

    return matrix


# In[2]:


def is_consistent(ref_matrix):
    # Check for inconsistency by finding a row with all zeros in the coefficients and a non-zero constant
    for row in ref_matrix:
        if np.all(row[:-1] == 0) and row[-1] != 0:
            return False
    return True

def is_unique_solution(ref_matrix):
    c=0;
    for row in ref_matrix:
        leading_index = np.argmax(row[:-1] != 0)
        if(row[leading_index]!=0):
            c+=1
    if(c==ref_matrix.shape[1]-1):
        return True
    else:
        return False
        

def find_solution(ref_matrix,val=1):
    num_variables = ref_matrix.shape[1] - 1
    solution = np.array(np.ones(num_variables)*np.inf)
    #solution = np.zeros(num_variables)

    for i in range(ref_matrix.shape[0] - 1, -1, -1):
        leading_index = np.argmax(ref_matrix[i, :-1] != 0)
        if(ref_matrix[i,leading_index]!=0):
            if leading_index < num_variables:
                for j in range (leading_index+1,num_variables):
                    if(solution[j]==np.inf):
                        solution[j]=val
                solution[leading_index] = (ref_matrix[i, -1] - np.dot(ref_matrix[i, leading_index+1:-1], solution[leading_index+1:]))/ref_matrix[i,leading_index]
    
    return solution
def solve_linear_system(augmented_matrix):
    ref_matrix=row_echelon_form(augmented_matrix)
    if not is_consistent(ref_matrix):
        return "The system is inconsistent."

    if not is_unique_solution(ref_matrix):
        # Return any 5 solutions in a 2D array
        solutions=[]
        for i in range(1,6):
            solutions.append(find_solution(ref_matrix,i))
        return np.array( solutions)
    else:
        # Return the unique solution in an array
        unique_solution = find_solution(ref_matrix)
        return unique_solution

    
matrix = np.array([[2,1,3,7,5],[0,0,6,0,9],[0,0,0,0,0]])
res=solve_linear_system(matrix)
print(res)


# In[ ]:




