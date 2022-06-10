# Модуль интерфейса
from parser import complexculator
from log import add2log
def init():
    print('Программа - калькулятор')
    print('Умеет работать с комплексными числами')
    print('Напишите /help в коммандной строке, чтобы понять, как работать')
    
def _help():
    print('Какая то помощь...')

def _info():
    print('Какая то инфа...')

def interface():
    add2log('Начало работы','<')

    while True:
        inp = input('>>>')
        add2log(inp,'>')
        match inp.lower():
            case '/help': _help()
            case '/info': _info()
            case '/exit': 
                break
            case '/quit': 
                break
            case _ : 
                res = complexculator(inp)
                print(res)
                add2log(res,'<')

    print('Завершение работы')
    add2log('Завершение работы','<')
