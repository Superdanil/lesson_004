# -*- coding: utf-8 -*-

import simple_draw as sd


sd.resolution = (1200, 800)


# 1) Написать функцию draw_branches, которая должна рисовать две ветви дерева из начальной точки
# Функция должна принимать параметры:
# - точка начала рисования,
# - угол рисования,
# - длина ветвей,
# Отклонение ветвей от угла рисования принять 30 градусов,

# 2) Сделать draw_branches рекурсивной
# - добавить проверку на длину ветвей, если длина меньше 10 - не рисовать
# - вызывать саму себя 2 раза из точек-концов нарисованных ветвей,
#   с параметром "угол рисования" равным углу только что нарисованной ветви,
#   и параметром "длинна ветвей" в 0.75 меньшей чем длина только что нарисованной ветви

# 3) первоначальный вызов:
root_point = sd.get_point(sd.resolution[0]/2, 30)
# draw_bunches(start_point=root_point, angle=90, length=100)

# Пригодятся функции
# sd.get_point()
# sd.get_vector()
# Возможный результат решения см lesson_004/results/exercise_04_fractal_01.jpg

# можно поиграть -шрифтами- цветами и углами отклонения

# TODO здесь ваш код

"""
def draw_branches(point, angle, length, delta=0): # получилось неплохо
    if length < 2:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta
    next_length = length * .75
    for delta in range(-30, 31, 60):
        draw_branches(point=next_point, angle=next_angle, length=next_length, delta=delta)

draw_branches(point=root_point, angle=90, length=120)

"""

# 4) Усложненное задание (делать по желанию)
# - сделать рандомное отклонение угла ветвей в пределах 40% от 30-ти градусов
# - сделать рандомное отклонение длины ветвей в пределах 20% от коэффициента 0.75
# Возможный результат решения см lesson_004/results/exercise_04_fractal_02.jpg

# Пригодятся функции
# sd.random_number()

def draw_branches(point, angle, length, delta=0): # тоже по кайфу
    if length < 2:
        return
    v1 = sd.get_vector(start_point=point, angle=angle, length=length, width=1)
    v1.draw()
    next_point = v1.end_point
    next_angle = angle - delta * sd.random_number(60, 140)/100
    next_length = length * sd.random_number(60, 90)/100
    for delta in range(-30, 31, 60):
        draw_branches(point=next_point, angle=next_angle, length=next_length, delta=delta)

draw_branches(point=root_point, angle=90, length=120)





sd.pause()


