# Seals - Numeric Calculus

This python namespace is made for applied Numeric Calculus of Linear Algebra. It is made with the following objectives in mind:

* Scan *csv* files to make a numpy matrix.

* Write a matrix into a *csv* file.

* Insert user input into a matrix or a vector.

* Calculate Eigenvalues and his Eigenvectors.

* Use methods to proccess the matrices.
  * Identity Matrix
  * Gauss Elimination
  * Inverse Matrix
  * Cholesky Decomposition
  * LU Decomposition
  * Cramer

## Syntax

To call the package *scan* use the syntax: `from yoshi_seals import scan`. The package also has a function for *Numpy* arrays and *Pandas* dataframes, and used the following syntax `scan.np(path)` for *Numpy* and `scan.pd(path)` for *Pandas*, where `path` is the path to your directory.

To call the package *write* use the syntax: `from yoshi_seals import write`. The package also has a function for *Numpy* arrays and *Pandas* dataframes, and uses the following syntax `write.np(array,path)` for *Numpy*, where `array` is the matrix that you desire to output and `path` is the path to your directory, and `write.pd(df,path)` for *Pandas*, where `df` is the matrix that you desire to output and `path` is the path to your directory.

To call the package *insert* use the syntax: `from yoshi_seals import insert`. The package also has a function for *matrix* and another for *vector*, and it has the following syntax `insert.function(array)`, where `insert` is the *Python Module* and `function` is either a `matrix` or a `vector` and `array` is either a *matrix* or a *vector*.

There is also a function that given a matrix it return all real eigenvalues and all real eigenvectors, this function uses the power method to find the eigenvalues and inverse power method for the eigenvector.

### Processes

To call the module `process` use the syntax: `from yoshi_seals import process as sl`, where `sl` is an alias and will be used to call functions: `sl.inverse(array)`.

* The function *gauss* returns a *numpy* vector containing the vector of variables from the augmented matrix. `sl.gauss(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.

* The function *inverse* returns a *numpy* inverse matrix of the matrix passed into to it, and it has the following syntax `sl.inverse(matrix)`, which `matrix` is a square matrix.

* The function *cholesky* returns a *numpy* vector containing the vector of variables from the coefficient matrix and the constants vector, and it has the following syntax `sl.cholesky(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.
  
* The function *decomposition* returns a *numpy* vector containing the vector of variables from the coefficient matrix and the constants vector, and it has the following syntax `sl.decomposition(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.

* The function *cramer* returns a *numpy* vector containing the vector of variables from the coefficient matrix and the constants vector, and it has the following syntax `sl.cramer(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.

## Installation

To install the package from source `cd` into the directory and run:

`pip install .`

or run

`pip install yoshi-seals`
