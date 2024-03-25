from random import randint
m = [1, 2, 3, 4, 5, 6, 7, 8, 9] # массив - поле
comb = [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 4, 8], [2, 4, 6], [0, 3, 6], [1, 4, 7], [2, 5, 8]] # выигрышные комбинации

def Start():
    return randint(1, 2)


def Step(symb_my, symb_enemy):
    global m
    step = Check(symb_my) # стратегия компьютера (ищет комбинацию из 2, чтобы доставить 3-ю)
    if step == -1: # если для компьютера нет выигрышного хода, то ищется 'опасная зона', чтобы предотвратить победу соперника
        step = Check(symb_enemy)
        if step == -1: # опасных и выигрышных позиций нет => ходит в первую попавшуюся
            for i in range(len(m)):
                if m[i] == i + 1:
                    step = i
                    break
    m[step] = symb_my
    return step + 1
    

def Check_winner():
    global m, comb
    for i in comb:
        if len(set([m[j] for j in i])) == 1:
            return 1
    return 0

    
def Check(symb): # ищет комбинации, в которых 2 элемента уже есть
    global m, comb
    for i in comb:
        set_i = set([m[j] for j in i])
        if len(set_i) == 2 and set_i != ('O', 'X') and symb in set_i:
             for elem in range(len(i)):
                 if m[i[elem]] == i[elem] + 1:
                     return i[elem]
    return -1


def Prn(m): # печать поля по заданному массиву m
    for i in range(0, 9, 3):
        print(' ', end='')
        for j in range(3):
            print(m[i + j], end='')
            if j != 2:
                print(' | ', end='')
        if i != 6:
            print('\n---|---|---')
    print()
    return

def main():
    global m
    step_num = 1
    status = 0
    
    start = Start()
    print('Подброс монетки:', start)
    Prn(m)
    if start == 2:
        print('Ход компьютера:')
        comp_symb, user_symb = 'X', 'O'
        m[4] = 'X'
        Prn(m)
    else:
        comp_symb, user_symb = 'O', 'X'
         
    while 1:
        if Check_winner() == 1:
            print('Победитель', (step_num - 1) % 2)
            return
        else:
            if step_num % 2 == 1 or status == 1: # если ходит пользователь или игра двух пользователей
                #print('Сделайте ход: ')
                step = int(input('Сделайте ход: '))
                # проверку на дурака сделать
                m[step - 1] = user_symb
            else:
                print('Ход компьютера:', Step(comp_symb, user_symb))
        step_num += 1
        Prn(m)
                

main()
