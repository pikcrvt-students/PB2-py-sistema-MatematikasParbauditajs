import os


def lietotaja_definesana():
    lietotajs = ''
    while lietotajs != '1' and lietotajs != '2':
        lietotajs = input('Vai jūs esat skolotājs vai skolnieks?\n1:Skolotājs\n2:Skolnieks')
        if lietotajs == '1':
            print('Jūs iegājāt kā skolotājs')
        elif lietotajs == '2':
            print('Jūs iegājāt kā skolnieks')
    return lietotajs


def lasit_teoriju():
    Teoriju_vieta = ('Teorijas')
    pieejamas_teorijas = os.listdir(Teoriju_vieta)
    izveleta_teorija = ''
    vai_turpinat = ''
    print('Tev ir pieejamas šādas teorijas: ')
    for i in pieejamas_teorijas:
        print(i.strip('.txt'))
    while izveleta_teorija + '.txt' not in pieejamas_teorijas:
        izveleta_teorija = input('Ievadi kādas teorijas nosaukumu lai to apskatītu: ')
    faila_informacija = open('Teorijas\\'+izveleta_teorija+'.txt', 'r', encoding='utf-16')
    print(faila_informacija.read())
    faila_informacija.close()
    while vai_turpinat != '1' and vai_turpinat != '0':
        vai_turpinat = input('Vai vēlies lasit citu failu? Jā - 1 / Nē - 0 ')
    if vai_turpinat == '1':
        return True
    elif vai_turpinat == '0':
        return False
    else:
        print('Kautkas ar lasit_teoriju funkciju nav kartiba, provesim ieslegt velreiz')
        return True


def veikt_testus():
    Testu_vieta = ('Testi')
    pieejamie_testi = os.listdir(Testu_vieta)
    izveletais_tests = ''
    vai_turpinat = ''
    print('Tev ir pieejamas šādi testi: ')
    for i in pieejamie_testi:
        print(i.strip('.py'))
    while izveletais_tests + '.py' not in pieejamie_testi:
        izveletais_tests = input('Ievadi kādas teorijas nosaukumu lai to apskatītu: ')
    os.startfile('Testi\\'+izveletais_tests+'.py')
    while vai_turpinat != '1' and vai_turpinat != '0':
        vai_turpinat = input('Vai vēlies veikt citu testu? Jā - 1 / Nē - 0 ')
    if vai_turpinat == '1':
        return True
    elif vai_turpinat == '0':
        return False
    else:
        print('Kautkas ar veikt_testus funkciju nav kartiba, provesim ieslegt velreiz')
        return True

def veikt_parbaudes_darbus():
    Parbaudes_vieta = ('Parbaudes')
    pieejamas_parbaudes = os.listdir(Parbaudes_vieta)
    izveleta_parbaude = ''
    vai_turpinat = ''
    print('Tev ir pieejamas šādi testi: ')
    for i in pieejamas_parbaudes:
        print(i.strip('.py'))
    while izveleta_parbaude + '.py' not in pieejamas_parbaudes:
        izveleta_parbaude = input('Ievadi kādas teorijas nosaukumu lai to apskatītu: ')
    os.startfile('Testi\\'+izveleta_parbaude+'.py')
    while vai_turpinat != '1' and vai_turpinat != '0':
        vai_turpinat = input('Vai vēlies veikt citu testu? Jā - 1 / Nē - 0 ')
    if vai_turpinat == '1':
        return True
    elif vai_turpinat == '0':
        return False
    else:
        print('Kautkas ar veikt_testus funkciju nav kartiba, provesim ieslegt velreiz')
        return True
def apskatit_parbaudes_darbu_rezultatus():
    pass
def darbu_veidosanas_pamaciba():
    pass


while True:
    print('Labdien,')
    lietotajs = lietotaja_definesana()

    if lietotajs == '1': #Piedava skolotaja funkcijas
        while True:
            pass
    else: #Piedava skolnieka funkcijas
        while True:
            izveleta_funkcija = ''
            while izveleta_funkcija != 1 and izveleta_funkcija != 2 and izveleta_funkcija != 3:
                izveleta_funkcija = input('Jums pieejamās programmas funkcijas:\nTeorijas lasīša - 1\nTestu veikšana - 2\nPārbaudes darbu veikšana - 3\nPārbaudes darbu rezultāti - 4\nIziet no programmas - 5 ')
                if izveleta_funkcija =='1':
                    while True:
                        turpinat_teoriju = '0'
                        turpinat_teoriju = lasit_teoriju()
                        if turpinat_teoriju:
                            continue
                        else:
                            break
                elif izveleta_funkcija =='2':
                    while True:
                        turpinat_testus = '0'
                        turpinat_testus = veikt_testus()
                        if turpinat_testus:
                            continue
                        else:
                            break
                elif izveleta_funkcija =='3':
                        turpinat_parbaudes = '0'
                        turpinat_parbaudes = veikt_parbaudes_darbus()
                        if turpinat_parbaudes:
                            continue
                        else:
                            break
                elif izveleta_funkcija =='4':
                        turpinat_apskati = '0'
                        turpinat_apskati = apskatit_parbaudes_darbu_rezultatus()
                        if turpinat_apskati:
                            continue
                        else:
                            break
                elif izveleta_funkcija =='5':
                    os._exit(0)
                else:
                    print('Kautkas nebija kartiba ar jusu ievadito tekstu, izvele tiks piedavata velreiz')
                    continue


                
    os._exit(0)
        
