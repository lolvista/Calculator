import calculator
import sys

c = calculator.Calc(calculator.functionList)

if sys.argv[1] == '-f':
    f = open(sys.argv[2], "r")
    i = 1 
    for line in f:
        try:
            a = c.Evaluate(line.replace(" ", "").strip("\n"))
        except ValueError,e:
            print e.message
        else:
            print a 
        i += 1
    f.close()
else:
    print "no file input!"
