#!/usr/bin/env python
import math

class Calc:
    'Base class for calculating everything'

    __functionList = {}

    __constantList = {}
    __constantList['e'] = math.e
    __constantList['pi'] = math.pi

    token = ''
    tok_type = 0
    cur_pos = 0
    exp_lenght = 0
    prog = ''


    def __init__(self, function_list):
        'Pass function list into class'
        self.__functionList = function_list;

    def Evaluate(self, expression):
        'Evaluate the expression'
        global token
        global tok_type
        global cur_pos
        global exp_lenght
        global prog

        token = ''
        tok_type = 0
        cur_pos = 0
        exp_lenght = len(expression)
        prog = expression[0]

        def eval_exp():
            'Enter point'
            global token

            answer = 0
            
            get_token()
            if token == '':
                err = "Bad token : " + token
                raise ValueError, err
                return 0.0
            else:
                answer = eval_expb1(answer);
            return float(answer);

        def eval_expb1(answer):
            '^ |'
            global token
            global tok_type

            temp = 0
            
            answer = eval_expb2(answer);
            op = token
            while op == '^' or op == '|':
                get_token()
                temp = eval_expb2(temp)
                if (float(answer)).is_integer() and (float(temp)).is_integer():
                    if op == '^':
                        answer = bin(int(answer)^int(temp))
                    elif op == '|':
                        answer = bin(int(answer)|int(temp))
                else:
                    err = "Can't do with float: " + str(answer) + ', ' + str(temp) 
                    raise ValueError, err
                op = token
            return float(answer)

        def eval_expb2(answer):
            '&'
            global token
            global tok_type
            global cur_pos
            global prog

            temp = 0
            
            answer = eval_expb3(answer)

            op = token
            while op == '&':
                get_token()
                temp = eval_expb3(temp)
                if (float(answer)).is_integer() and (float(temp)).is_integer():
                    answer = bin(int(answer)&int(temp))
                else:
                    err = "Can't do with float: " + str(answer) + ', ' + str(temp) 
                    raise ValueError, err
                op = token
            return float(answer) 

        def eval_expb3(answer):
            '<< >>'
            global token
            global tok_type

            temp = 0
            
            answer = eval_exp2(answer);
            op = token
            while op == '>>' or op == '<<':
                get_token()
                temp = eval_exp2(temp)
                if (float(answer)).is_integer() and (float(temp)).is_integer():
                    if op == '<<':
                        answer = temp
                    elif op == '>>':
                        answer = temp
                else:
                    err = "Can't do with float: " + str(answer) + ', ' + str(temp) 
                    raise ValueError, err
                op = token
            return float(answer)

        def eval_exp2(answer):
            'Summ'
            global token
            global tok_type

            temp = 0
            
            answer = eval_exp3(answer);
            op = token
            while op == '+' or op == '-':
                get_token()
                temp = eval_exp3(temp)
                if op == '-':
                    answer -= temp
                elif op == '+':
                    answer += temp
                op = token
            return float(answer)

        def eval_exp3(answer):
            'Multi'
            global token
            global tok_type
            global cur_pos
            global prog

            temp = 0
            correct = False

            answer = eval_exp4(answer)

            if token == '(' or tok_type == 'FUNCTION' or tok_type == 'CONSTANT' or tok_type == 'NUMBER':
                op = '*'
                correct = True
            else :
                op = token

            while op == '*' or op == '/' or op == '%' or op == '//':
                if correct == False:
                    get_token()
                else :
                    correct = False

                temp = eval_exp4(temp)
                if op == '*':
                    answer = answer * temp
                elif op == '/':
                    if temp == 0.0:
                        err = "Divide by zero"
                        raise ValueError, err
                        answer = 0.0
                    else:
                        answer = answer /temp 
                elif op == '//':
                    if temp == 0.0:
                        err = "Divide by zero"
                        raise ValueError, err
                        answer = 0.0 
                    else:
                        answer = int(answer/temp)
                elif op == '%':
                    answer = int(answer) % int(temp)

                if token == '(' or tok_type == 'FUNCTION' or tok_type == 'CONSTANT' or tok_type == 'NUMBER':
                    op = '*'
                    correct = True
                else :
                    op = token
            return float(answer)

        def eval_exp4(answer):
            'unar operators and ~'
            global token
            global tok_type

            op = ''

            if token == '+' or token == '-':
                op = token
                get_token()

            answer = eval_exp5(answer)
            if op == '-':
                answer = -answer
            return float(answer)

        def eval_exp5(answer):
            'pow'
            global token
            global tok_type

            temp = 0.0
            ex = 0.0

            answer = eval_expfun(answer)

            if token == '**':
                get_token()
                temp = eval_exp4(temp)
                ex = answer
                if temp == 0.0:
                    answer = 1.0
                else:
                    answer = math.pow(ex, temp);
            return float(answer)
          
        def eval_expfun(answer):
            'function, variable and constant'
            global token
            global tok_type

            if tok_type == 'FUNCTION':
                temp = token
                get_token();
                answer = eval_exp6(answer);
                answer = self.__functionList.get(temp)(answer);
            elif tok_type == 'CONSTANT':
                answer = self.__constantList[token];
                get_token();
                return answer
            else:
                answer = eval_exp6(answer);

            return float(answer)
          
        def eval_exp6(answer):
            'brackets function'
            global token
            global tok_type
            
            temp = 0

            if token == '(':
                get_token()
                answer = eval_exp2(answer)
                if token != ')':
                    err = "Unbalanced brackets"
                    raise ValueError, err
                get_token()
            else:
                answer = atom(answer);
            return float(answer)

        def atom(answer):
            'value'
            global token
            global tok_type

            if tok_type == 'NUMBER':
                try:
                    answer = float(token)
                except ValueError,e:
                    print e.message
                else:
                    get_token()
                    return float(answer)
            else :
                err = "Syntax error : " + token
                raise ValueError, err

        def get_token():
            'Extract the token from the input string'
            global token
            global tok_type
            global cur_pos
            global exp_lenght
            global prog

            if prog == '':
                tok_type = ''
                return False
            
            if isdelim(prog):
                tok_type = 'DELIMITER'
                token = prog
                if cur_pos < exp_lenght - 1:
                    cur_pos += 1
                    prog = expression[cur_pos]
                elif token != ')':
                    err = "Syntax error : " + token
                    raise ValueError, err
                    return False

                if token == prog:
                    cur_pos += 1
                    if token == '/':
                        token = '//'
                    elif token == '*':
                        token = '**'
                    elif token == '-':
                        token = '+'    
                    elif token == '>':
                        token = '>>'
                    elif token == '<':
                        token = '<<'
                if token == ':':
                    token = '/'
                if cur_pos < exp_lenght:
                    prog = expression[cur_pos]
                else:
                    prog = ''
            elif issumbol(prog):
                token = ''
                while not isdelim(prog) and (issumbol(prog) or isnumber(prog)):
                    token += prog
                    cur_pos += 1
                    if cur_pos < exp_lenght:
                        prog = expression[cur_pos]
                    else:
                        prog = ''
                if token in self.__functionList.keys():
                    tok_type = 'FUNCTION'
                elif token in self.__constantList.keys():
                    tok_type = 'CONSTANT'
                else:
                    err = "Unknown expression : " + token
                    raise ValueError, err
            elif isnumber(prog):
                token = ''
                dot = False
                if prog == '.':
                    dot = True
                    token = '0.'
                    cur_pos += 1
                    prog = expression[cur_pos]
                while not isdelim(prog) and not issumbol(prog):
                    if dot == True and prog == '.':
                        raise ValueError, "Multiple dot"
                    if prog == '.':
                        dot = True
                    token += prog
                    if cur_pos < exp_lenght - 1:
                        cur_pos += 1
                        prog = expression[cur_pos]
                    else:
                        prog = ''
                tok_type = 'NUMBER'
            else:
                err = "Unknown expression : " + token
                raise ValueError, err
                token = ''
                return False
            return True

        def isdelim(c):
            'true if token is delimiter'
            if c in ('>','<','|','&','~','+','-','*','/','%','^',':','=','(',')','\n','EOF',''):
                return True
            return False

        def isnumber(c):
            'true if token is number'
            if c >= '0' and c <= '9' or c == '.':
                return True
            return False
          
        def issumbol(c):
            'true if token is sumbol'
            if c >= 'a' and c <= 'z':
                return True
            return False

        ans = eval_exp()
        return ans;
