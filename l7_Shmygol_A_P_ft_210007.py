from main import *
import logging

logging.basicConfig(level=logging.INFO, filename="py_log.log", format="%(asctime)s %(levelname)s %(message)s")

while True:
    try:
        k = int(input('введите координату x1/ От 1 до 8'))
        l = int(input('введите координату y1/ От 1 до 8'))
        m = int(input('введите координату x2/ От 1 до 8'))
        n = int(input('введите координату y2/ От 1 до 8'))
        logging.info(f'Значения координат ({k}:{l})({m}:{n})')
        break
    except ValueError:
        print('Вводите число он 1 до 8 !!!!')
        logging.error("ValueError", exc_info=True)

k1 = Kletka(k, l)                                                    # задание 1
k2 = Kletka(m, n)

if (k1.x + k1.y) % 2 == (k2.x + k2.y) % 2:
    print(f'Клетки ({k1.x}:{k1.y}) и ({k2.x}:{k2.y}) одного цвета')
    logging.info(f'{(k1.x + k1.y) % 2}  {(k2.x + k2.y) % 2}')
else:
    print(f'Клетки ({k1.x}:{k1.y}) и ({k2.x}:{k2.y}) разных цветов')
    logging.info(f'{(k1.x + k1.y) % 2}  {(k2.x + k2.y) % 2}')


while True:
    try:
        fig = str(input(f' Какая фигура стоит на поле ({k1.x}:{k1.y})/'
                        f'Ферзь/Ладья/Слон/Конь'))  # задание 2

        c2 = k2.cord
        fig1 = ''
        if fig == 'Ферзь':
            fig1 = Ferz(k, l)
        if fig == 'Ладья':
            fig1 = Ladia(k, l)
        if fig == 'Слон':
            fig1 = Slon(k, l)
        if fig == 'Конь':
            fig1 = Kon(k, l)

        coordinat = fig1.hod()  # создание скиска клеток, на которые может попасть за 1 ход
        logging.info(f'создание списка клеток, на которые может попасть за 1 ход {coordinat}')

        if c2 in coordinat:
            print(f'{fig1.name} угрожает полю {c2}')
        else:
            print(f'{fig1.name} не угрожает полю {c2}')
        break
    except AttributeError:
        logging.error("AttributeError", exc_info=True)
        print('Вводите Ферзь/Ладья/Слон/Конь !!! ')


while True:
    try:
        fig = str(input(f' Какая фигура стоит на поле ({k1.x}:{k1.y})/'
                        f'Ферзь/Ладья/Слон/Конь'))  # задание 3

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
        logging.info(f'создание списка клеток, на которые может попасть за 1 ход {coordinat}')
        o_p = []
        if c2 in coordinat:
            print(f'{fig1.name} может за 1 ход попасть на поле  {c2}')
        else:
            print(f'{fig1.name} не может за 1 ход попасть на поле {c2}')
            coordinat2 = fig2.hod()
            for i in coordinat:
                if i in coordinat2:
                    o_p.append(i)
                    logging.info(f'промежуточные поля  '
                                 f'{o_p}')
            if len(o_p) != 0:
                print(f'Может попасть за 2 хода через поле(поля) {o_p}')
            else:
                print(f'Не может за 2 хода попасть на поле {c2}')
        break
    except AttributeError:
        logging.error("AttributeError", exc_info=True)
        print('Вводите Ферзь/Ладья/Слон/Конь !!! ')


















