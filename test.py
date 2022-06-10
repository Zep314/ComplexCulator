# тесты всякие - не для продакшына....


from cmath import exp
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
    while True: # Разбираемся с комплексными числами, у которых есть мнимая часть
        find = False
        for pos_i in range(len(expression)):
            if type(expression[pos_i]) != list and expression[pos_i].find('i') > -1:
                find = True
                break
        if find:
            if pos_i < len(expression) - 1: # полагаем, что может быть скобка
                if expression[pos_i + 1] == ')':
                    # тут уже хоршее число - т.е. вида (2+3i), т.е в виде списка: ['(','2','+','3i',')'] 
                    # выкидываем первый и последний элементы. первый -записываем в новый писок - второй - тоже, но - записываем знак в 3-м элементе
                    complex = []
                    if expression[pos_i-1] == '-':
                        complex = [[expression[pos_i-2],'-'+expression[pos_i].replace('i','')]]
                    else:    
                        complex = [expression[pos_i-2],expression[pos_i].replace('i','')]
                    del expression[pos_i-3:pos_i+2]
                    expression.insert(pos_i-3,complex)
                else:
                    # полагаем, что это только одна мнимая часть комплексного числа
                    if pos_i > 0:
                        if expression[pos_i-1] == '-':
                            expression[pos_i] = ['0','-'+expression[pos_i].replace('i','')]
                        else:
                            expression[pos_i] = ['0',expression[pos_i].replace('i','')]
                    else:
                            expression[pos_i] = ['0',expression[pos_i].replace('i','')]
            else:
                # тут последний элемент в строке - мнимая часть числа, значит просто заменяем последний элемент
                if expression[pos_i-1] == '-':
                    expression[pos_i] = ['0','-'+expression[pos_i].replace('i','')]
                else:
                    expression[pos_i] = ['0',expression[pos_i].replace('i','')]
        else:
            break    
    for i in range(len(expression)):
        if type(expression[i]) != list \
                    and not expression[i] in settings.operators:
            expression[i] = [expression[i],0]
    return expression

expression = ['15i','*','(','1','+','2i',')','+','(','3','+','4i',')','+','8i','-','1','/','2']
# [['1','2'],'+',['3','4'],'+',['8','0']]

print(expression)
print(convert2complex(expression))

