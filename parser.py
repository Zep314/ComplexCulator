# парсинг строки и обработка ошибок

# обработки ошибок нет - надо сделать!

import settings
from queue import queue_handler

# my_parse оставляем как есть. На вход прилетает '(1+2i)+(3+4i)', на выходе - ['(','1','+','2','i',')','+','(','3','+','4','i',')']
def my_parse(string): # раскалываем строку на операнды, скобки и числа в список
    ret = []
    num = ''
    for char in string:
        if char in '.0123456789i': # - тут добавил, среди валидных символов числа может быть 'i'
            num += char
        elif char in settings.operators or char in '()':
            if len(num)>0: 
                ret.append(num)
                num = ''
            ret.append(char)
    if len(num)>0: ret.append(num)        
    return ret

# тут переделываем в комплексные числа, то, что нам парсер расколол
# на входе такое: ['(','1','+','2i',')','+','(','3','+','4i',')','+','8']
# на выходе должно быть такое: [['1','2'],'+',['3','4'],'+',['8','0']]
def convert2complex(expression):
    

    return expression

def complexculator(text): # потом тут надо все в однострочники завернуть
    #print(f'ComplexCulator in action {text}')
    expression = my_parse(text)
    
    #expression = convert2complex(expression)

    expression = queue_handler(expression)
    
    return str(f'Ответ:  {expression[0]}')
