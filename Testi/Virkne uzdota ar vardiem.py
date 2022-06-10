from random import randint
def parbaude(skaitlis):
    for i in range(4):
        if int(input()) != skaitlis * (i+1):
            return False
    return True
while True:
    try:
        skaitlis = randint(3,9)
        atkartot = ''
        print('Pēteris iedomājās virkni, kuru veido skaitļa '+str(skaitlis)+' dalāmie augošā secībā.\nUzraksti pirmos četrus šīs virknes locekļus!')
        atbildes = []
        if parbaude(skaitlis):
            print('Tava piedāvātā virkne ir pareiza!')
        else:
            print('Tava piedāvātā virkne nav pareiza!')
        while atkartot != '1' and atkartot != '0':
            atkartot = input('Vai vēlies atkārtot pārbaudi? 1 - Jā, 0 - Nē ')
        if atkartot == '1':
            continue
        else:
            break
    except:
        print('Notika kļūme')
        continue

    