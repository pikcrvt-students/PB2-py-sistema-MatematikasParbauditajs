from random import randint
import os

while True:
    rezultati = []
    skolens = input('Pārbaudes darba rezultāti tiks saglabāti failā ar jūsu vārdu, kāds ir jūsu vārds? ')
    if os.path.isfile(skolens + '.txt'):
        print('Profils ir atrasts')
        skolena_fails = open(skolens + '.txt','r+')
    else:
        print('Profils nav atrasts, tika izveidots')
        skolena_fails = open(skolens + '.txt','x')
        skolena_fails.close()
        skolena_fails = open(skolens + '.txt','r+')
    skaitlis_ar_kuru_dalas = randint(2,10)
    skaitlis_kuru_dala = randint(100,500)
    print('Aplūkojam visus naturālos skaitļus, kas dalās ar ' + str(skaitlis_ar_kuru_dalas))
    print('Cik skaitļa ' + str(skaitlis_ar_kuru_dalas) + ' dalāmie atrodas intervālā no 1 līdz ' + str(skaitlis_kuru_dala))
    if int(input()) == round(skaitlis_kuru_dala/skaitlis_ar_kuru_dalas):
        print('Pareizi')
        rezultati.append('1')
    else:
        print('Nepareizi')
        rezultati.append('0')
    pirma_sekunde = randint(2,10)
    katra_nakama = 9.7
    pec_cik_sekundem = randint(5,10)
    print('Koka gabals krīt no kraujas. Brīvā kritiena pirmajā sekundē tas veic ' + str(pirma_sekunde) + 'm, nākamajā par 9.7m vairāk')
    print('Aprēķini aizas dziļumu, ja koks sasniedz dibenu pēc '+ str(pec_cik_sekundem) +' sekundēm')
    if int(input()) == ((pirma_sekunde+(pirma_sekunde + (pec_cik_sekundem-1)*katra_nakama))*pec_cik_sekundem)/2:
        print('Pareizi')
        rezultati.append('1')
    else:
        print('Nepareizi')
        rezultati.append('0')
    print('Nosaki likumsakarību šajā virknē (skaitli par cik palielinās)')
    print('5 9 13 ...')
    if int(input()) == 4:
        print('Pareizi')
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
        if buffer[i].startswith('AritmetiskaParbaude'):
            for ii in range(i+1,i+len(rezultati)):
                buffer[ii] = rezultati[ii-len(rezultati)]
            atrasts = True
            break
    if atrasts == False:
        buffer.append('AritmetiskaParbaude')
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