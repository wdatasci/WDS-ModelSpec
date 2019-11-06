/* from swig example
   File : example.i */
%module WDS_zzzExamples_lua_swig_example1

%inline %{
    extern int    gcd(int x, int y);
    extern double Foo;
%}
