#!/usr/bin/env python
# coding: utf-8

# In[ ]:


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


    
def eliminate_above_and_below(matrix, pivot_row, col):

    nrows = matrix.shape[0]
    
    matrix[pivot_row]=matrix[pivot_row]/matrix[pivot_row,col]

    pivot_element = matrix[pivot_row, col]
    
    for row in range(0,pivot_row):

        factor = matrix[row, col]
                
        matrix[row] = matrix[row] - (factor * matrix[pivot_row])


    for row in range(pivot_row + 1, nrows):

        factor = matrix[row, col]
        
        matrix[row] = matrix[row] - (factor * matrix[pivot_row])
    

def reduced_row_echelon_form(matrix):

    ncols = matrix.shape[1]

    pivot_row = 0
# this will run for number of column times. If matrix has 3 columns this loop will run for 3 times

    for col in range(ncols):

        nonzero_row = find_nonzero_row(matrix, pivot_row, col)

        if nonzero_row is not None:

            swap_rows(matrix, pivot_row, nonzero_row)

            eliminate_above_and_below(matrix, pivot_row, col)

            pivot_row += 1

    return matrix



mat=np.array([[1,2,3,4],[5,6,7,8],[9,0,1,2]])
print(reduced_row_echelon_form(mat))

