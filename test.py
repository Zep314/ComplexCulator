# тесты всякие - не для продакшына....

import settings

def my_parse(string): # раскалываем строку на операнды, скобки и числа в список
    ret = []
    num = ''
    for char in string.lower():
        if char in '.0123456789i': # - тут добавил, среди валидных символов числа может быть 'i'
            num += char
        elif char in settings.operators or char in '()':
            if len(num)>0: 
                ret.append(num)
                num = ''
            ret.append(char)
    if len(num)>0: ret.append(num)        
    return ret

def convert2complex(expression):
    ok = False
    while not ok:
        find = False
        for pos_i in range(len(expression)):
            if expression[pos_i].find('i') > -1:
                find = True
                break
        if find:
            if pos_i < len(expression): # полагаем, что может быть скобка
                if expression[pos_i + 1] == ')':
                    # тут уже хоршее число - т.е. вида (2+3i), т.е в виде списка: ['(','2','+','3i',')'] 
                    # выкидываем первый и последний элементы. первый -записываем в новый писок - второй - тоже, но - записываем знак в 3-м элементе
                    complex = []
                    if expression[pos_i-1] == '-':
                        complex = [[expression[pos_i-2],'-'+expression[pos_i].replace('i','')]]
                    else:    
                        complex = [[expression[pos_i-2],expression[pos_i].replace('i','')]]
                    del expression[pos_i-3:pos_i+1]
                    expression.insert(pos_i-3,complex)
                else:
                    print('Ошибка записи комплесного числа!')
                    exit() # надо доработать - стобы ошибка в интерфейс уходила
            else:
                # тут последний элемент в строке - мнимая часть числа, значит просто заменяем последний элемент
                if expression[pos_i-1] == '-':
                    expression[pos_i] = ['0','-'+expression[pos_i].replace('i','')]
                else:
                    expression[pos_i] = ['0',expression[pos_i].replace('i','')]


    return expression

expression = ['(','1','+','2i',')','+','(','3','+','4i',')','+','8']
# [['1','2'],'+',['3','4'],'+',['8','0']]

print(expression)
print(convert2complex(expression))

