from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self):
        pass

    @property
    @abstractmethod
    def scatter(self):
        pass

    def __add__(self, other):
        return self.scatter + other.scatter


class Coat(Clothes):
    def __init__(self, size):
        super().__init__()
        self.size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, size):
        if size < 40:
            print('Minimal size is 40')
            self.__size = 40
        elif size > 58:
            print('Maximal size is 58')
            self.__size = 58
        else:
            self.__size = size

    @property
    def scatter(self):
        return self.__size / 6.5 + 0.5


class Costume(Clothes):
    def __init__(self, height):
        super().__init__()
        self.height = height

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, height):
        if height < 150:
            print('Minimal size is 150')
            self.__height = 150
        elif height > 240:
            print('Maximal size is 240')
            self.__height = 240
        else:
            self.__height = height

    @property
    def scatter(self):
        return 2 * (self.__height / 100) + 0.3


coat = Coat(int(input('Input size of the coat to do scatter: ')))
print(f'You will need {coat.scatter:.2f} meters of the cloth for a coat {coat.size} size')
costume = Costume(int(input('Input size of the costume to do scatter: ')))
print(f'You will need {costume.scatter:.2f} meters of the cloth for a costume {costume.height} height')
print(f'You will need {coat + costume:.2f} meters of the cloth in total')


# ************************************************* Простой вариант ***************************************************


# from abc import ABC, abstractmethod
#
#
# class Clothes(ABC):
#     result = 0
#
#     def __init__(self, a):
#         self.a = a
#
#     @property
#     @abstractmethod
#     def consumption(self):
#         pass
#
#     def __add__(self, other):
#         Clothes.result += self.consumption + other.consumption
#         return Costume(0)
#
#     def __str__(self):
#         res = Clothes.result
#         Clothes.result = 0
#         return f'{res}'
#
# class Coat(Clothes):
#     @property
#     def consumption(self):
#         return round(self.a / 6.5) + 0.5
#
#
# class Costume(Clothes):
#     @property
#     def consumption(self):
#         return round((2 *self.a + 0.3) / 100)
#
#
# coat = Coat(46)
# costume = Costume(120)
# print(coat + costume + coat)
