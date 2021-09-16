import time
import random


signs = ['камень', 'ножницы', 'бумага', 'карандаш', 'огонь', 'вода']

idiot_counter = 0
user_score = 0
pc_score = 0
while True:
    print('Привет! Вот список возможных знаков: ')
    for item in signs:
        print(item)
    ready_check = input('Готов? y/n')
    if ready_check == 'y':
        while True:
            print('Для выхода введи "q" ниже')
            user_sign = input('Укажи свой знак: ')
            if user_sign not in signs:
                if idiot_counter < 3:
                    idiot_counter += 1
                    print('Если ты забыл, то вот возможные варианты: ')
                    for item in signs:
                        print(item)
                else:
                    print('Антон, рад тебя видеть, играть мы конечно же не будем')
                    break
            else:
                fight_list = []
                pc_sign = random.choice(signs)
                fight_list.append(user_sign)
                fight_list.append(pc_score)
                idiot_counter = 0
                print('Цу!')
                time.sleep(0.5)
                print('Е!')
                time.sleep(0.5)
                print('Фа!')
                time.sleep(0.5)











    else:
        if idiot_counter < 3:
            print('Этот текст будет выводиться бесконечно, пока ты не введешь "y"')
        else:
            print('Вряд ли ты осилишь такую игру. Заходи попозже')
            time.sleep(180)
            break
















