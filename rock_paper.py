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
    ready_check = input('Готов? Для выхода нажми "n" \n y/n:  ')
    if ready_check == 'y':

        while True:
            print('Для выхода введи "q" ниже')
            user_sign = input('Укажи свой знак: ')
            if user_sign not in signs and user_sign != 'q':
                if idiot_counter < 3:
                    idiot_counter += 1
                    print('Если ты забыл, то вот возможные варианты: ')
                    for item in signs:
                        print(item)
                else:
                    print('Антон, рад тебя видеть, играть мы конечно же не будем')
                    break

            elif user_sign == 'q':
                if user_score > pc_score:
                    print(f'Игра окончена! Ты выиграл!\n'
                          f' Счет: Игрок - {user_score}, PC - {pc_score}')
                    break
                elif user_score < pc_score:
                    print(f'Игра окончена! PC выиграл!\n'
                          f' Счет: Игрок - {user_score}, PC - {pc_score}')
                    break
                else:
                    print(f'Игра окончена! Ничья ЛОЛ\n'
                          f' Счет: Игрок - {user_score}, PC - {pc_score}')
                    break

            else:
                pc_sign = random.choice(signs)
                idiot_counter = 0
                print('Цу!')
                time.sleep(0.5)
                print('Е!')
                time.sleep(0.5)
                print('Фа!')
                time.sleep(0.5)
                # Блок знка ИИ равен камню
                if pc_sign == 'камень' and user_sign == 'камень':
                    print(f'ничья! {user_sign} vs {pc_sign}(pc)')
                    continue
                elif pc_sign == 'камень' and user_sign == 'ножницы':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'камень' and user_sign == 'бумага':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'камень' and user_sign == 'карандаш':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'камень' and user_sign == 'огонь':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'камень' and user_sign == 'вода':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue

                # Блок знак ИИ равен ножницам
                elif pc_sign == 'ножницы' and user_sign == 'ножницы':
                    print(f'ничья! {user_sign} vs {pc_sign}(pc)')
                    continue
                elif pc_sign == 'ножницы' and user_sign == 'бумага':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'ножницы' and user_sign == 'камень':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'ножницы' and user_sign == 'карандаш':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'ножницы' and user_sign == 'огонь':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'ножницы' and user_sign == 'вода':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue

                    # Блок знак ИИ равен бумаге
                elif pc_sign == 'бумага' and user_sign == 'бумага':
                    print(f'ничья! {user_sign} vs {pc_sign}(pc)')
                    continue
                elif pc_sign == 'бумага' and user_sign == 'ножницы':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'бумага' and user_sign == 'камень':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'бумага' and user_sign == 'карандаш':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'бумага' and user_sign == 'огонь':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'бумага' and user_sign == 'вода':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue

                    # Блок знак ИИ равен карандашу
                elif pc_sign == 'карандаш' and user_sign == 'бумага':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'карандаш' and user_sign == 'ножницы':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'карандаш' and user_sign == 'камень':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'карандаш' and user_sign == 'карандаш':
                    print(f'ничья! {user_sign} vs {pc_sign}(pc)')
                    continue
                elif pc_sign == 'карандаш' and user_sign == 'огонь':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'карандаш' and user_sign == 'вода':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue

                    # Блок знак ИИ равен огню
                elif pc_sign == 'огонь' and user_sign == 'бумага':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'огонь' and user_sign == 'ножницы':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'огонь' and user_sign == 'камень':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'огонь' and user_sign == 'карандаш':
                    print(f'PC победил! {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'огонь' and user_sign == 'огонь':
                    print(f'ничья! {user_sign} vs {pc_sign}(pc)')
                    continue
                elif pc_sign == 'огонь' and user_sign == 'вода':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue

                    # Блок знак ИИ равен воде
                elif pc_sign == 'вода' and user_sign == 'бумага':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'вода' and user_sign == 'ножницы':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'вода' and user_sign == 'камень':
                    print(f'PC победил {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'вода' and user_sign == 'карандаш':
                    print(f'Ты победил! {user_sign} vs {pc_sign}(pc)')
                    user_score += 1
                    continue
                elif pc_sign == 'вода' and user_sign == 'огонь':
                    print(f'PC победил {user_sign} vs {pc_sign}(pc)')
                    pc_score += 1
                    continue
                elif pc_sign == 'вода' and user_sign == 'вода':
                    print(f'ничья! {user_sign} vs {pc_sign}(pc)')
                    continue

    elif ready_check == 'n':
        print('Bye!')
        break

    else:
        idiot_counter += 1
        if idiot_counter < 3:
            print('Этот текст будет выводиться бесконечно, пока ты не введешь английскую "y"')
        else:
            print('Вряд ли ты осилишь такую игру. Заходи попозже')
            break
















