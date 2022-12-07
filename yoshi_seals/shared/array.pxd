cdef double[::] mult(double[::] array, double value)

cdef double[::] div(double[::] array, double value)

cdef double[::] addition(double[::] a, double[::] b)

cdef double[::] subtract(double[::] a, double[::] b)

cdef double[::,:] hstack(double[:,:] a, double[:,:] b)

cdef double[::,::] vstack(double[:,:] a, double[:,:] b)

cdef double[::,::] identity(int size)

cdef double[:,:] zeros((int, int) sizes)

cdef double[:,:] ones((int, int) sizes)

cdef double[:,:] inverse(double[:,:] a)

cdef double[:,:] transpose(double[:,:] a)

cdef double[:,:] dot(double[:,:] a, double[:,:] b)

cdef double det(double[::,::] a)