from autodoc import *

def check(got, expected):
  if expected != got:
    raise RuntimeError("\n" + "Expected: [" + expected + "]\n" + "Got     : [" + got + "]")

check(A.__doc__, "Proxy of C++ A class")
check(A.funk.__doc__, "just a string")
check(A.func0.__doc__, "func0(self, arg2, hello) -> int")
check(A.func1.__doc__, "func1(A self, short arg2, Tuple hello) -> int")
check(A.func2.__doc__,  "\n"
"        func2(self, arg2, hello) -> int\n"
"\n"
"        Parameters:\n"
"            arg2: short\n"
"            hello: int tuple[2]\n"
"\n"
"        "
)
check(A.func3.__doc__,  "\n"
"        func3(A self, short arg2, Tuple hello) -> int\n"
"\n"
"        Parameters:\n"
"            arg2: short\n"
"            hello: int tuple[2]\n"
"\n"
"        "
)

check(A.func0default.__doc__, "\n"
"        func0default(self, e, arg3, hello, f=2) -> int\n"
"        func0default(self, e, arg3, hello) -> int\n"
"        "
)
check(A.func1default.__doc__, "\n"
"        func1default(A self, A e, short arg3, Tuple hello, double f=2) -> int\n"
"        func1default(A self, A e, short arg3, Tuple hello) -> int\n"
"        "
)
check(A.func2default.__doc__,  "\n"
"        func2default(self, e, arg3, hello, f=2) -> int\n"
"\n"
"        Parameters:\n"
"            e: A *\n"
"            arg3: short\n"
"            hello: int tuple[2]\n"
"            f: double\n"
"\n"
"        func2default(self, e, arg3, hello) -> int\n"
"\n"
"        Parameters:\n"
"            e: A *\n"
"            arg3: short\n"
"            hello: int tuple[2]\n"
"\n"
"        "
)
check(A.func3default.__doc__,  "\n"
"        func3default(A self, A e, short arg3, Tuple hello, double f=2) -> int\n"
"\n"
"        Parameters:\n"
"            e: A *\n"
"            arg3: short\n"
"            hello: int tuple[2]\n"
"            f: double\n"
"\n"
"        func3default(A self, A e, short arg3, Tuple hello) -> int\n"
"\n"
"        Parameters:\n"
"            e: A *\n"
"            arg3: short\n"
"            hello: int tuple[2]\n"
"\n"
"        "
)

check(A.func0static.__doc__, "\n"
"        func0static(e, arg2, hello, f=2) -> int\n"
"        func0static(e, arg2, hello) -> int\n"
"        "
)
check(A.func1static.__doc__, "\n"
"        func1static(A e, short arg2, Tuple hello, double f=2) -> int\n"
"        func1static(A e, short arg2, Tuple hello) -> int\n"
"        "
)
check(A.func2static.__doc__,  "\n"
"        func2static(e, arg2, hello, f=2) -> int\n"
"\n"
"        Parameters:\n"
"            e: A *\n"
"            arg2: short\n"
"            hello: int tuple[2]\n"
"            f: double\n"
"\n"
"        func2static(e, arg2, hello) -> int\n"
"\n"
"        Parameters:\n"
"            e: A *\n"
"            arg2: short\n"
"            hello: int tuple[2]\n"
"\n"
"        "
)
check(A.func3static.__doc__,  "\n"
"        func3static(A e, short arg2, Tuple hello, double f=2) -> int\n"
"\n"
"        Parameters:\n"
"            e: A *\n"
"            arg2: short\n"
"            hello: int tuple[2]\n"
"            f: double\n"
"\n"
"        func3static(A e, short arg2, Tuple hello) -> int\n"
"\n"
"        Parameters:\n"
"            e: A *\n"
"            arg2: short\n"
"            hello: int tuple[2]\n"
"\n"
"        "
)

check(A.variable_a.__doc__, "A_variable_a_get(self) -> int")
check(A.variable_b.__doc__, "A_variable_b_get(A self) -> int")
check(A.variable_c.__doc__, "\n"
"A_variable_c_get(self) -> int\n"
"\n"
"Parameters:\n"
"    self: A *\n"
"\n"
)
check(A.variable_d.__doc__, "\n"
"A_variable_d_get(A self) -> int\n"
"\n"
"Parameters:\n"
"    self: A *\n"
"\n"
)

check(B.__doc__, "Proxy of C++ B class")
check(C.__init__.__doc__, "__init__(self, a, b, h) -> C")
check(D.__init__.__doc__, "__init__(D self, int a, int b, Hola h) -> D")
check(E.__init__.__doc__, "\n"
"        __init__(self, a, b, h) -> E\n"
"\n"
"        Parameters:\n"
"            a: special comment for parameter a\n"
"            b: another special comment for parameter b\n"
"            h: enum Hola\n"
"\n"
"        "
)
check(F.__init__.__doc__, "\n"
"        __init__(F self, int a, int b, Hola h) -> F\n"
"\n"
"        Parameters:\n"
"            a: special comment for parameter a\n"
"            b: another special comment for parameter b\n"
"            h: enum Hola\n"
"\n"
"        "
)

check(B.funk.__doc__, "funk(B self, int c, int d) -> int")
check(funk.__doc__, "funk(A e, short arg2, int c, int d) -> int")
check(funkdefaults.__doc__, "\n"
"    funkdefaults(A e, short arg2, int c, int d, double f=2) -> int\n"
"    funkdefaults(A e, short arg2, int c, int d) -> int\n"
"    "
)

check(func_input.__doc__, "func_input(int * INPUT) -> int")
check(func_output.__doc__, "func_output() -> int")
check(func_inout.__doc__, "func_inout(int * INOUT) -> int")
check(banana.__doc__, "banana(S a, S b, int c, Integer d)")
