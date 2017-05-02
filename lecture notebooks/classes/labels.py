class Label(object):
    """ Класс для произвольных наклеек (этикеток)
    (может быть любым изображением) """
    def __init__(self, *size):
        if len(size) > 1:
            self._width = size[0]
            self._height = size[1]
        else:
            self._width = 0
            self._height = 0

    def load(self, filename):
        self._filename = filename
        # self._width = Image.get_width(filename)    как-то так
        # self._width = Image.get_height(filename)

    def scan(self):
        pass

    def scale(self, width, height):
        print('The {} was scaled at {} x {}'.format(
                self.__class__.__name__, width, height))

    # еще пример синтаксиса Property
    @property
    def filename(self):
        return self._filename

    @filename.setter
    def filename(self, filename):
        self.load(filename)


class Barcode(Label):
    """ Класс для наклеек со штрих-кодом """
    def __init__(self):
        super(Barcode, self).__init__(100, 25)

    def recognize(self):
        self.scale(100, 25)
        # сюда пишем код для распознавания
        # ...
        return '0098000129212'


class QRcode(Label):
    """ Класс для наклеек с QR-кодом """
    def __init__(self):
        super(QRcode, self).__init__(100, 100)

    def recognize(self):
        self.scale(100, 100)
        # сюда пишем код для распознавания
        # ...
        return 'lalalala'
