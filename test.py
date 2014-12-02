#!/usr/bin/env python
functionList = ['cos', 'sin'];
tokenTypes = {'DELIMITER' : 1, 'VARIABLE' : 2, 'NUМВЕR' : 3}


# Точка входа анализатора
def eval_exp():
    print 'eval_exp'
    global token
    global tok_type
    answer = 0
    get_token()
    if token == '':
        serror(2)
        return
    else:
        answer = eval_exp2(answer);
    #if token != '':
       #serror(0)  # последней лексемой должен быть нуль
       #print 'exp error'
    return float(answer);

# Сложение или вычитание двух слагаемых
def eval_exp2(answer):
    print 'eval_exp2'
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
            print 'Answer 2= ', answer
        elif op == '+':
            answer += temp
            print 'Answer = ', answer
        op = token
    return float(answer)

# Умножение или деление двух множителей
def eval_exp3(answer):
    print 'eval_exp3'
    global token
    global tok_type
    
    temp = 0

    answer = eval_exp4(answer)
    op = token
    while op == '*' or op == '/' or op == '%':
        get_token()
        temp = eval_exp4(temp)
        if op == '*':
            answer = answer * temp
            print 'Answer 1 = ', answer
        elif op == '/':
            if temp == 0.0:
                serror(3) # деление на нуль
                answer = 0.0
                print 'Answer = ', answer
            else:
                answer = answer /temp
                print 'Answer = ', answer
        elif op == '%':
            answer = int(answer) % int(temp)
            print 'Answer = ', answer
        op = token
    return float(answer)

# Возведение в степень 
def eval_exp4(answer):
    print 'eval_exp4'
    global token
    global tok_type
    temp = 0.0
    ex = 0.0

    answer = eval_exp5(answer)

    if token == '^':
        get_token()
        temp = eval_exp4(temp)
        ex = answer
        if temp == 0.0:
            answer = 1.0
            print 'Answer = ', answer
            return
       #for i in range(0, temp - 1):
           #answer = answer * ex;
    return float(answer)
    
# Умножение унарных операторов + и -
def eval_exp5(answer):
    print 'eval_exp5'
    global token
    global tok_type
    op = 0
    if tok_type == 'DELIMITER' and token == '+' or token == '-':
        op = token
        get_token()
    answer = eval_exp6(answer)
    if op == '-':
        answer = - answer
        print 'Answer = ', answer
    return float(answer)

# Вычисление выражения в скобках
def eval_exp6(answer):
    print 'eval_exp6'
    global token
    global tok_type
    if token == '(':
        get_token()
        answer = eval_exp2(answer)
        if token != ')':
            serror(1)
        get_token()
    else:
        answer = atom(answer);
    return float(answer)

# Получение значения в скобках
def atom(answer):
    print 'atom'
    global token
    global tok_type
    if tok_type == 'NUMBER':
        answer = float(token)
        print 'Answer = ', answer
        get_token()
        return float(answer)
    serror(0)  # иначе синтаксическая ошибка в выражении
    print 'atom error'
    return float(answer)
    
# Отображение сообщения об ошибке
def serror(error):
    e = ['Синтаксическая ошибка', 'Несбалансированные скобки', 'Нет выражения', 'Деление на нуль']
    print e[error]
    return

# Возврат очередной лексемы
def get_token():
    global token
    global tok_type
    global prog
    global i
    tok_type = 0

    if prog == '':
        print 'конец выражения'
        return False# конец выражения
    
    if prog in ('+','-','*','/','%','^','=','(',')'):
        tok_type = 'DELIMITER'
        token = prog
        i += 1
        if i < j:
            prog = Input[i]
    elif prog >= 'a' and prog <= 'z':
        while not isdelim(prog):
            token = prog
            i += 1
            if i < j:
                prog = Input[i]
            else:
                prog = ''
        tok_type = 'VARIABLE'
    elif prog >= '0' and prog <= '9':
        token = ''
        while not isdelim(prog):
            token += prog
            if i < j - 1:
                i += 1
                prog = Input[i]
            else:
                prog = ''
        tok_type = 'NUMBER'
    print 'token = ', token, ', type = ', tok_type
    return True

# Возвращение значения ИСТИНА, если с является разделителем
def isdelim(c):
    if c in ('+','-','*','/','%','^','=','(',')') or c == '\0' or c == '':
        return True
    return False

# Проверка входнойстроки
def spellcheck(str):
    while get_token() == True:
        if tok_type == 'DELIMITER':
            break;
        elif tok_type == 'VARIABLE':
            break;
        elif tok_type == 'NUMBER':
            break;
        else:
            print 'token error'
    return True;

var = True
while var == True:
    Input = raw_input("Input string (type 'exit' to quit):");
    if Input == 'exit':
        var = False;
        break;
    if spellcheck(Input) == True:
        token = ''
        tok_type = 0
        i = 0
        j = len(Input)
        prog = Input[i]
        ans = eval_exp()
        print Input, ' = ', ans
    else:
        print 'spellcheck error!'
    
