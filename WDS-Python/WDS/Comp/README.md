# Artificials

To compare both Cython, raw, and JIT versions of the Artificials.h C code

* Build
    This assumes that cython and python3 distributions and dependencies are available.

    Build with:  
        (rm __init__.py if it tries to install in a WDS subdirectory)
        export CPPFLAGS=-I/usr/local/lib/python3.9/dist-packages/numpy/core/include
        python3 setup.py build_ext --inplace; python3 setup.py clean --all
        (echo "pass" > __init__.py if necessary)

