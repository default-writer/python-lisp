# GLOBALS
counter = 0
functions = {}
verbose_level = 0  # 0 - no debugging, 1 - short, 2 - stack trace


# DEBUGGER
def debugger(name, debug=False):
    _FMT = lambda *x:  f"'{x}'" if type(x) is str else str(*x)
    _STR = lambda *x: ", ".join([functions[arg] if arg in functions else _FMT(arg) for arg in x])

    def _PRN(x):
        global counter
        counter += 1
        print(f"{counter}:", x)

    def wrapper(f):
        def func(*args, **kwargs):
            global counter
            local = counter + 1
            prefix = f"{[i for i, k_v in enumerate(functions.values()) if k_v == name]} " if verbose_level == 2 else ''
            _PRN(f"{prefix}{name} ({_STR(*args)})") if verbose_level > 0 and debug else ()
            res = f(*args, **kwargs)
            res = res if res else ""
            _PRN(f"{local}: {res}") if verbose_level == 2 and debug else ()
            return res

        functions[func] = name
        return func

    return wrapper


# PRN FUNCTION
def PRN(*x):
    global counter
    counter += 1
    print(f"{counter}:", *LST(*x))
    return x


# LISt Programming FUNCTIONS
CAR = lambda *x: x[0] if x else ()
CDR = lambda *x: x[1:]
LST = lambda *x: tuple(x)
LEN = lambda *x: len(*x)
SUM = lambda *x: sum(*x)
CON = lambda *x: LST(*CON(CAR(*x)), *CON(*CDR(*x))) if CDR(*x) else CAR(*x)
DUP = lambda *x: LST(*x)
CAL = lambda f, *x: f(*x)
EVL = lambda f, *x: LST(*EVL(f, CAR(*x)), *EVL(f, *CDR(*x))) if CDR(*x) else f(x)


# DEBUGGER SETTINGS
CAR = debugger("CAR", debug=True)(CAR)
CDR = debugger("CDR", debug=True)(CDR)
LST = debugger("LST", debug=True)(LST)
LEN = debugger("LEN", debug=True)(LEN)
SUM = debugger("SUM", debug=True)(SUM)
CON = debugger("CON", debug=True)(CON)
DUP = debugger("DUP", debug=True)(DUP)
CAL = debugger("CAL", debug=True)(CAL)
EVL = debugger("EVL", debug=True)(EVL)


# TEST DATA
a = (1, 2, 3)
b = LST(4, 5, 6)
c = (7, 8)
d = (9,)


# TEST FUNCTION CALLS
PRN(CON((1,), a))  # 1
PRN(a)  # 2
PRN(f"{CAR(a)}-{CDR(a)}")  # 3
PRN(CDR(a,4))  # 4
PRN(CAR(*a))  # 5
PRN(LEN(a))  # 6
PRN(SUM(a))  # 7
PRN(LST(1, 2, 3))  # 8
PRN(CAR(b))  # 9
PRN(CAR(LST(CAR(b))))  # 10
PRN(CON((1,), a, b, c, d))  # 11
CAL(PRN, "Hello, world!")  # 12
PRN(LST("Hello, world!"))  # 13
PRN("Hello, world!")  # 14
PRN(1, 2, 3)  # 15
CAL(PRN, 11, 12, 13)  # 16
PRN(CAL(CON, (1,), (2,), (3, 4)))  # 17
PRN(CON((1, 2, 3), (2,), (1,), (3, 4)))  # 18
PRN(EVL(CON, (1, 2, 3), (2,), (1,), (3, 4)))  # 19
PRN(CON(((1,),), (2,), (3, 4)))  # 20
PRN(DUP(a))  # 21
PRN(EVL(DUP, *CON((1, 2, 3), (2,), (1,), (3, 4))))  # 22
PRN(CON(1))  # 23
PRN(CAR((((1,),),)))  # 24
