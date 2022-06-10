# парсинг строки и обработка ошибок
import settings

def my_parse(string): # раскалываем строку на операнды, скобки и числа в список
    ret = []
    num = ''
    for char in string:
        if char in '.0123456789i':
            num += char
        elif char in settings.operators or char in '()':
            if len(num)>0: 
                ret.append(num)
                num = ''
            ret.append(char)
    if len(num)>0: ret.append(num)        
    return ret


def complexculator(text):
    print(f'ComplexCulator in action {text}')
    return my_parse(text)
