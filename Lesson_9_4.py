class Car:
    def __init__(self, name, color, speed, is_police=False):
        self.name = name
        self.color = color
        self.speed = speed
        self.is_police = is_police
        print(f'New car: {self.name} (color {self.color}) is police car - {self.is_police}')

    def go(self):
        print(f'{self.name}: Car starts moving')

    def stop(self):
        print(f'{self.name}: Car stops')

    def turn(self, direction):
        print(f'{self.name}: Car turns {"left" if direction == 0 else "right"}')

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}'


class TownCar(Car):
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speed is too high!' \
            if self.speed > 60 else f'{self.name}: Car speed {self.speed}'

class WorkCar(Car):
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Speed is too high!' \
            if self.speed > 40 else f'{self.name}: Car speed {self.speed}'

class SportCar(Car):
    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. The car is flying!' \
            if self.speed > 220 else f'{self.name}: Car speed {self.speed}'

class PoliceCar(Car):
    def __init__(self, name, color, speed, is_police=True):
        super().__init__(name, color, speed, is_police)


police_car = PoliceCar('"Ford Crown Victoria"', "Black and White", 80)
police_car.go()
print(police_car.show_speed())
police_car.turn(0)
police_car.stop()
print()

work_car = WorkCar('"Volvo FH"', 'Brown', 40)
work_car.go()
work_car.turn(1)
print(work_car.show_speed())
work_car.turn(0)
work_car.stop()

print()
sport_car = SportCar('"Aston Martin DB11"', 'Silver', 180)
sport_car.go()
sport_car.turn(0)
print(sport_car.show_speed())
sport_car.stop()
print()

town_car = TownCar('"Mini Cooper"', 'Red', 50)
town_car.go()
town_car.turn(1)
town_car.turn(0)
print(town_car.show_speed())
town_car.stop()

print(f'\nCar {town_car.name} (color {town_car.color})')
print(f'Car {police_car.name} (color {police_car.color})')
