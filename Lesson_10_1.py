# class Matrix:
#     def __init__(self, list):
#         self.list = list
#
#     def __str__(self):
#         return '\n'.join('\t'.join([f'{el}' for el in string]) for string in self.list)
#
#     def __add__(self, other):
#         try:
#             a = [[int(self.list[string][el]) + int(other.list[string][el]) for el in range(len(self.list[string]))]
#                  for string in range(len(self.list))]
#             return Matrix(a)
#         except IndexError:
#             return f'Matrix error'
#
# matrix_1 = [[1, 4, 8, -8], [1, 3, -3 ,7], [0, 2, 2, 8]]
# matrix_2 = [[0, 2, 2, 8], [1, 4, 8, 8], [1, 3, 3 ,7]]
#
# matr_1 = Matrix(matrix_1)
# matr_2 = Matrix(matrix_2)
# sum = matr_1 + matr_2
# print(f'Matrix 1:\n{matr_1}\n{"_" * 30}\n')
# print(f'Matrix 2:\n{matr_2}\n{"_" * 30}\n')
# print(f'Matrix 1 + Matrix 2\n{matr_1 + matr_2}')


# ************************************************ Другой вариант *****************************************************


# a = [[1, 4, 8, 8], [1, 3, 3 ,7], [0, 2, 2, 8]]
# b = [[0, 2, 2, 8], [1, 4, 8, 8], [1, 3, 3 ,7]]
#
#
# class Matrix:
#     def __init__(self, list):
#         self.list = list
#
#     def __str__(self):
#         return '\n'.join(map(str, self.list))
#
#     def __add__(self, another):
#         sum = []
#         for el in range(len(self.list)):
#             sum.append([])
#             for i in range(len(self.list[0])):
#                 sum[el].append(self.list[el][i] + another.list[el][i])
#         return '\n'.join(map(str, sum))
#
#
# matrix_1 = Matrix(a)
# matrix_2 = Matrix(b)
# print(f'Matrix 1:\n{matrix_1}\n{"_" * 30}\n')
# print(f'Matrix 2:\n{matrix_2}\n{"_" * 30}\n')
# print(f'Matrix 1 + Matrix 2\n{matrix_1 + matrix_2}')


# ************************************************ Третий вариант *****************************************************

from itertools import zip_longest


class Matrix(object):
    def __init__(self, m):
        self.m = m

    def __str__(self):
        return str('\n'.join(['\t'.join([str(i) for i in j]) for j in self.m]))

    def __add__(self, other):
        return Matrix([map(sum, zip_longest(*t, fillvalue=0))
                       for t in zip_longest(self.m, other.m, fillvalue=[])])


a = [[1, 4, 8, 8], [1, 3, 3 ,7], [0, 2, 2, 8]]
b = [[0, 2, 2, 8], [1, 4, 8, 8], [1, 3, 3 ,7]]
matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f'Matrix 1:\n{matrix_1}\n{"_" * 30}\n')
print(f'Matrix 2:\n{matrix_2}\n{"_" * 30}\n')
print(f'Matrix 1 + Matrix 2\n{matrix_1 + matrix_2}')
