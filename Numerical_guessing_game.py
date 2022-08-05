import random


information = []
numder_of_attempt = 0
clear = lambda: os.system('cls')
wallet = 0

def numerical_guessing_game():           ## Новая игра
    print('\nДобро пожаловать в числовую угадайку! Напиши своё имя, чтобы я знал, как к тебе обращаться!\n')
    name = input('Тебя зовут: ')
    information.append(name)
    print(f'\n\t{name.title()}, приятной игры!\n\n Я загадал от 1-го до n-го числа.\n\n\t\tУдачи!')
    while True:
        try:
            frontier = int(input('\n Введите границу n в пределах которой будет генерироваться число: '))
            break
        except ValueError:
            print('\n Вы ввели не целое число.')
        
            #print('\nГраница строго > 0. Попробуйте ввести число ещё раз')
        
    
            
    information.append(frontier)
    number = random.randint(1, frontier)
    information.append(number)
    print(f'\nВы успешно сгенерировали все целые числа от 1-го до {frontier}-го.\n\nВаша задача - угадать число, которое я загадал в этой границе!')
    


def new_game1(level, start, stop, name, wallet):    ## Уровень 1
    print(f'\n{name1.title()}, вы повысили свой уровень до {level}-ого!\n\nВсего в игре пять уровней, дойдёшь до пятого, и ты - победил!\n\nНа твоём балансе {wallet} монет!\n\nТеперь ты должен отгадать число, которое находится в диапозоне {start} до {stop}!')
    print(f'\nЗа каждый неправильный ответ на уровне {level} вы будете терять 100 монет.\nЕсли на балансе будет мало средств, - вы проиграли.')
    number = random.randint(1, stop)
    while True:
        while True:
            try:
                message = int(input('\nВведи число: '))
                break
            except ValueError:
                print('\nВы ввели не целое число')
            
        if wallet == 0:
            print('\nВы проиграли, - на вашем балансе недостаточно средств.')
            exit(0)
        elif message > 30 or message < 1:
            print('\nВы ввели некоректное число! Монеты с вашего баланса не списаны. Диапозон от 1 до 30.')
        if message < number and  message > 0:
            print('\nЧисло которое я загадал, - больше')
            wallet -= 100
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message > number and message < 31 and message > 0:
            print('\nЧисло которое я загадал, - меньше')
            wallet -= 100
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message == number:
            print(f'\n{name} вы угадали число! ({number})\n\nВаш уровень повышен')
            cls()
            wallet += 2000
            new_game2(2, 1, 150, name, wallet,)

            
def new_game2(level, start, stop, name, wallet):  ## Уровень 2
    print(f'\n{name1.title()}, вы повысили свой уровень до {level}-ого!\n\nВсего в игре пять уровней, дойдёшь до пятого, и ты - победил!\n\nНа твоём балансе {wallet} монет!\n\nТеперь ты должен отгадать число, которое находится в диапозоне {start} до {stop}!')
    print(f'\nЗа каждый неправильный ответ на уровне {level} вы будете терять 200 монет.\nЕсли на балансе будет мало средств, - вы проиграли.')
    number = random.randint(1, stop)
    while True:
        while True:
            try:
                message = int(input('\nВведи число: '))
                break
            except ValueError:
                print('\nВы ввели не целое число')
        if wallet < 200 :
            print('\nВы проиграли, - на вашем балансе недостаточно средств.')
            exit(0)
        elif message > 150 or message < 1:
            print('\nВы ввели некоректное число! Монеты с вашего баланса не списаны. Диапозон от 1 до 150.')
        if message < number and message > 0:
            print('\nЧисло которое я загадал, - больше')
            wallet -= 200
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message > number and message < 151 and message > 0:
            print('\nЧисло которое я загадал, - меньше')
            wallet -= 200
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message == number:
            print(f'\n{name} вы угадали число! ({number})\n\nВаш уровень повышен.')
            cls()
            wallet += 2000
            new_game3(3, 1, 10, name, wallet)
            
def new_game3(level, start, stop, name, wallet):  ## Уровень 3
    print(f'\n{name1.title()}, вы повысили свой уровень до {level}-ого!\n\nВсего в игре пять уровней, дойдёшь до пятого, и ты - победил!\n\nНа твоём балансе {wallet} монет!\n\nТеперь ты должен отгадать число, которое находится в диапозоне {start} до {stop}!')
    print(f'\nЗа каждый неправильный ответ на уровне {level} вы будете терять 500 монет.\nЕсли на балансе будет мало средств, - вы проиграли.')
    number = random.randint(1, stop)
    while True:
        while True:
            try:
                message = int(input('\nВведи число: '))
                break
            except ValueError:
                print('\nВы ввели не целое число.')
        if message > 10 or message < 1:
            print('\nВы ввели некоректное число! Монеты с вашего баланса не списаны. Диапозон от 1 до 10.')
        if wallet < 500 :
            print('\nВы проиграли, - на вашем балансе недостаточно средств.')
            exit(0) 
        if message < number and message > 0:
            print('\nЧисло которое я загадал, - больше')
            wallet -= 500
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message > number and message < 11 and message > 0:
            print('\nЧисло которое я загадал, - меньше')
            wallet -= 500
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message == number:
            print(f'\n{name} вы угадали число! ({number})\n\nВаш уровень повышен.')
            cls()
            wallet += 500
            new_game4(4, 1, 1000, name, wallet)


