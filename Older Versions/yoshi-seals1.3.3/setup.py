import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="yoshi-seals",
    version="1.3.3",
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