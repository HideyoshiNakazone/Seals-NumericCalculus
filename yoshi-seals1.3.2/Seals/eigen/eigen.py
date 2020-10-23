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

def eigen(a):

    k = 0
    l = np.ones((a.shape[0]))

    at = a #variavel temporaria para A

    while (k < at.shape[0]):

        u = np.random.rand(at.shape[0],1)
        u = u/max(u.min(), u.max(), key=abs)

        ctrl = 0

        while (ctrl != l[k]):
            
            ctrl = l[k]
            u = at.dot(u)
            l[k] = max(u.min(), u.max(), key=abs)
            u = u/l[k]


        i = 0

        while (u[i] == 0):
            i += 1

        at = at - (1/u[i])*u*at[i]
        k += 1

    i = 0
    b = np.random.rand(a.shape[0],a.shape[1])

    while (i < l.shape[0]):

        alpha = 0.999*l[i]

        t = np.random.rand(a.shape[0],1)

        b[i] = b[i]/max(b[i].min(), b[i].max(), key=abs)
        t = l/max(l.min(), l.max(), key=abs)

        while not (np.allclose(b[i],t,atol=10**(-17))):
            t = b[i].copy()
            b[i] = np.linalg.solve((a - alpha*np.identity(a.shape[0])),((l[i]-alpha)*t))
            b[i] = b[i]/max(b[i].min(), b[i].max(), key=abs)
        
        i += 1

    return l, b