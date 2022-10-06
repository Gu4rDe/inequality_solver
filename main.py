from solver import solve_complete_square


print('Выберете тип неравенства')
print('(1) Полное квадратное')
index = int(input('Введите номер: '))

if index == 1:
    a, b, c = map(float, input('Введите коэффиценты: ').split())
    sign_string = input('Введите знак неравенства: ')
    sign = -1 if sign_string == '<' else 1
    print('Ответ:', solve_complete_square(a, b, c, sign))