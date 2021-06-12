# from time import sleep
#
# class TrafficLight:
#     __color = "Трёхцветный"
#
#     def running(self):
#         while True:
#             print("Сейчас горит красный")
#             sleep(7)
#             print("Сейчас горит жёлтый")
#             sleep(2)
#             print("Сейчас горит зелёный")
#             sleep(10)
#
#
# trafficLight = TrafficLight()
# trafficLight.running()


# ********************************* Альтернативный вариант решения ****************************************************

# from time import sleep
# from itertools import cycle
#
#
# class TrafficLight:
#     __color = [["red", [7, 31]], ["yellow", [2, 33]], ["green", [7, 32]], ["yellow", [2, 33]]]
#
#     def running(self):
#         for light in cycle(self.__color):
#             print(f"\r\033[{light[1][1]}m\033[1m{light[0]}\033[0m", end="")
#             sleep(light[1][0])
#
# trafficLight_1 = TrafficLight()
# trafficLight_1.running()


# ****************************** Ещё один альтернативный вариант решения **********************************************

# from time import sleep
# from itertools import cycle
#
#
# class TrafficLight:
#     __color = ["   ", [7, 2, 4], ["\033[41m\033[1m", "\033[43m\033[1m", "\033[42m\033[1m"]]
#
#     def running(self):
#         col_list = ["", ""]
#         for n in cycle((0, 1, 2)):
#             col_list[1] = self.__color[2][n]
#             print(f"\r({col_list[int(n == 0)]}{self.__color[0]}\033[0m)"
#                   f"({col_list[int(n == 1)]}{self.__color[0]}\033[0m)"
#                   f"({col_list[int(n == 2)]}{self.__color[0]}\033[0m)", end="")
#             sleep(self.__color[1][n])
#
#
# trafficLight_2 = TrafficLight()
# trafficLight_2.running()

# ******************************** Ещё один альтернативный вариант решения_2 *****************************************

from time import sleep
import colorama
import sys

colorama.init()


class TrafficLight:
    def running(self):
        while True:
            print(f'\r\033[31m{chr(11035)} ', end='')
            sleep(4)
            print(f'\r\033[30m{chr(11035)} ')
            print(f'\r\033[33m{chr(11035)} ', end='')
            sleep(2)
            print(f'\r\033[30m{chr(11035)} ', end='')
            print(f'\r\033[32m{chr(11035)} ', end='')
            sleep(4)
            print(f'\r\033[33m{chr(11035)} ', end='')
            sys.stdout.write('\r\x1b[2A')


trafficLight_3 = TrafficLight()
trafficLight_3.running()
