from setuptools import setup, Extension
import numpy as np

from Cython.Build import cythonize

setup(name='ArtificialsCythonWrapped',
    ext_modules=cythonize(
        Extension("ArtificialsCythonWrapped",
                sources=['ArtificialsCythonWrapped.pyx',],
                requires=['polars','pyarrow',],
                include_dirs=[np.get_include()]), 
        ),
    language_level="3",
    install_requires=['numpy'])

