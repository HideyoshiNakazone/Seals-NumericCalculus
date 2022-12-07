from setuptools import Extension, setup
from Cython.Build import cythonize
import setuptools
import numpy
import os


__name = "yoshi-seals"

__version_sufix = os.environ.get('VERSION_SUFIX')
if not __version_sufix:
    __version_sufix = "dev"

__version = f"2.0.{__version_sufix}"

with open("README.md", "r") as fh:
    long_description = fh.read()


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

setuptools.setup(
    name=__name,
    version=__version,
    author="Vitor Hideyoshi",
    author_email="vitor.h.n.batista@gmail.com",
    description="Numeric Calculus python module in the topic of Linear Algebra",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/HideyoshiNakazone/Seals-NumericCalculus.git",
    packages=setuptools.find_packages(),
    ext_modules=cythonize(ext_modules),
    include_dirs=[numpy.get_include()],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v2 (GPLv2)",
        "Operating System :: OS Independent"
    ],
    python_requires='>=3.6',
    install_requires=[
        'numpy',
        'pandas',
    ],
)
