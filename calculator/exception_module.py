#!/usr/bin/env python
#__all__ = ["functionList"]
class Networkerror(RuntimeError):
	def __init__(self, message):
		self.message = message


try:
    raise ValueError, "Bad hostname"
except ValueError,e:
    print e.message
