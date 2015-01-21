#!/usr/bin/env python
#__all__ = ["functionList"]
import math
functionList = {}
#functionList[''] = math.copysign(x, y)
#Return x with the sign of y. On a platform that supports signed zeros, copysign(1.0, -0.0) returns -1.0.
#functionList[''] = math.fmod(x, y)
#functionList[''] = math.ldexp(x, i)
#Return x * (2**i). This is essentially the inverse of function frexp().
functionList['log'] = math.log
#With one argument, return the natural logarithm of x (to base e).
#With two arguments, return the logarithm of x to the given base, calculated as log(x)/log(base).
#functionList[''] = math.pow(x, y)
#Return x raised to the power y. Exceptional cases follow Annex  of the C99 standard as far as possible. In particular, pow(1.0, x) and pow(x, 0.0) always return 1.0, even when x is a zero or a NaN. If both x and y are finite, x is negative, and y is not an integer then pow(x, y) is undefined, and raises ValueError.
#functionList[''] = math.atan2(y, x)
#Return atan(y / x), in radians. The result is between -pi and pi. The vector in the plane from the origin to point (x, y) makes this angle with the positive X axis. The point of atan2() is that the signs of both inputs are known to it, so it can compute the correct quadrant for the angle. For example, atan(1) and atan2(1, 1) are both pi/4, but atan2(-1, -1) is -3*pi/4.
#functionList[''] = math.hypot(x, y)
#Return the Euclidean norm, sqrt(x*x + y*y). This is the length of the vector from the origin to point (x, y).
functionList['factorial'] = math.factorial
functionList['floor'] = math.floor
functionList['abs'] = math.fabs
functionList['ceil'] = math.ceil
functionList['frexp'] = math.frexp
functionList['fsum'] = math.fsum
functionList['isinf'] = math.isinf
functionList['isnan'] = math.isnan
functionList['modf'] = math.modf
functionList['trunc'] = math.trunc
functionList['exp'] = math.exp
functionList['expm1'] = math.expm1
functionList['log1p'] = math.log1p
functionList['log10'] = math.log10
functionList['sqrt'] = math.sqrt
functionList['acos'] = math.acos
functionList['asin'] = math.asin
functionList['atan'] = math.atan
functionList['cos'] = math.cos
functionList['sin'] = math.sin
functionList['tan'] = math.tan
functionList['degrees'] = math.degrees
functionList['radians'] = math.radians
functionList['acosh'] = math.acosh
functionList['asinh'] = math.asinh
functionList['atanh'] = math.atanh
functionList['cosh'] = math.cosh
functionList['sinh'] = math.sinh
functionList['tanh'] = math.tanh
