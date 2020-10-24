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

def matrix(matrix):

    i = 0
    
    while (i < matrix.shape[0]):
        
        j = 0
        
        while (j < matrix.shape[1]):
            
            matrix[i][j] = float(input('Insira o elemento {}x{}: '.format((i+1),(j+1))))
            j += 1
        
        i += 1
        
    return matrix

def vector(vector):
    
    j=0
    
    while (j < vector.shape[0]):
            
        vector[j] = float(input('Insira o elemento b{}: '.format((j+1))))
        j += 1
        
    return vector