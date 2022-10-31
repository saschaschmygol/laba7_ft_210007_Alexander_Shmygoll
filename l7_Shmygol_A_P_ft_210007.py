from main import *
while True:
    try:
        k = int(input('введите координату x1/ От 1 до 8'))
        l = int(input('введите координату y1/ От 1 до 8'))
        m = int(input('введите координату x2/ От 1 до 8'))
        n = int(input('введите координату y2/ От 1 до 8'))
        break
    except ValueError:
        print('Вводите число он 1 до 8 !!!!')

k1 = Kletka(k, l)
k2 = Kletka(m, n)

if (k1.x + k1.y) % 2 == (k2.x + k2.y) % 2:
    print(f'Клетки ({k1.x}:{k1.y}) и ({k2.x}:{k2.y}) одного цвета')
else:
    print(f'Клетки ({k1.x}:{k1.y}) и ({k2.x}:{k2.y}) разных цветов')


#
# fig = str(input(f' Какая фигура стоит на поле ({k1.x}:{k1.y})/'
#                 f'Ферзь/Ладья/Слон/Конь'))                              # задание2
#
# c2 = k2.cord
# fig1 = ''
# if fig == 'Ферзь':
#     fig1 = Ferz(k, l)
# if fig == 'Ладья':
#     fig1 = Ladia(k, l)
# if fig == 'Слон':
#     fig1 = Slon(k, l)
# if fig == 'Конь':
#     fig1 = Kon(k, l)
#
# coordinat = fig1.hod()
#
# if c2 in coordinat:
#     print(f'{fig1.name} угрожает полю {c2}')
# else:
#     print(f'{fig1.name} не угрожает полю {c2}')
#

fig = str(input(f' Какая фигура стоит на поле ({k1.x}:{k1.y})/'
                f'Ферзь/Ладья/Слон/Конь'))                              # задание2

c2 = k2.cord
fig1 = ''
fig2 = ''
if fig == 'Ферзь':
    fig1 = Ferz(k, l)
    fig2 = Ferz(m, n)
if fig == 'Ладья':
    fig1 = Ladia(k, l)
    fig2 = Ladia(m, n)
if fig == 'Слон':
    fig1 = Slon(k, l)
    fig2 = Slon(m, n)
if fig == 'Конь':
    fig1 = Kon(k, l)
    fig2 = Kon(m, n)

coordinat = fig1.hod()
o_p = []
if c2 in coordinat:
    print(f'{fig1.name} может за 1 ход попасть на поле  {c2}')
else:
    print(f'{fig1.name} не может за 1 ход попасть на поле {c2}')
    coordinat2 = fig2.hod()
    for i in coordinat:
        if i in coordinat2:
            o_p.append(i)
    if len(o_p) != 0:
        print(f'Может попасть за 2 хода через поле(поля) {o_p}')
    else:
        print(f'Не может за 2 хода попасть на поле {c2}')

























