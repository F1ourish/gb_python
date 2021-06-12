class Stationery:
    def __init__(self, title="Something that can draw"):
        self.title = title

    def draw(self):
        print(f'Start drawing. {self.title}')


class Pen(Stationery):
    def draw(self):
        print(f'Start drawing with the {self.title} pen')

class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing with the {self.title} pencil')

class Marker(Stationery):
    def draw(self):
        print(f'Start drawing with the {self.title} marker')


stat = Stationery()
stat.draw()
pen = Pen('Parker')
pen.draw()
pencil = Pencil('Faber-Castell')
pencil.draw()
marker = Marker('Copic')
marker.draw()
