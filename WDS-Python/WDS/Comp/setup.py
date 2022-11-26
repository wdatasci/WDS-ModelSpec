from setuptools import setup, Extension
import numpy as np

from Cython.Build import cythonize

setup(name='Artificials_CythonWrapped',
    ext_modules=cythonize(
        Extension("Artificials_CythonWrapped",
                sources=['Artificials_CythonWrapped.pyx',],
                requires=['polars','pyarrow',],
                include_dirs=[np.get_include()]), 
        ),
    language_level="3",
    install_requires=['numpy'])

