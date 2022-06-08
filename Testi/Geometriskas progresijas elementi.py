from random import uniform,randint

while True:
    try:
        sakumskaitlis = randint(5,200)
        kvocients = round(uniform(1,2), 1)
        rezultats = sakumskaitlis
        atkartot = ''
        print('Uzraksti ģeometriskās progresijas pirmos piecus locekļus, ja b1 = ' + str(sakumskaitlis) + ' un kvocients q = ' + str(kvocients))
        for i in range(4):
            rezultats = rezultats * kvocients
            if float(input()) != rezultats:
                print('Ievadītais numurs neietilpst progresijā')
                break
            print('Solis tika atbildēts pareizi')
        while atkartot != '1' and atkartot != '0':
            atkartot = input('Vai vēlies atkārtot pārbaudi? 1 - Jā, 0 - Nē ')
        if atkartot == '1':
            continue
        else:
            break
    except:
        continue