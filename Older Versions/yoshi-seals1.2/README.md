# Seals - Numeric Calculus

This python package is made for applied Numeric Calculus of Linear Algebra. It is made with the following objectives in mind:

* Scan *csv* files to make a numpy matrix.

* Write a matrix into a *csv* file

* Insert user input into a matrix or a vector.

* Use methods to proccess the matrices.
  * Identity Matrix
  * Gauss Elimination
  * Inverse Matrix
  * Cholesky Decomposition
  * LU Decomposition
  * Cramer

## Syntax

The function *scan* has the following syntax `scan(path)`, where `path` is the path to your directory.

The function *solution* has the following syntax `write(array,path)`, where `array` is the matrix that you desire to output and `path` is the path to your directory.

The python class *Insert* has a method for *matrix* and another for *vector*, and it has the following syntax `Insert.method(array)`, where `Insert` is the *Python Class* and `method` is either a `matrix` or a `vector` and `array` is either a *matrix* or a *vector*.

### Processes

The python class *process* has all the methods described in the first session.

To call the method use a syntax like `sl = Seals.process()`, where `sl` is an instance and to use a method you have to append the method in front of the instance like: `sl.identity(array)`.

* The method *identity* returns a *numpy* identity matrix of the order of the matrix passed into to it, and it has the following syntax `sl.identity(array)`, which `array` is a square matrix.

* The method *gauss* returns a *numpy* vector containing the vector of variables from the augmented matrix. `sl.gauss(matrix)`, which `matrix` is the augmented matrix.

* The method *inverse* returns a *numpy* inverse matrix of the matrix passed into to it, and it has the following syntax `sl.inverse(matrix)`, which `matrix` is a square matrix.

* The method *cholesky* returns a *numpy* vector containing the vector of variables from the coefficient matrix and the constants vector, and it has the following syntax `sl.cholesky(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.
  
* The method *decomposition* returns a *numpy* vector containing the vector of variables from the coefficient matrix and the constants vector, and it has the following syntax `sl.cholesky(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.

* The method *cramer* returns a *numpy* vector containing the vector of variables from the coefficient matrix and the constants vector, and it has the following syntax `sl.cholesky(A,b)`, which `A` is the coefficient matrix and `b` is the constants vector.

## Installation

To install the package from source `cd` into the directory and run:

`pip install .`

or run

`pip install yoshi-seals`
