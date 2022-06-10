from bdb import Breakpoint
from random import randint
import os
def parbaude(skaitlis):
    for i in range(4):
        if int(input()) != skaitlis * (i+1):
            return False
    return True
def parbaude2(nta):
    for i in range(3):
        if int(input()) !=  7 * (i+1) + nta:
            return False
    return True
def parbaude3(nta):
    for i in range(3):
        if int(input()) !=  2**(i+1) - 1:
            return False
    return True


while True:
    rezultati = []
    kvadrata_izmeri = randint(2, 20)
    nepieciesamie_serkocini = 2*kvadrata_izmeri*(kvadrata_izmeri + 1)
    nta_locekla_formula = randint(2,5)
    skolens = input('Pārbaudes darba rezultāti tiks saglabāti failā ar jūsu vārdu, kāds ir jūsu vārds? ')
    if os.path.isfile(skolens + '.txt'):
        print('Profils ir atrasts')
        skolena_fails = open(skolens + '.txt','r+')
    else:
        print('Profils nav atrasts, tika izveidots')
        skolena_fails = open(skolens + '.txt','x')
        skolena_fails.close()
        skolena_fails = open(skolens + '.txt','r+')
    print('Kvadrāta ar izmēriem 1×1 veidošanai nepieciešami 4 kociņi, kvadrāta ar izmēriem 2×2 veidošanai nepieciešami 12 kociņi, kvadrāta ar izmēriem 3×3 veidošanai nepieciešami 24 kociņi.')
    if int(input('Cik sērkociņi nepieciešami ' + str(kvadrata_izmeri) + '*' + str(kvadrata_izmeri) + ' kvadrātam?')) == nepieciesamie_serkocini:
        print('Pareizi.')
        rezultati.append('1')
    else:
        print('Nepareizi')
        rezultati.append('0')
    print('Lai izveidotu kvadrātu ar izmēriem n x n, nepieciešami ?1*n*(n+?2) sērkociņi')
    if int(input('?1: ')) == '2' and int(input('?2: ')) == '1':
        print('Pareizi.')
        rezultati.append('1')
    else:
        print('Nepareizi')
        rezultati.append('0')
    print('Uzraksti pirmos četrus virknes locekļus, ja tie ir uzdoti ar n-tā locekļa formulu an = '+ str(nta_locekla_formula) +' * n')
    if parbaude(nta_locekla_formula):
        print('Pareizi.')
        rezultati.append('1')
    else:
        print('Nepareizi')
        rezultati.append('0')
    nta_locekla_formula = randint(2,5)
    print('Uzraksti virknes an pirmos 3 locekļus, ja an = 7n + ' + str(nta_locekla_formula))
    if parbaude2(nta_locekla_formula):
        print('Pareizi.')
        rezultati.append('1')
    else:
        print('Nepareizi')
        rezultati.append('0')
    nta_locekla_formula = randint(2,5)
    print('Uzraksti pirmos četrus virknes locekļus, ja tie ir uzdoti ar n-tā locekļa formulu')
    if parbaude3(nta_locekla_formula):
        print('Pareizi.')
        rezultati.append('1')
    else:
        print('Nepareizi')
        rezultati.append('0')
    print('Tu esi pabeidzis pārbaudes darbu.')
    print('Tavi rezultāti:')
    for i in rezultati:
        print(i)
    buffer = []
    atrasts = False
    buffer = skolena_fails.read()
    buffer = buffer.splitlines()
    print(buffer)
    for i in range(len(buffer)):
        if buffer[i].startswith('VirknuParbaude'):
            for ii in range(i+1,i+len(rezultati)):
                buffer[ii] = rezultati[ii-len(rezultati)]
            atrasts = True
            break
    if atrasts == False:
        buffer.append('VirknuParbaude')
        for i in rezultati:
            buffer.append(i)
    print(buffer)
    skolena_fails.close()
    skolena_fails = open(skolens + '.txt','w')
    for i in buffer:
        skolena_fails.write('%s\n' % i)
    skolena_fails.close()
    print('Faila saglabāšana ir pabeigta.')
    break