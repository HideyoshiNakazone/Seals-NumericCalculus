# Seals - Numeric Calculus

This python package is made for applied Numeric Calculus of Linear Algebra. It is made with the following objectives in mind:

* Scan *csv* files to make a numpy matrix.

* Write a matrix into a *csv* file

* Insert user input into a matrix or a vector.

* Calculate Eigen Values

* Use methods to proccess the matrices.
  * Identity Matrix
  * Gauss Elimination
  * Inverse Matrix
  * Cholesky Decomposition
  * LU Decomposition
  * Cramer

## Syntax

The module *scan* has a function for *Numpy* arrays and *Pandas* dataframes, and used the following syntax `Seals.scan.np(path)` for *Numpy* and `Seals.scan.pd(path)` for *Pandas*, where `path` is the path to your directory.

The module *write* has a function for *Numpy* arrays and *Pandas* dataframes, and uses the following syntax `Seals.write.np(array,path)` for *Numpy*, where `array` is the matrix that you desire to output and `path` is the path to your directory, and `Seals.write.pd(df,path)` for *Pandas*, where `df` is the matrix that you desire to output and `path` is the path to your directory.

The module *insert* has a function for *matrix* and another for *vector*, and it has the following syntax `Seals.insert.function(array)`, where `insert` is the *Python Module* and `function` is either a `matrix` or a `vector` and `array` is either a *matrix* or a *vector*.

There is also a function that given a matrix it return all real eigen values

### Processes

To call the module `process` use the syntax: `sl = Seals.process`, where `sl` is an instance and to use a function you have to append the desired function in front of the instance like: `sl.identity(array)`.

* The function *identity* returns a *numpy* identity matrix of the order of the matrix passed into to it, and it has the following syntax `sl.identity(array)`, which `array` is a square matrix.

* The function *gauss* returns a *numpy* vector containing the vector of variables from the augmented matrix. `sl.gauss(matrix)`, which `matrix` is the augmented matrix.

* The function *inverse* returns a *numpy* inverse matrix of the matrix passed into to it, and it has the following syntax `sl.inverse(matrix)`, which `matrix` is a square matrix.

* The function *cholesky* returns a *numpy* vector containing the vector of variables from the coefficient matrix and the constants vector, and it has the following syntax `sl.cholesky(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.
  
* The function *decomposition* returns a *numpy* vector containing the vector of variables from the coefficient matrix and the constants vector, and it has the following syntax `sl.cholesky(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.

* The function *cramer* returns a *numpy* vector containing the vector of variables from the coefficient matrix and the constants vector, and it has the following syntax `sl.cholesky(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.

## Installation

To install the package from source `cd` into the directory and run:

`pip install .`

or run

`pip install yoshi-seals`
