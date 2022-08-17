import ctypes
import pathlib

libname = pathlib.Path().absolute() / "num_multi.so"
print(libname)
c_lib = ctypes.cdll.LoadLibrary(libname)

x, y = 3, 1.2
c_lib.mult.restype = ctypes.c_float
answer = c_lib.mult(x,ctypes.c_float(y))
print(f"    In Python: int: {x} float {y} return val {answer}")