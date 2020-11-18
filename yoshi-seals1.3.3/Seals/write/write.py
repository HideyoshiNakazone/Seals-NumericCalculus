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

import csv
import numpy as np
import pandas as pd

class numpy:

    def __init__(self):
        pass
    def csv(self, array, path):

        with open(path, mode='w') as sistema_linear:

            solution_writer = csv.writer(sistema_linear, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
            solution_writer.writerows(array)

    def txt(self, array, path):

        np.savetxt(path, array, fmt='%8f', delimiter=' ', \
            newline='\n', header='', footer='', comments='# ', encoding=None)

class pandas:

    def __init__(self):
        pass
    def csv(self, df, path):

        df.to_csv(path)

    def txt(self, df, path):

        np.savetxt(path, df.values, fmt='%8f', delimiter=' ', \
            newline='\n', header='', footer='', comments='# ', encoding=None)
