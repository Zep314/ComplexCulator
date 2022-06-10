# простой вычислитель занчений +-*/ для комплексных чисел

# сейчас сделано для простых чисел. На вход приходит такое: ['1','+','3'] в результате - '4'

# надо чтобы было на входе: [['2','3'],'+',['4','5']] - на выходе - [['6','8']]

def solver2operand(expression): # тут ждем 3 элемента в списке, из которых первый и последний - числа,
                                # а средний - операнд (просто операция над 2-мя числами)
    match expression[1]:
    #     case '+': return str(float(expression[0]) + float(expression[2]))
    #     case '-': return str(float(expression[0]) - float(expression[2]))
    #     case '*': return str(float(expression[0]) * float(expression[2]))
    #     case '/': return str(float(expression[0]) / float(expression[2]))
    #     case _  : 
    #         print('Ошибка в выражении (1)')
    #         exit()

        case '+': return [float(expression[0][0]) + float(expression[2][0]),float(expression[0][1]) + float(expression[2][1])]
        case '-': return [float(expression[0][0]) - float(expression[2][0]),float(expression[0][1]) - float(expression[2][1])]
        case '*': return [float(expression[0][0]) * float(expression[2][0]) - float(expression[0][1]) * float(expression[2][1]), \
                          float(expression[0][1]) * float(expression[2][0]) + float(expression[0][0]) * float(expression[2][1])]
        case '/': return [(float(expression[0][0]) * float(expression[2][0]) + float(expression[0][1]) * float(expression[2][1])) / \
                          (float(expression[2][0])**2 + float(expression[2][1])**2), 
                          (float(expression[0][1]) * float(expression[2][0]) - float(expression[0][0]) * float(expression[2][1])) / \
                          (float(expression[2][0])**2 + float(expression[2][1])**2)]
        case _  : 
            print('Ошибка в выражении (1)')
            exit()
