# -*- coding: utf-8 -*-

import simple_draw as sd
sd.resolution = (1200, 800)

from random import randrange

# На основе кода из практической части реализовать снегопад:
# - создать списки данных для отрисовки N снежинок
# - нарисовать падение этих N снежинок
# - создать список рандомных длин лучей снежинок (от 10 до 100) и пусть все снежинки будут разные

n = 20

# Пригодятся функции
# sd.get_point()
# sd.snowflake()
# sd.sleep()
# sd.random_number()
# sd.user_want_exit()

# TODO здесь ваш код
# while True:
#     sd.clear_screen()
#     pass
#     pass
#     pass
#     sd.sleep(0.1)
#     if sd.user_want_exit():
#         break


# объявляем список размеров снежинок
lst = [randrange(10, 50) for _ in range(n)]

print(lst)
# объявляем координату Y появления снежинок на экране
y = [sd.resolution[1]]*20
print(y)
# объявляем список координат Х появления снежинок на экране
x = [x for x in range(100, sd.resolution[0], 55)]
print(x)


while True:  # получилось что-то странное, сугроб не реализован в целях экономии времени
    sd.clear_screen()
    for i in range(n):
        point = sd.get_point(x[i], y[i])
        sd.snowflake(center=point, length=lst[i])
        y[i] -= sd.random_number(1, 100)/10
        if y[i] < 0:
            break
        x[i] += sd.random_number(-20, 20)


    sd.sleep(0.1)
    if sd.user_want_exit():
        break
sd.pause()

# подсказка! для ускорения отрисовки можно
#  - убрать clear_screen()
#  - в начале рисования всех снежинок вызвать sd.start_drawing()
#  - на старом месте снежинки отрисовать её же, но цветом sd.background_color
#  - сдвинуть снежинку
#  - отрисовать её цветом sd.COLOR_WHITE на новом месте
#  - после отрисовки всех снежинок, перед sleep(), вызвать sd.finish_drawing()


# 4) Усложненное задание (делать по желанию)
# - сделать рандомные отклонения вправо/влево при каждом шаге
# - сделать сугроб внизу экрана - если снежинка долетает до низа, оставлять её там,
#   и добавлять новую снежинку
# Результат решения см https://youtu.be/XBx0JtxHiLg


