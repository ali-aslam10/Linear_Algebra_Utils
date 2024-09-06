import numpy as np
import copy

# Helper functions
def find_nonzero_row(matrix, pivot_row, col):
    nrows = matrix.shape[0]
    for row in range(pivot_row, nrows):
        if matrix[row, col] != 0:
            return row
    return None

def swap_rows(matrix, row1, row2):
    matrix[[row1, row2]] = matrix[[row2, row1]]

# Row Echelon Form (REF)
def eliminate_below(matrix, pivot_row, col):
    nrows = matrix.shape[0]
    for row in range(pivot_row + 1, nrows):
        factor1 = matrix[pivot_row, col]
        factor2 = matrix[row, col]
        matrix[row] = (factor1 * matrix[row]) - (factor2 * matrix[pivot_row])

def row_echelon_form(matrix):
    ncols = matrix.shape[1]
    pivot_row = 0
    for col in range(ncols):
        nonzero_row = find_nonzero_row(matrix, pivot_row, col)
        if nonzero_row is not None:
            swap_rows(matrix, pivot_row, nonzero_row)
            eliminate_below(matrix, pivot_row, col)
            pivot_row += 1
    return matrix

# Reduced Row Echelon Form (RREF)
def eliminate_above_and_below(matrix, pivot_row, col):
    nrows = matrix.shape[0]
    matrix[pivot_row] = matrix[pivot_row] / matrix[pivot_row, col]
    for row in range(nrows):
        if row != pivot_row:
            factor = matrix[row, col]
            matrix[row] = matrix[row] - (factor * matrix[pivot_row])

def reduced_row_echelon_form(matrix):
    ncols = matrix.shape[1]
    pivot_row = 0
    for col in range(ncols):
        nonzero_row = find_nonzero_row(matrix, pivot_row, col)
        if nonzero_row is not None:
            swap_rows(matrix, pivot_row, nonzero_row)
            eliminate_above_and_below(matrix, pivot_row, col)
            pivot_row += 1
    return matrix

# Is RREF Checker
def is_rref(mat):
    row_count = mat.shape[0]
    pre_lead = -1
    for i in range(row_count):
        leading_index = np.argmax(mat[i, :] != 0)
        if leading_index == 0 and mat[i, leading_index] == 0:
            if np.any(mat[i:] != 0):
                return False
            else:
                return True
        if leading_index < pre_lead or mat[i, leading_index] != 1:
            return False
        pre_lead = leading_index
        for j in range(row_count):
            if j != i and mat[j, leading_index] != 0:
                return False
    return True

# Solving Linear Systems
def is_consistent(ref_matrix):
    for row in ref_matrix:
        if np.all(row[:-1] == 0) and row[-1] != 0:
            return False
    return True

def is_unique_solution(ref_matrix):
    count = 0
    for row in ref_matrix:
        leading_index = np.argmax(row[:-1] != 0)
        if row[leading_index] != 0:
            count += 1
    return count == ref_matrix.shape[1] - 1

def find_solution(ref_matrix, val=1):
    num_variables = ref_matrix.shape[1] - 1
    solution = np.array([np.inf] * num_variables)
    for i in range(ref_matrix.shape[0] - 1, -1, -1):
        leading_index = np.argmax(ref_matrix[i, :-1] != 0)
        if ref_matrix[i, leading_index] != 0:
            for j in range(leading_index + 1, num_variables):
                if solution[j] == np.inf:
                    solution[j] = val
            solution[leading_index] = (ref_matrix[i, -1] - np.dot(ref_matrix[i, leading_index + 1:-1], solution[leading_index + 1:])) / ref_matrix[i, leading_index]
    return solution

def solve_linear_system(augmented_matrix):
    ref_matrix = row_echelon_form(augmented_matrix)
    if not is_consistent(ref_matrix):
        return "The system is inconsistent."
    if not is_unique_solution(ref_matrix):
        solutions = [find_solution(ref_matrix, i) for i in range(1, 6)]
        return np.array(solutions)
    else:
        return find_solution(ref_matrix)

# Inverse of Matrix by Gaussian Elimination
def matrix_inverse_gaussian_elimination(A):
    if A.shape[0] != A.shape[1]:
        return "Matrix is not invertible."
    
    N = A.shape[0]
    inverse_matrix = np.eye(N)
    test_matrix_copy = copy.deepcopy(A)

    for i in range(N):
        coeff = test_matrix_copy[i][i]
        for j in range(i + 1, N):
            mult = -test_matrix_copy[j][i] / coeff
            test_matrix_copy[j] += mult * test_matrix_copy[i]
            inverse_matrix[j] += mult * inverse_matrix[i]
        test_matrix_copy[i] /= coeff
        inverse_matrix[i] /= coeff

    for i in range(N - 1, -1, -1):
        coeff = test_matrix_copy[i][i]
        for j in range(i - 1, -1, -1):
            mult = -test_matrix_copy[j][i] / coeff
            test_matrix_copy[j] += mult * test_matrix_copy[i]
            inverse_matrix[j] += mult * inverse_matrix[i]

    if not is_rref(test_matrix_copy):
        return "Matrix is not invertible."
    return inverse_matrix
