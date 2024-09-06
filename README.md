# Linear Algebra

## Overview

`linalg_utils` is a Python library for performing essential linear algebra operations. It provides functions for computing Row Echelon Form (REF), Reduced Row Echelon Form (RREF), solving linear systems, and calculating the inverse of matrices using Gaussian Elimination.

## Features

- **Row Echelon Form (REF)**: Transform a matrix into its row echelon form.
- **Reduced Row Echelon Form (RREF)**: Transform a matrix into its reduced row echelon form.
- **RREF Checker**: Check whether a given matrix is in RREF.
- **Linear System Solver**: Solve a system of linear equations, checking for consistency and returning either unique or multiple solutions.
- **Matrix Inverse**: Compute the inverse of a square matrix using Gaussian Elimination.

## Installation

Clone this repository or download `linalg_utils.py` to your local machine.

```bash
git clone https://github.com/ali-aslam10/Linear_Algebra_Utils.git
```
## Usage

You can import the utility functions and use them in your projects.

```python
import numpy as np
from linalg_utils import row_echelon_form, reduced_row_echelon_form, is_rref, solve_linear_system, matrix_inverse_gaussian_elimination

# Example: Row Echelon Form
matrix = np.array([[12, 1, 0], [0, 12, 1], [0, 16, 0]])
print("Row Echelon Form:")
print(row_echelon_form(matrix))

# Example: Reduced Row Echelon Form
matrix = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 0, 1, 2]])
print("Reduced Row Echelon Form:")
print(reduced_row_echelon_form(matrix))

# Example: Is RREF?
matrix = np.array([[1, 0, 0], [0, 0, 1], [0, 0, 0]])
print("Is RREF?:", is_rref(matrix))

# Example: Solving Linear System
aug_matrix = np.array([[2, 1, 3, 7], [0, 0, 6, 9], [0, 0, 0]])
print("Solving Linear System:")
print(solve_linear_system(aug_matrix))

# Example: Matrix Inverse (Gaussian Elimination)
matrix = np.array([[4., 3.], [3., 2.]])
print("Matrix Inverse:")
print(matrix_inverse_gaussian_elimination(matrix))
```

## Functions

### `row_echelon_form(matrix: np.ndarray) -> np.ndarray`
Converts a given matrix into its Row Echelon Form.

### `reduced_row_echelon_form(matrix: np.ndarray) -> np.ndarray`
Converts a given matrix into its Reduced Row Echelon Form.

### `is_rref(matrix: np.ndarray) -> bool`
Checks if a matrix is in Reduced Row Echelon Form (RREF).

### `solve_linear_system(augmented_matrix: np.ndarray) -> Union[str, np.ndarray]`
Solves a system of linear equations represented as an augmented matrix. Returns either a unique solution or multiple solutions.

### `matrix_inverse_gaussian_elimination(matrix: np.ndarray) -> Union[str, np.ndarray]`
Computes the inverse of a square matrix using Gaussian Elimination. Returns the inverse matrix or an error message if the matrix is not invertible.

## Example

Here's an example for computing the inverse of a 2x2 matrix:

```python
import numpy as np
from linalg_utils import matrix_inverse_gaussian_elimination

matrix = np.array([[4., 3.], [3., 2.]])
inverse_matrix = matrix_inverse_gaussian_elimination(matrix)
print("Inverse of the matrix:")
print(inverse_matrix)
```
### Output:

```plaintext
Inverse of the matrix:
[[-2.  3.]
 [ 3. -4.]]
```

## Contributing

Feel free to submit issues or pull requests if you find any bugs or want to improve the functionality of this project.

