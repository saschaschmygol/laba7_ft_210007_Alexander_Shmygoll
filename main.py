
class Kletka:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)
        self.cord = (x, y)


class Ferz():
    def __init__(self, x, y):
        self.coord = Kletka(x, y)
        self.name = 'Ферзь'

    def hod(self):
        x = int(self.coord.x)
        y = int(self.coord.y)
        moves_x = [x]
        moves_y = [y]
        while x <= 7 and x != 8:
            x += 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        while x > 0 and x != 1:
            x -= 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        while y <= 7 and y != 8:
            y += 1
            moves_x.append(x)
            moves_y.append(y)
        y = int(self.coord.y)
        while y > 0 and y != 1:
            y -= 1
            moves_x.append(x)
            moves_y.append(y)
        y = int(self.coord.y)

        while x != 8 and y != 8 :                                          # по диагонали
            x += 1
            y += 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        y = int(self.coord.y)

        while y != 1 and x != 8 :
            x += 1
            y -= 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        y = int(self.coord.y)

        while y != 8 and x != 1:
            x -= 1
            y += 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        y = int(self.coord.y)

        while y != 1 and x != 1:
            x -= 1
            y -= 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        y = int(self.coord.y)
        coord = list(zip(moves_x, moves_y))
        return coord

# aa = Ferz(p1, p2)
# t, z = aa.hod()
# print(t, z)

class Ladia():
    def __init__(self, x, y):
        self.coord = Kletka(x, y)
        self.name = 'Ладья'

    def hod(self):
        x = int(self.coord.x)
        y = int(self.coord.y)
        moves_x = [x]
        moves_y = [y]
        while x <= 7 and x != 8:
            x += 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        while x > 0 and x != 1:
            x -= 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        y = int(self.coord.y)
        while y <= 7 and y != 8:
            y += 1
            moves_x.append(x)
            moves_y.append(y)
        y = int(self.coord.y)
        while y > 0 and y != 1:
            y -= 1
            moves_x.append(x)
            moves_y.append(y)
        coord = list(zip(moves_x, moves_y))
        return coord

# aa = Ladia(p1, p2)
# t, z = aa.hod()
# print(t, z)

class Slon():
    def __init__(self, x, y):
        self.coord = Kletka(x, y)
        self.name = 'Слон'

    def hod(self):
        x = int(self.coord.x)
        y = int(self.coord.y)
        moves_x = [x]
        moves_y = [y]

        while x != 8 and y != 8 :
            x += 1
            y += 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        y = int(self.coord.y)

        while y != 1 and x != 8 :
            x += 1
            y -= 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        y = int(self.coord.y)

        while y != 8 and x != 1:
            x -= 1
            y += 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        y = int(self.coord.y)

        while y != 1 and x != 1:
            x -= 1
            y -= 1
            moves_x.append(x)
            moves_y.append(y)
        x = int(self.coord.x)
        y = int(self.coord.y)
        coord = list(zip(moves_x, moves_y))
        return coord

# aa = Slon(p1, p2)
# t1, t2 = aa.hod()
# print(t1, t2)

class Kon():
    def __init__(self, x, y):
        self.coord = Kletka(x, y)
        self.name = 'Конь'

    def hod(self):
        x = int(self.coord.x)
        y = int(self.coord.y)
        moves_x = [x]
        moves_y = [y]

        if y != 7 and y != 8 and x != 8:
            x += 1
            y += 2
            moves_x.append(x)
            moves_y.append(y)
            x = int(self.coord.x)
            y = int(self.coord.y)
        if y != 8 and x != 7 and x != 8:
            x += 2
            y += 1
            moves_x.append(x)
            moves_y.append(y)
            x = int(self.coord.x)
            y = int(self.coord.y)
        if y != 1 and x != 7 and x != 8:
            x += 2
            y -= 1
            moves_x.append(x)
            moves_y.append(y)
            x = int(self.coord.x)
            y = int(self.coord.y)
        if y != 1 and y != 2 and x != 8:
            x += 1
            y -= 2
            moves_x.append(x)
            moves_y.append(y)
            x = int(self.coord.x)
            y = int(self.coord.y)
        if y != 1 and y != 2 and x != 1:
            x -= 1
            y -= 2
            moves_x.append(x)
            moves_y.append(y)
            x = int(self.coord.x)
            y = int(self.coord.y)
        if x != 1 and x != 2 and y != 1:
            x -= 2
            y -= 1
            moves_x.append(x)
            moves_y.append(y)
            x = int(self.coord.x)
            y = int(self.coord.y)
        if x != 1 and x != 2 and y != 8:
            x -= 2
            y += 1
            moves_x.append(x)
            moves_y.append(y)
            x = int(self.coord.x)
            y = int(self.coord.y)
        if x != 1 and y != 7 and y != 8:
            x -= 1
            y += 2
            moves_x.append(x)
            moves_y.append(y)
            x = int(self.coord.x)
            y = int(self.coord.y)
        coord = list(zip(moves_x, moves_y))
        return coord

# aa = Kon(p1, p2)
# t1, t2 = aa.hod()
# print(t1, t2)
































