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

from yoshi_seals.shared cimport array

from libc.stdlib cimport malloc
from libc cimport math

cimport numpy as np
import numpy as np

cpdef double det(double[::,::] a):
    return array.det(a)

cpdef np.ndarray[np.float64_t, ndim=2] inverse(double[::,::] matrix):
    return np.asarray(array.inverse(matrix))

cpdef np.ndarray[np.float64_t, ndim=2] hstack(double[::,::] a, double[::,::] b):
    return np.asarray(array.hstack(a, b))

cpdef np.ndarray[np.float64_t, ndim=2] vstack(double[::,::] a, double[::,::] b):
    return np.asarray(array.vstack(a, b))

cpdef np.ndarray[np.float64_t, ndim=2] gauss(double[::,::] A, double[::,::] b):

    cdef:
        int i = 0, j = 0, k = 0, l = 0, reversed_index = 0

        double[:] tmp
        double sum_var

        double[::,::] a = array.hstack(A,b)

        double *c_pointer = <double *> malloc(A.shape[1]*sizeof(double))
        double[:] x = <double[:A.shape[1]]>c_pointer

    if not c_pointer:
        raise MemoryError()

    for i in range(A.shape[0]):

        l = 1
        while i < A.shape[1] and a[i][i] == 0 and (l + i) < A.shape[0]:

            tmp = a[i]
            a[i] = a[i+l]
            a[i+l] = tmp

            l += 1

        for k in range(i + 1, A.shape[1]):

            if a[k][i] != 0:
                a[k] = array.subtract(a[k],array.mult(a[i], (a[k][i]/a[i][i])))

    for j in range(A.shape[1]):

        sum_var = 0
        reversed_index = (A.shape[1] - 1) - j

        for k in range(reversed_index,A.shape[1]):
            sum_var += a[reversed_index][k]*x[k]
        x[reversed_index] = (a[reversed_index][A.shape[1]] - sum_var)/a[reversed_index][reversed_index]

    return np.asarray(x).reshape(b.shape[0],b.shape[1])

cpdef np.ndarray[np.float64_t, ndim=2] cholesky(double[:,:] A, double[:,:] b):

    cdef:
        int i = 0, j = 0, size_x = A.shape[0], size_y = A.shape[1]

        double *c_pointer = <double *> malloc(size_x*size_y*sizeof(double))
        double[::,::] g = <double[:size_x,:size_y]>c_pointer, y, x

    while j < size_y:
        while i < size_x:
            if i == 0 and j == 0:
                g[i][j] = math.sqrt(A[0][0])

            elif j == 0:
                g[i][j] = A[i][0] / g[0][0]

            elif i == j:
                k = 0
                theta = 0

                while k < i:
                    theta += g[i][k] ** 2
                    k += 1

                g[i][j] = math.sqrt(A[i][i] - theta)

            else:
                k = 0
                theta = 0

                while k < j:
                    theta += g[i][k] * g[j][k]
                    k += 1

                g[i][j] = (A[i][j] - theta) / g[j][j]

            i += 1

        j += 1
        i = j

    y = array.dot(array.inverse(g), b)

    x = array.dot(array.inverse(array.transpose(g)), y)

    return np.asarray(x)


cpdef np.ndarray[np.float64_t, ndim=2] decomposition(double[::,::] U, double[::,::] b):

    cdef:
        int i = 0, k = 0

        double[::,::] L = array.identity(U.shape[0]), y, x

    for i in range(U.shape[0]):

        if U[i][i] == 0:

            n = i

            while (U[i][i] == 0) and (n < U.shape[0]):
                temp = U[i].copy()
                U[i] = U[n]
                U[n] = temp

                n += 1

        for k in range(U.shape[0]):

            if (k > i) and (U[i][i] != 0):

                L[k][i] = U[k][i] / U[i][i]
                U[k] = array.subtract(U[k], array.mult(U[i], L[k][i]))

    y = array.dot(array.inverse(L), b)

    x = array.dot(array.inverse(U), y)

    return np.asarray(x)

cpdef np.ndarray[np.float64_t, ndim=2] cramer(double[:,:] A, double[:,:] b):

    cdef:
        int size_a_y = A.shape[0], size_a_x = A.shape[1]
        int size_b_y = b.shape[0], size_b_x = b.shape[1]

        int k = 0

        double *c_pointer_tmp = <double *> malloc(size_a_x*size_a_y*sizeof(double))
        double[::,::] tmp = <double[:size_a_y,:size_a_x]>c_pointer_tmp

        double *c_pointer_x = <double *> malloc(size_b_x*size_b_y*sizeof(double))
        double[::,::] x = <double[:size_b_y,:size_b_x]>c_pointer_x

    if size_a_y != size_b_y:
        raise ValueError("The matrices must have the same height.")
    if size_b_x != 1:
        raise ValueError("The b matrix must be a column matrix.")

    for k in range(size_a_x):
        tmp = A.copy()

        for i in range(size_a_y):
            tmp[i, k] = b[i,0]

        x[k,0] = np.linalg.det(tmp) / np.linalg.det(A)

        k += 1

    return np.asarray(x)