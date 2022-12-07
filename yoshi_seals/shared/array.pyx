from libc.stdlib cimport malloc

cimport numpy as np
import numpy as np


cdef double[::] mult(double[::] array, double value):

    cdef int size = array.shape[0], i = 0

    cdef:
        double *c_pointer = <double *> malloc(size*sizeof(double))
        double[::] mult_array = <double[:size]>c_pointer

    for i in range(size):

        mult_array[i] = array[i]*value

    return mult_array

cdef double[::] div(double[::] array, double value):

    cdef int size = array.shape[0], i = 0

    cdef:
        double *c_pointer = <double *> malloc(size*sizeof(double))
        double[::] mult_array = <double[:size]>c_pointer

    for i in range(size):

        mult_array[i] = array[i]/value

    return mult_array

cdef double[::] addition(double[::] a, double[::] b):

    cdef int size_a = a.shape[0], size_b = b.shape[0], i = 0
    cdef double *c_pointer = <double *> malloc(size_a*sizeof(double))
    cdef double[::] mult_array = <double[:size_a]>c_pointer

    for i in range(size_a):

        mult_array[i] = a[i] + b[i]

    return mult_array

cdef double[::] subtract(double[::] a, double[::] b):

    cdef int size_a = a.shape[0], size_b = b.shape[0], i = 0
    cdef double *c_pointer = <double *> malloc(size_a*sizeof(double))
    cdef double[::] mult_array = <double[:size_a]>c_pointer

    for i in range(size_a):

        mult_array[i] = a[i] - b[i]

    return mult_array

cdef double[::,::] identity(int size):

    cdef int i = 0

    cdef double *c_pointer = <double *> malloc(size*size*sizeof(double))
    cdef double[::,:] matrix = <double[:size,:size]>c_pointer

    for i in range(size):
        for j in range(size):
            if i == j:
                matrix[i][j] = 1

            elif i != j:
                matrix[i][j] = 0

    return matrix

cdef double[:,:] zeros((int, int) size):

    cdef int i = 0, j = 0

    cdef:

        double *c_pointer = <double *> malloc(size[0]*size[1]*sizeof(double))
        double[:,:] id_array = <double[:size[0],:size[1]]>c_pointer

    if not c_pointer:
        raise MemoryError()

    for i in range(size[0]):
        for j in range(size[1]):
            id_array[i,j] = 0.0

    return id_array

cdef double[:,:] ones((int, int) size):

    cdef int i = 0, j = 0

    cdef:

        double *c_pointer = <double *> malloc(size[0]*size[1]*sizeof(double))
        double[:,:] id_array = <double[:size[0],:size[1]]>c_pointer

    for i in range(size[0]):
        for j in range(size[1]):
            id_array[i,j] = 1.0

    return id_array

cdef double[:,:] hstack(double[:,:] a, double[:,:] b):

    cdef:

        int i, j
        int a_x = a.shape[0], a_y = a.shape[1]
        int b_x = b.shape[0], b_y = b.shape[1]
        int size_x = a_x, size_y = a_y + b_y

        double *c_pointer = <double *> malloc(size_x*size_y*sizeof(double))
        double[::,::] matrix = <double[:size_x,:size_y]>c_pointer

    if a_x != b_x:
        raise ValueError("Cannot hstack matrices")

    for i in range(size_x):
        for j in range(size_y):
            if j < a_y:
                matrix[i,j] = a[i,j]
            else:
                matrix[i,j] = b[i,j-a_y]

    return matrix

cdef double[:,:] vstack(double[:,:] a, double[:,:] b):

    cdef:

        int i, j
        int a_x = a.shape[0], b_x = b.shape[0]
        int a_y = a.shape[1], b_y = b.shape[1]
        int size_x = a_x + b_x, size_y = a_y

        double *c_pointer = <double *> malloc(size_x*size_y*sizeof(double))
        double[:,:] matrix = <double[:size_x,:size_y]>c_pointer

    if a_y != b_y:
        raise ValueError("Cannot vstack matrices")

    for i in range(size_x):
        for j in range(size_y,):
            if i < a_x:
                matrix[i,j] = a[i,j]
            else:
                matrix[i,j] = b[i-a_x, j]

    return matrix

cdef double[:,:] inverse(double[:,:] a):

    cdef:

        int i = 0, k = 0, n, size = a.shape[0]

        double[:,:] matrix = hstack(a,identity(size))
        double mult_const
        double[:] tmp

    if a.shape[0] != a.shape[1]:
        raise ValueError("Non Quadratic Matrix doesn't have an Inverse Matrix")

    for i in range(size):

        if matrix[i][i] == 0:

            n = i

            while (matrix[i][i] == 0) and (n < size):

                tmp = matrix[i]
                matrix[i] = matrix[n].copy()
                matrix[n] = tmp

                n += 1

        for k in range(size):

            if (k != i) and (matrix[i][i] != 0):

                mult_const = matrix[k][i]/matrix[i][i]
                matrix[k] = subtract(matrix[k], mult(matrix[i], mult_const))

        for k in range(size):
            if matrix[k][k] != 0:
                matrix[k] = div(matrix[k], matrix[k][k])

    return matrix[:,size:]

cdef double[:,:] transpose(double[:,:] a):

    cdef:

        int size_x = a.shape[0], size_y = a.shape[1]

        double *c_pointer = <double *> malloc(size_y*size_x*sizeof(double))
        double[:,:] tmp = <double[:size_y,:size_x]>c_pointer

    for i in range(size_x):
        for j in range(size_y):
            tmp[j,i] = a[i,j]

    return tmp

cdef double[:,:] dot(double[:,:] a, double[:,:] b):
    c = np.zeros((a.shape[0], b.shape[1]))

    for i in range(a.shape[0]):
        for j in range(b.shape[1]):
            for k in range(a.shape[0]):
                c[i][j] += a[i][k] * b[k][j]

    return c

cdef double det(double[::,::] a):

    cdef:

        double[:,:] tmp
        double total = 0, sub_det

        int size_x = a.shape[0], size_y = a.shape[1], i

    if size_x != size_y:
        raise ValueError("Determinant Operation is only valid for Quadratic Matrices.")

    if size_x == 2 and size_y == 2:
        total = a[0][0] * a[1][1] - a[1][0] * a[0][1]
        return total

    for i in range(size_x):

        tmp = a.copy()
        tmp = tmp[1:]

        for i in range(size_y):
            tmp[i] = addition(tmp[i][0:i], tmp[i][i + 1:])

        sign = (-1) ** (i % 2)
        sub_det = det(tmp)

        total += sign * a[0][i] * sub_det

    return total