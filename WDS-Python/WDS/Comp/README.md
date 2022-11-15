# Artificials

To compare both Cython, raw, and JIT versions of the Artificials.h C code

* Build
    This assumes that cython and python3 distributions and dependencies are available.

    Update to work with anaconda on windows (works also in WSL2 ubuntu):
        Build with:
            python setup.py build_ext --inplace
            python setup.py clean -all
        setting CPPFLAGS for the numpy include location is no longer necessary


    Old - Build with:  
        (rm __init__.py if it tries to install in a WDS subdirectory)
        export CPPFLAGS=-I/usr/local/lib/python3.9/dist-packages/numpy/core/include
        python3 setup.py build_ext --inplace; python3 setup.py clean --all
        (echo "pass" > __init__.py if necessary)

