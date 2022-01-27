counter = 0


def debugger(name, debug=False):
    def wrapper(f):
        def func(*args, **kwargs):
            global counter
            local = counter + 1
            if debug:
                PRN(f"{name} {args}")
            res = f(*args, **kwargs)
            if debug:
                PRN(f"{local}: {res}")
            return res

        return func

    return wrapper


def PRN(*args, **kwargs):
    global counter
    counter += 1
    print(f"{counter}:", *args, **kwargs)


LST = lambda *x: x
CAR = lambda x: x[0] if x else []
CDR = lambda x: x[1:]
LEN = lambda x: 1 + LEN(CDR(x)) if x else 0
ACC = lambda x, f: f(LST(CAR(x), ACC(CDR(x), f))) if CDR(x) else CAR(x)
SUM = lambda x: ACC(x, sum)
FLT = lambda *x: LST(*FLT(CAR(x)), *FLT(*CDR(x))) if CDR(x) else CAR(x)

LST = debugger("LST", debug=False)(LST)
CAR = debugger("CAR", debug=True)(CAR)
CDR = debugger("CDR", debug=True)(CDR)
LEN = debugger("LEN", debug=True)(LEN)
ACC = debugger("ACC", debug=True)(ACC)
SUM = debugger("SUM", debug=True)(SUM)
FLT = debugger("FLT", debug=True)(FLT)

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
