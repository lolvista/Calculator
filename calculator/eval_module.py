#!/usr/bin/env python
import math

class Calc:
    'Base class for calculating everything'

    __functionList = {}

    __constantList = {}
    __constantList['e'] = math.e
    __constantList['pi'] = math.pi

    __variableList = {}

    token = ''
    tok_type = 0
    i = 0
    j = 0
    prog = ''
    input = ''

    def __init__(self, function_list):
        self.__functionList = function_list;

    def Evaluate(self, str):
        'Evaluate the expression'
        global token
        global tok_type
        global i
        global j
        global prog
        global input

        token = ''
        tok_type = 0
        i = 0
        j = len(str)
        prog = str[i]
        input = str;

        def eval_exp():
            'Enter point'
            global token
            answer = 0
            
            get_token()
            if token == '':
                raise ValueError, "Bad token"
                return 0.0
            else:
                answer = eval_exp2(answer);
            return float(answer);

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
            global i
            global prog
            temp = 0

            answer = eval_exp4(answer)

            if token == '(':
                token = '*'
                i -= 1
                prog = '('

            op = token
            while op == '*' or op == '/' or op == '%' or op == '//':
                get_token()
                temp = eval_exp4(temp)
                if op == '*':
                    answer = answer * temp
                elif op == '/':
                    if temp == 0.0:
                        raise ValueError, "Divide by zero" 
                        answer = 0.0
                    else:
                        answer = answer /temp 
                elif op == '//':
                    if temp == 0.0:
                        raise ValueError, "Divide by zero" 
                        answer = 0.0
                    else:
                        answer = int(answer/temp)         
                elif op == '%':
                    answer = int(answer) % int(temp)
                op = token
            return float(answer)

        def eval_exp4(answer):
            'unar operators'
            global token
            global tok_type
            op = 0

            if tok_type == 'DELIMITER' and token == '+' or token == '-':
                op = token
                get_token()
            answer = eval_exp5(answer)
            if op == '-':
                answer = - answer
            return float(answer)

        def eval_exp5(answer):
            'pow'
            global token
            global tok_type
            temp = 0.0
            ex = 0.0

            answer = eval_expfun(answer)

            if token == '^':
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
            elif tok_type == 'VARIABLE':
                answer = self.__variableList[token];
                get_token();
                return answer
            else:
                answer = eval_exp6(answer);

            return float(answer)
          
        def eval_exp6(answer):
            'brackets function'
            global token
            global tok_type

            if token == '(':
                get_token()
                answer = eval_exp2(answer)
                if token != ')':
                    raise ValueError, "Unbalanced brackets" 
                get_token()
            else:
                answer = atom(answer);
            return float(answer)

        def atom(answer):
            'value'
            global token
            global tok_type

            if tok_type == 'NUMBER':
                answer = float(token)
                get_token()
                return float(answer)
            raise ValueError, "Syntax error" 
            return float(answer)

        def get_token():
            'Extract the token from the input string'
            global prog
            global token
            global tok_type
            global i
            global j
            tok_type = 0

            if prog == '':
                return False
            
            if isdelim(prog):
                tok_type = 'DELIMITER'
                token = prog
                i += 1
                if token == '/' and input[i] == '/':
                    token += input[i]
                    i += 1
                elif token == '*' and input[i] == '*':
                    token = '^'
                    i += 1
              
                if i < j:
                    prog = input[i]
                else:
                    prog = ''
                    return False
            elif issumbol(prog):
                token = '';
                while not isdelim(prog) and (issumbol(prog) or isnumber(prog)):
                    token += prog;
                    i += 1;
                    if i < j:
                        prog = input[i]
                    else:
                        prog = ''
                if token in self.__functionList.keys():
                    tok_type = 'FUNCTION'
                elif token in self.__constantList.keys():
                    tok_type = 'CONSTANT'
                elif token in self.__variableList.keys():
                    tok_type = 'VARIABLE'
                else:
                    raise ValueError, "Unknown expression" 
            elif isnumber(prog):
                token = ''
                while not isdelim(prog):
                    if prog == '.':
                        token = '0'
                    token += prog
                    if i < j - 1:
                        i += 1
                        prog = input[i]
                    else:
                        prog = ''
                tok_type = 'NUMBER'
            else:
              raise ValueError, "Unknown token" 
              token = ''
              return False
            return True

        def isdelim(c):
            'true if token is delimiter'
            if c in ('+','-','*','/','%','^','=','(',')') or c == '' or c == '\n' or c == 'EOF' or c == '':
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