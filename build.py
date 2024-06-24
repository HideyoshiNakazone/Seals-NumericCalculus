import os
import numpy


try:
    from Cython.Build import cythonize
except ImportError:
    def build(setup_kwargs):
        pass
else:
    from setuptools import Extension
    from setuptools.dist import Distribution
    from setuptools.command.build_ext import build_ext


    def build_ext_modules_array(ext: list[dict]) -> list[Extension]:
        return [
            Extension(
                name=e['name'],
                sources=[e['path']],
                extra_compile_args=['-O3', '-fopenmp'],
                extra_link_args=['-fopenmp'],
                language='c',
            ) for e in ext
        ]

    def build(setup_kwargs):
        extensions = [
            {"name": "yoshi_seals.shared.array", "path": "yoshi_seals/shared/array.pyx"},
            {"name": "yoshi_seals.process.process", "path": "yoshi_seals/process/process.pyx"},
        ]

        setup_kwargs.update({
            'ext_modules': cythonize(
                build_ext_modules_array(extensions),
                language_level=3,
                compiler_directives={'linetrace': True},
            ),
            'include_dirs': [numpy.get_include()],
            'cmdclass': {'build_ext': build_ext}
        })
