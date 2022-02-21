from setuptools import setup

from Cython.Build import cythonize

setup(ext_modules=cythonize("Artificials_CythonWrapped.pyx",language_level="3"))

