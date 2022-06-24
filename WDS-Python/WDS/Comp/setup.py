from setuptools import setup

from Cython.Build import cythonize

setup(ext_modules=cythonize("ArtificialsCythonWrapped.pyx",language_level="3"))