def new_game4(level, start, stop, name, wallet):  ## Уровень 4
    print(f'{name1.title()}, вы повысили свой уровень до {level}-ого!\n\nВсего в игре пять уровней, дойдёшь до пятого, и ты - победил!\n\nНа твоём балансе {wallet} монет!\n\nТеперь ты должен отгадать число, которое находится в диапозоне {start} до {stop}!')
    print(f'\nЗа каждый неправильный ответ на уровне {level} вы будете терять 50 монет.\nЕсли на балансе будет мало средств, - вы проиграли.')
    number = random.randint(1, stop)
    while True:
        while True:
            try:
                message = int(input('\nВведи число: '))
                break
            except ValueError:
                print('\nВы ввели не целое число.')
        if message > 1000 or message < 1:
            print('\nВы ввели некоректное число! Монеты с вашего баланса не списаны. Диапозон от 1 до 1000.')
        if wallet < 50 :
            print('\nВы проиграли, - на вашем балансе недостаточно средств.')
            exit(0) 
        if message < number and message > 0:
            print('\nЧисло которое я загадал, - больше')
            wallet -= 50
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message > number and message < 1001 and message > 0:
            print('\nЧисло которое я загадал, - меньше')
            wallet -= 50
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message == number:
            print(f'\n{name} вы угадали число! ({number})\n\nВаш уровень повышен.')
            cls()
            wallet += 1500
            new_game5(5, 1, 20, name, wallet)
            
def new_game5(level, start, stop, name, wallet):  ## Уровень 5
    print(f'{name1.title()}, вы повысили свой уровень до {level}-ого!\n\nПройди пятый уровень, и победишь в моей игре!!\n\nНа твоём балансе {wallet} монет!\n\nТеперь ты должен отгадать число, которое находится в диапозоне {start} до {stop}!')
    print(f'\nЗа каждый неправильный ответ на уровне {level} вы будете терять 500 монет.\nЕсли на балансе будет мало средств, - вы проиграли.')
    number = random.randint(1, stop)
    while True:
        while True:
            try:
                message = int(input('\nВведи число: '))
                break
            except ValueError:
                print('\nВы ввели не целое число.')
        if message > 20 or message < 1:
            print('\nВы ввели некоректное число! Монеты с вашего баланса не списаны. Диапозон от 1 до 20.')
        if wallet < 500 :
            print('\nВы проиграли, - на вашем балансе недостаточно средств.')
            exit(0) 
        if message < number and message > 0:
            print('\nЧисло которое я загадал, - больше')
            wallet -= 500
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message > number and message < 21 and message > 0:
            print('\nЧисло которое я загадал, - меньше')
            wallet -= 500
            print(f'\nВаш баланас: {wallet} монет.')
            continue
        elif message == number:
            print(f'\n{name} вы угадали число! ({number})\n{name} Вы прошли игру!.')
            cls()
            win()

def win():     ## Победное сообщение
    print('Поздравляю! Вы прошли игру "Числовая угадайка". Разработчик игры - Андрей Семёнов, - начинающий программист.\n\n Я буду выпускать другие интересные проекты!"Числовая угадайка" - мой первый крупный проект!')  
    print(f'Разработчик: vk.com/memhy')
    exit(0)


            
def cls():       ## Очистка консоли
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")

    
numerical_guessing_game()

while True:
    
    number1 = information[-1]
    name1 = information[0]
    while True:
        try:
            attempt = int(input('\nВаш вариант загаданного числа: '))
            break
        except ValueError:
            print('\nВы ввели не целое число.')
    if attempt < number1:
        print('\nЗагаданное число больше!')
        numder_of_attempt += 1
        continue
    elif attempt > number1:
        print('\nЧисло, которое я загадал - меньше!')
        numder_of_attempt += 1
        continue
    else:
        numder_of_attempt += 1
        
        information.append(numder_of_attempt)
        
        print(f'\n{name1.title()}, поздравляем вы угадали число, которое я задумал! ({number1})\n\nКоличество попыток, которое вы потратили: {numder_of_attempt}.')
        message = input('\nТы можешь начать новую игру и проходить уровни (Введи "Играть").\n\nТы можешь продолжать угадывать числа с заданами границами (Введи "Снова").\n\nЧтобы завершить игру введи "Выйти" ')
        if message.lower() == 'играть':
            cls()
            wallet += 1000
            new_game1(1, 1, 30, name1, wallet)
            numder_of_attempt = 0
            information.append(wallet)
        elif message.lower() == 'выйти':
            print('\nИгра завершена, приходи ещё!')
            break
        elif message.lower() == 'снова':
            cls()
            numerical_guessing_game()
        else:
            break
            
