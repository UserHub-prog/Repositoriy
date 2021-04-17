import time 
from random import randint

def minigame():
    board = []

    for x in range(4):
        board.append(["O"] * 4)

    print("Начнем игру в Морской бой!")
    for row in board:
        print((" ").join(row))

    ship_row = randint(0, len(board) - 1)
    ship_col = randint(0, len(board[0]) - 1)

    global b1

    for b1 in range(7):
        print ("Ход: ", b1)
        try:
            guess_row = int(input("Строка 0-3:"))
            guess_col = int(input("Столбец 0-3:"))
        except ValueError:
            print('Здесь только цифры!')       
        try:
            if guess_row == ship_row and guess_col == ship_col:
                print("Поздравляю, ты потопил мой корабль!")
                break
        except UnboundLocalError:
            pass   
        else:
            if (guess_row < 0 or guess_row > 3) or (guess_col < 0 or guess_col > 3):
                print("Oops, эти координаты не в нашем океане.")
            elif(board[guess_row][guess_col] == "X"):
                print("Эти координаты вы уже называли.")
            else:
                print("Мимо!")
                board[guess_row][guess_col] = "X"
        if b1 == 6:
            print("Игра окончена! Вы проиграли!")
            break
        #b1 =+ 1
        for row in board:
            print((" ").join(row))

my_while = True

time.sleep(2)
print('Однажды, в одном селе. Жил мальчик, и его звали Федя. \nЕму было не больше 7 лет. \nИ один раз с ним произошла печальная история.')
time.sleep(2)
print('У него был друг Дима (он был на год старше Феди), и Димушка решил позвать друга на рыбалку. Согласился ли Федя?')

while my_while:
    a1 = input('Вы хотите выйти из игры? (ДА/НЕТ) ')
    if a1 == 'ДА':
        my_while = False
        exit()
    elif a1 == 'НЕТ':
        my_while = False
        pass
    else:
        print('Вы ввели не корректную информацию!') 

my_while = True

