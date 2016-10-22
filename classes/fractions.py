class VerySimpleFraction(object):
    """ Класс для представления обыкновенных дробей (первая версия) """

    def __init__(self, n, d):
        # data attribute
        # по соглашению о наименовании - private
        self.__num = n
        self.__den = d
        self.reduce()

    # финализатор  (вызывается при сборке мусора)    
    def __del__(self):
        print('deleted')

    def set_num(self, n):
        self.__num = n

    def get_num(self):
        return self.__num

    def set_den(self, d):
        self.__den = d

    def get_den(self):
        return self.__den

    def reduce(self):
        g = VerySimpleFraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g

    def gcd(n, m):
        if m == 0:
            return n
        else:
            return VerySimpleFraction.gcd(m, n % m)

    gcd = staticmethod(gcd)



class Fraction(object):
    """ Класс для представления обыкновенных дробей """

    # class attribute
    count = 0

    def __init__(self, *nd):
        self.__num = 0
        self.__den = 1
        self.__class__.count += 1

        if len(nd) == 1:
            self.__num = nd[0]
        elif len(nd) > 1:
            self.__num = nd[0]
            self.__den = nd[1]
            self.reduce()

    def __del__(self):
        print('Fraction was deleted')

    def __getitem__(self, name):
        if name == 'num':
            return self.__num
        elif name == 'den':
            return self.__den
        else:
            return None

    def reduce(self):
        g = Fraction.gcd(self.__num, self.__den)
        self.__num /= g
        self.__den /= g

    #  ============================================ magic методы
    def __add__(self, f):
        res = Fraction()
        res.__num = self.__num * f.__den + f.__num * self.__den
        res.__den = self.__den * f.__den
        res.reduce()
        return res

    # метод добавлен для демонстрации; практического смысла не имеет
    def __len__(self):
        return int(self.__num + self.__den)

    def __str__(self):
        return '%d/%d' % (self.__num, self.__den)

    def __lt__(self, f):
        return self.__num <= f.__num and self.__den <= f.__den

    def __contains__(self,f):
        if f.__num <= self.__num and f.__den <= self.__den:
            return True
        else:
            return False

    """ осторожно использовать:
    def __setattr__(self, name, value):
        if name == 'red':
            self.__dict__[name] = value + 1
        else:
            self.__dict__[name] = value
    """

    # ===========================================================

    @staticmethod
    def gcd(n, m):
        if m == 0:
            return n
        else:
            return Fraction.gcd(m, n % m)

    # num = property(get_num, set_num)
    # den = property(get_den, set_den)

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, n):
        self.__num = n

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, d):
        self.__den = d