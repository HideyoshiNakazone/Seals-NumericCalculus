import numpy
from Cython.Build import cythonize
from setuptools import Extension, setup

ext_modules = [
    Extension(
        "yoshi_seals.shared.array",
        [
            "yoshi_seals/shared/array.pyx",
        ],
        extra_compile_args=["-O3", "-fopenmp"],
        extra_link_args=['-fopenmp'],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")],
    ),
    Extension(
        "yoshi_seals.process.process",
        [
            "yoshi_seals/process/process.pyx",
        ],
        extra_compile_args=["-O3", "-fopenmp"],
        extra_link_args=['-fopenmp'],
        define_macros=[("NPY_NO_DEPRECATED_API", "NPY_1_7_API_VERSION")]
    ),
]

setup(
    ext_modules=cythonize(ext_modules),
    include_dirs=[numpy.get_include()]
)
