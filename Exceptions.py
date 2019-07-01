expression=input('введите выражение в формате "действие операнд1 операнд2"')
result=0
assert expression[0] in ['+','-','*','/']
try:
    if expression[0] == '+':
        print(f'результат = {int(expression[1])+int(expression[2])}')
    elif expression[0] == '-':
        print(f'результат = {int(expression[1])-int(expression[2])}')
    elif expression[0] == '*':
        print(f'результат = {int(expression[1])*int(expression[2])}')
    elif expression[0] == '/':
        try:
            print(f'результат = {int(expression[1])/int(expression[2])}')
        except ZeroDivisionError:
            print ('Ошибка деления на ноль')
except IndexError:
    print('введено недостаточное количество операндов')
except ValueError:
    print('неверно введен один из операндов')
finally:
    print('программа завершена')