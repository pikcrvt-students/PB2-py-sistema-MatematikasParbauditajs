from random import randint

while True:
    try:
        inkriments = randint(5,50)
        sakuma_skaitlis = randint(5,50)
        locekla_vertiba = randint(5,50)
        atkartot = ''
        print('Dotā virkne '+ str(sakuma_skaitlis) + ' ' + str(sakuma_skaitlis+inkriments) + ' ' + str(sakuma_skaitlis+inkriments*2) + ' ' + str(sakuma_skaitlis+inkriments*3) +  ' ' + str(sakuma_skaitlis+inkriments*4) +  ' ' + '... ir aritmētiskā progresija.')
        print('Uzraksti vispārīgā locekļa formulas trūkstošos skaitļus\nan = ?1 + (n-?2)*?3')
        pirmais = input('?1 = ')
        otrais = input('?2 = ')
        tresais = input('?3 = ')
        if pirmais == str(sakuma_skaitlis) and otrais == '1' and tresais == str(inkriments):
            print('Pareizi')
            if int(input('Aprēķini ' + str(locekla_vertiba)+ ' locekla vertibu')) == sakuma_skaitlis + (locekla_vertiba - 1) * inkriments:
                print('Tests veikts pareizi ')
            else:
                print('Tests netika veikts pareizi ')
        else:
            print('Nepareizi')
        while atkartot != '1' and atkartot != '0':
            atkartot = input('Vai vēlies atkārtot pārbaudi? 1 - Jā, 0 - Nē ')
        if atkartot == '1':
            continue
        else:
            break
    except:
        continue
