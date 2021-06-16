class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['*' * rows for _ in range(self.nums // rows)]) + '\n' + '*' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('Sum of cells is: ')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        print('Subtraction of cell is: ')
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'Error! Count of elements is incorrect!'

    def __mul__(self, other):
        print('Multiply of cell is: ')
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        print('Truediv of cell is: ')
        return Cell(self.nums // other.nums)


cell_1 = Cell(42)
cell_2 = Cell(6)
print(cell_1 + cell_2)
print(cell_1 - cell_2)
print(cell_1 * cell_2)
print(cell_1 // cell_2)
print(cell_2.make_order(7))
