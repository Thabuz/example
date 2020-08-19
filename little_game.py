import random

number = random.randint(1, 100)

user_number = None
count = 0

levels = {1: 10, 2: 5, 3: 3}
max_count = levels[int(input('Введите уровень сложности: '))]

user_count = int(input('Введите колличество игроков: '))
users = []

for i in range(user_count):
    user_name = input(f'Введите имя пользователя {i}: ')
    users.append(user_name)


winner = False
winner_name = None
while winner != True:
    count += 1
    if count > max_count:
        print('Все пользователи проиграли!')
        break
    print(f'Попытка №{count}')
    for i in users:
        print(f'Ход пользователя {i}')
        user_number = int(input('Введите число: '))
        if user_number == number:
            winner = True
            winner_name = i
            break
        if user_number > number:
            print('Загаданное число меньше введенного')
        elif user_number < number:
            print('Загаданное число больше введенного')
else:
    print(f'Победил пользователь {winner_name}!')
