import abc


class Parser:
    """ Интерфейс "Парсер" """

    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def load(self, filename):
        """ абстрактная загрузка данных """

    @abc.abstractmethod
    def parse(self):
        """ абстрактный парсинг """


# как вариант еще:
#
# def parse(self):
#   raise NotImplementedError
#

class XMLParser(Parser):
    def load(self, filename):
        self._filename = filename

    def parse(self):
        print('Parsing XML: ' + self._filename)


class JSONParser(Parser):
    def load(self, filename):
        self._filename = filename

    def parse(self):
        print('Parsing JSON: ' + self._filename)


class StringParser:
    def __init__(self, s):
        self._string = s

    def load(self, s):
        self._string = s

    def parse(self):
        print('foo... ' + self._string)


class ParserFactory:
    """ Фабрика парсеров """
    @classmethod
    def create_parser(cls, filename):
        if filename.endswith('xml'):
            parser = XMLParser()
            parser.load(filename)
            return parser
        else:
            parser = JSONParser()
            parser.load(filename)
            return parser
