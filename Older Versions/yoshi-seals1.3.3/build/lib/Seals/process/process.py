# Seals - Program made for educational intent, can be freely distributed
# and can be used for economical intent. I will not take legal actions
# unless my intelectual propperty, the code, is stolen or change without permission.  

# Copyright (C) 2020  VItor Hideyoshi Nakazone Batista

# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License version 2 as published by
# the Free Software Foundation.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.

# You should have received a copy of the GNU General Public License along
# with this program; if not, write to the Free Software Foundation, Inc.,
# 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301 USA.

import numpy as np
import math

def identity(matrix):
    
    i = 0
    
    while (i < matrix.shape[0]):
        
        j = 0
        
        while (j < matrix.shape[0]):
            
            if (i == j):
                
                matrix[i][j] = 1
                
            elif (i != j):
                
                matrix[i][j] = 0
                        
            j += 1
        
        i += 1
        
    return matrix

def gauss(matrix):
    
    i = 0
    k = 0
    
    while (i < matrix.shape[0]):
        
        if (matrix[i][i] == 0):
            
            n = i
            
            while (matrix[i][i] == 0) and (n < matrix.shape[0]):
                
                temp = matrix[i].copy()
                matrix[i] = matrix[n]
                matrix[n] = temp
                
                n += 1
        
        while (k < matrix.shape[0]):
            
            if (k == i) or (matrix[i][i] == 0):
                
                k += 1
                
            else:
                
                mult = matrix[k][i]/matrix[i][i]
                matrix[k] = matrix[k] - mult*matrix[i]
                k += 1
            
        i += 1
        k = 0
    
    i = 0
    
    while ((i) < matrix.shape[0]) and (matrix[i][i] != 0):
        
        matrix[i] = matrix[i]/matrix[i][i]
        i += 1        
    
    return matrix[:,(matrix.shape[0]):]

def inverse(matrix):
    
    return gauss(np.hstack((matrix, identity(np.zeros(matrix.shape)))))

def cholesky(A, b):
    
    g = np.zeros((A.shape))
    
    i = 0
    j = 0
    
    while j < A.shape[1]:
        while i < A.shape[0]:

            if i == 0 and j == 0:

                g[i][j] = math.sqrt(A[0][0])

            elif j == 0:

                g[i][j] = A[i][0]/g[0][0]

            elif i == j:

                k = 0
                theta = 0

                while k < i:

                    theta += g[i][k]**2
                    k += 1
                
                g[i][j] = math.sqrt(A[i][i] - theta) 

            else:

                k = 0
                theta = 0

                while k < j:

                    theta += g[i][k]*g[j][k]
                    k += 1

                g[i][j] = (A[i][j] - theta)/g[j][j]

            i += 1

        j += 1
        i = j
                
    y = (inverse(g)).dot(b) 
    
    x = (inverse(g.T)).dot(y)
    
    return x

def decomposition(U, b):
    
    L = identity(np.zeros(U.shape))

    i = 0
    k = 0

    while (i < U.shape[0]):
        
        k = 0

        if (U[i][i] == 0):
            
            n = i
            
            while (U[i][i] == 0) and (n < U.shape[0]):
                
                temp = U[i].copy()
                U[i] = U[n]
                U[n] = temp
                
                n += 1
        
        while (k < U.shape[0]):
            
            if (k <= i) or (U[i][i] == 0):
                
                k += 1
                
            else:
                L[k][i] = U[k][i]/U[i][i]
                U[k] = U[k] - L[k][i]*U[i]
                k += 1
            
        i += 1

    y = (inverse(L)).dot(b) 
    
    x = (inverse(U)).dot(y)
    
    return x
    
def cramer(A, b):

    x = np.vstack(np.zeros(b.shape))
    k = 0

    while (k < A.shape[0]):

        temp = A.copy()
        temp[:,k] = b

        x[k] = np.linalg.det(temp)/np.linalg.det(A)
        
        k += 1
    
    return x