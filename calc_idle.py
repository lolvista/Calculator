import calculator
import sys

c = calculator.Calc(calculator.functionList)

f = open("m.txt", "r")
i = 1 
for line in f:
    try:
        a = c.Evaluate(line.replace(" ", "").strip("\n"))
    except ValueError,e:
        print e.message
    else:
        print 'output : ', a 
    i += 1
f.close()