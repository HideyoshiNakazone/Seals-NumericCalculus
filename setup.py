import setuptools
import os

__name = "yoshi_seals"

__version_sufix = os.environ.get('VERSION_SUFIX')
if not __version_sufix:
    __version_sufix = "dev"

__version = f"2.0.{__version_sufix}"

with open("README.md", "r") as fh:
    long_description = fh.read()

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