while my_while:

    firstinput = str(input('Пойдет ли Федя на рыбалку с Димой? (ДА/НЕТ) '))

    if firstinput == 'ДА':
        my_while = False
        pass
        time.sleep(2)
        print('Конечно пошел, ведь у него не было причин отказываться.\nФедя взял банку червей, удочку, хлеб, а заодно, прихватил свою собаку Бима. \nОни не спеша направились в сторону местной речки.')
        time.sleep(2)
        print('Она была в десяти километрах от дома Феди. Дети весело болтали и хорошо проводили время.')
        time.sleep(2)
        print('Через один час, они уже были возле речки.')
        time.sleep(2)
        print('Они достали все необходимое, и начали рыбачить.')

        my_while = True

        while my_while:
            a1 = input('Вы хотите выйти из игры? (ДА/НЕТ) ')
            if a1 == 'ДА':
                my_while = False
                exit()
            elif a1 == 'НЕТ':
                my_while = False
                pass
            else:
                print('Вы ввели не корректную информацию!') 
        print('Но вдруг, у Димы начало булькать. Он приготовился и начал потихоньку вытаскивать рыбу.')
        time.sleep(2)
        print('И неожиданно собака прыгнула за рыбой. Она не понимала, что речка была глубокой.\nТакже, Бим не умел плавать, и ребята это хорошо знали.')
        time.sleep(2)
        print('Дети были в панике, не знали, что делать.')
        time.sleep(2)
        print('И тут у мальчиков появился выбор: попытаться спасти собачку или бросить её, так как Бим был уже достаточно далеко.')

        my_while = True

        while my_while:
            a1 = input('Вы хотите выйти из игры? (ДА/НЕТ) ')
            if a1 == 'ДА':
                my_while = False
                exit()
            elif a1 == 'НЕТ':
                my_while = False
                pass
            else:
                print('Вы ввели не корректную информацию!') 

        my_while = True
        print('Вы не можете продолжить, пока не выиграйте в морском бою! У вас 7 ходов!')

        while my_while:
            minigame()  
            if b1 != 6:
                my_while = False
                print('Вы можете играть дальше!')
                pass
            elif b1 == 6:    
                print('Вы не можете играть дальше. Попробуйте снова.') 

        my_while = True  

        while my_while:

            secondinput = str(input('Попытаться спасти Бима или бросить его на произвол судьбы? (СПАСТИ/БРОСИТЬ) '))

            if secondinput == 'СПАСТИ':
                my_while = False
                pass

                my_while = True

                while my_while:
                    thirdinput = str(input('Как Федя  попытается спасти Бима? \n(ПОПЛЫТЬ ЗА БИМОМ/ПОЗВАТЬ НА ПОМОЩЬ/КИНУТЬ ПАЛКУ СОБАКЕ)'))
                    if thirdinput == 'ПОПЛЫТЬ ЗА БИМОМ':
                        my_while = False
                        pass
                        time.sleep(2)
                        print('Ни Федя, ни Дима не умели плавать.')
                        time.sleep(2)
                        print('Но Федя решился, все-таки попытаться спасти бедную собаку.\nОн поплыл за ним, но вдруг зацепился за водоросли.\n')
                        time.sleep(2)
                        print('Мальчик начал тонуть. Дима был настолько расстерян, что даже не смог пошевельнуться.')
                        time.sleep(2)
                        print('Прошло 5 минут, а признаков жизни Федя и Бим, так и не подали. Утонула и собачка, и бедный Федя.')
                        time.sleep(2)
                        print('')
                        print('<-------------------------------КОНЕЦ------------------------------->')

                        my_while = True

                        while my_while:
                            a1 = input('Вы хотите выйти из игры? (ДА/НЕТ) ')
                            if a1 == 'ДА':
                                my_while = False
                                exit()
                            elif a1 == 'НЕТ':
                                print('Но ведь история уже закончилась.')
                            else:
                                print('Вы ввели некорректную информацию!')  
                    elif thirdinput == 'ПОЗВАТЬ НА ПОМОЩЬ':
                        my_while = False
                        pass
                        time.sleep(2)    
                        print('Федя решил позвать на помощь.')
                        time.sleep(2)
                        print('"ПОМОГИТЕ!!!" - крикнул мальчик.')
                        time.sleep(2)
                        print('Из глубин леса вышел лесник.') 
                        my_while = True

                        while my_while:
                            a1 = input('Вы хотите выйти из игры? (ДА/НЕТ) ')
                            if a1 == 'ДА':
                                my_while = False
                                exit()
                            elif a1 == 'НЕТ':
                                my_while = False
                                pass
                            else:
                                print('Вы ввели некорректную информацию!')     
                        print('Он, увидев тонущую собаку, прыгнул в воду.')
                        time.sleep(2)
                        print('Ему удалось спасти Бима.')
                        time.sleep(2)
                        print('Мужчина спросил, почему мальчики не попытались помочь собаке?')
                        time.sleep(2)
                        print('Мальчики ответили, что не умеют плавать.')
                        time.sleep(2)
                        print('Лесник предложил поучиться их этому делу. Ребята согласились.')
                        time.sleep(2)
                        print('И с того дня, всей компанией, они шли на эту речку и тренировались плавать.')
                        time.sleep(2)
                        print('')
                        print('<-------------------------------КОНЕЦ------------------------------->')

                        my_while = True
                        
                        while my_while:
                            a4 = str(input('Вы хотите выйти из игры? (ДА/НЕТ) '))
                            if a4 == 'ДА':
                                my_while = False
                                exit()
                            elif a4 == 'НЕТ':
                                print('Но ведь история уже закончилась.')
                            else:
                                print('Вы ввели некорректную информацию!')   
                    elif thirdinput == 'КИНУТЬ ПАЛКУ СОБАКЕ':
                        my_while = False
                        pass
                        time.sleep(2)
                        print('Федя решил помочь бедному Биму, кинув палку.')
                        time.sleep(2)
                        print('Собака не поняла, зачем хозяин кинул деревяшку ей. Так и потанул несчастный Бим')
                        time.sleep(2)
                        print('Федя не стал рисковать собственной жизнью ради собаки. Бим так и утонул.\nФеде было очень больно от этого.\nВсю жизнь, Федя не переставал думать о Биме и о его ужасной гибели.')
                        time.sleep(2)
                        print('')
                        print('<-------------------------------КОНЕЦ------------------------------->') 
    
                        my_while = True

                        while my_while:
                            a4 = str(input('Вы хотите выйти из игры? (ДА/НЕТ) '))
                            if a4 == 'ДА':
                                my_while = False
                                exit()
                            elif a4 == 'НЕТ':
                                print('Но ведь история уже закончилась.')
                            else:
                                print('Вы ввели не корректную информацию!')    
                    else:
                        print('Вы ввели некорректную информацию!')         
            elif secondinput == 'БРОСИТЬ':
                my_while = False
                pass
                time.sleep(2)
                print('Федя не стал рисковать собственной жизнью ради собаки. Бим так и утонул.\nФеде было очень больно от этого.\nВсю жизнь, Федя не переставал думать о Биме и о его ужасной гибели.') 
                time.sleep(2)
                print('')
                print('<-------------------------------КОНЕЦ------------------------------->')  
                
                my_while = True
                
                while my_while:
                    a4 = str(input('Вы хотите выйти из игры? (ДА/НЕТ) '))
                    if a4 == 'ДА':
                        my_while = False
                        exit()
                    elif a4 == 'НЕТ':
                        print('Но ведь история уже закончилась.')
                    else:
                        print('Вы ввели некорректную информацию!')   
            else:
                print('Вы ввели некорректную информацию!')          

    elif firstinput == 'НЕТ':
        my_while = False
        pass
        time.sleep(2)
        print('Он не захотел идти сегодня на рыбалку. Видимо у него были более важные дела.')
        time.sleep(2)
        print('Дима обиделся и долго не говорил с Федей.\nНо потом, все же, простил его.')
        time.sleep(2)
        print('')
        print('<-------------------------------КОНЕЦ------------------------------->')
        
        my_while = True

        while my_while:
            a4 = str(input('Вы хотите выйти из игры? (ДА/НЕТ) '))
            if a4 == 'ДА':
                my_while = False
                exit()
            elif a4 == 'НЕТ':
                print('Но ведь история уже закончилась.')
            else:
                print('Вы ввели некорректную информацию!')     
    else:
        print('Вы ввели некорректную информацию!')
