counter = 0
functions = {}


def debugger(name, debug=False):
    _STR = lambda *x: ", ".join([functions[arg] if arg in functions else str(arg) for arg in x])

    def wrapper(f):
        def func(*args, **kwargs):
            global counter
            local = counter + 1
            PRN(f"{name} ({_STR(*args)})") if debug else ()
            res = f(*args, **kwargs)
            PRN(f"{local}: {res}") if debug else ()
            return res
        functions[func] = name
        return func

    return wrapper


def PRN(x):
    global counter
    counter += 1
    print(f"{counter}:", x)


CAR = lambda x: x[0] if x else []
CDR = lambda x: x[1:]

LST = lambda *x: tuple(x)
LEN = lambda *x: len(x)
SUM = lambda *x: sum(*x)
FLT = lambda *x: LST(*FLT(CAR(x)), *FLT(*CDR(x))) if CDR(x) else CAR(x)
STR = lambda *x: ", ".join([functions[arg] if arg in functions else str(arg) for arg in x])
CAL = lambda f, *x: f(x)
# ACC = lambda x, f: f(LST(CAR(x), ACC(CDR(x), f))) if CDR(x) else CAR(x)

CAR = debugger("CAR", debug=True)(CAR)
CDR = debugger("CDR", debug=True)(CDR)

LST = debugger("LST", debug=True)(LST)
LEN = debugger("LEN", debug=True)(LEN)
SUM = debugger("SUM", debug=True)(SUM)
FLT = debugger("FLT", debug=True)(FLT)
STR = debugger("STR", debug=True)(STR)
CAL = debugger("CAL", debug=True)(CAL)
# ACC = debugger("ACC", debug=False)(ACC)

a = (1, 2, 3)
b = LST(4, 5, 6)
c = (7, 8)
d = (9,)

PRN(a)
PRN(CAR(a))
PRN(CDR(a))
PRN(LEN(a))
PRN(SUM(a))
PRN(LST(1, 2, 3))
PRN(CAR(b))
PRN(CAR(LST(CAR(b))))
PRN(FLT(a, b, c, d))
PRN(CAL(STR, a, b, c, d))
