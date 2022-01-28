counter = 0
functions = {}
verbose_level = 1 # 0 - no debugging, 1 - short, 2 - stack trace


def debugger(name, debug=False):
    _STR = lambda *x: ", ".join([functions[arg] if arg in functions else str(arg) for arg in x])
    def _PRN(x):
        global counter
        counter += 1
        print(f"{counter}:", x)

    def wrapper(f):
        def func(*args, **kwargs):
            global counter
            local = counter + 1
            function_counter = [i for i, k_v in enumerate(functions.values()) if k_v == name]
            prefix = f"{function_counter} " if verbose_level == 2 else ''
            _PRN(f"{prefix}{name} ({_STR(*args)})") if verbose_level > 0 and debug else ()
            res = f(*args, **kwargs)
            _PRN(f"{local}: {res}") if verbose_level == 2 and debug else ()
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

LST= lambda *x: tuple(x)
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
# ACC = debugger("ACC", debug=True)(ACC)

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
