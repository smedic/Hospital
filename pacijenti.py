__author__ = 'stevan'

pacijenti = []
id = 1


def broj_pacijenata():
    return len(pacijenti)


def sacuvaj_pacijente():
    file = open('pacijenti.txt', 'w')
    for pac in pacijenti:
        file.write(pac2str(pac))
        file.write('\n')
    file.close()


def dodaj_pacijenta(pacijent):
    for pac in pacijenti:
        if pac['jmbg'] == pacijent['jmbg']:
            print("Pacijent vec postoji!")
            return False
    global id
    pacijent['id']= id
    id += 1
    pacijenti.append(pacijent)
    return True

def obrisi_pacijenta(id):
    for pac in pacijenti:
        if pac['id'] == int(id):
            pacijenti.remove(pac)


def pac2str(pac):
    string = ' '.join([str(pac['id']),pac['ime'], pac['prezime'], pac['jmbg'], \
                    pac['datum_rodjenja'], pac['adresa'], pac['krvna_grupa'], \
                      pac['lista_pregleda'] , str(pac['zaduzenje']) ])
    return string


def formatiraj_zaglavlje_liste_pregleda():
    return \
        "\n Lista pregleda: \n" \
        "----------------------------------------------------------------------------------------------------"


def formatiraj_listu_pregleda(pac):
    return "{0:50}".format(pac['lista_pregleda'])


def formatiraj_pacijenta(pac):
    return "{0:5}|{1:10}|{2:12}|{3:13}|{4:11}|{5:>20}|{6:>9}|{7:>13}".format(
        str(pac['id']), pac['ime'], pac['prezime'], pac['jmbg'], pac['datum_rodjenja'], pac['adresa'], pac['krvna_grupa'],
        format(pac['zaduzenje'], '.2f') + ' rsd')


def formatiraj_zaglavlje_liste_pacijenata():
    return \
        "\nId   |   Ime    |  Prezime   |    JMBG     |Datum rodj.|      adresa        |krv.grupa| zaduzenje  \n" \
        "-----+----------+------------+-------------+-----------+--------------------+---------+-------------"


def prikazi_listu_pacijenata(lista_pacijenata):
    print(formatiraj_zaglavlje_liste_pacijenata())
    for pac in lista_pacijenata:
        print(formatiraj_pacijenta(pac))


def prikazi_tabelu_pacijenata():
    return prikazi_listu_pacijenata(pacijenti)


def sortiraj_listu_pacijenata(polje, lista_pacijenata):
    for i in range(0, len(lista_pacijenata)):
        for j in range(0, len(lista_pacijenata)):
            if lista_pacijenata[j][polje] > lista_pacijenata[i][polje]:
                lista_pacijenata[i], lista_pacijenata[j] = lista_pacijenata[j], lista_pacijenata[i]


def sortiraj_pacijente(polje):
    sortiraj_listu_pacijenata(polje, pacijenti)


def pretraga_pacijenata(polje, vrednost):
    pronadjeni = []
    for pac in pacijenti:
        str1 = str(pac[polje]).upper();
        str2 = str(vrednost).upper();
        if str2 in str1:
            pronadjeni.append(pac)
    return pronadjeni


def pronadji_pacijenta(polje, vrednost):
    for pac in pacijenti:
        if str(pac[polje]).upper() == str(vrednost).upper():
            return pac
    return ''


def pronadji_pacijenta_po_id(vrednost):
    return pronadji_pacijenta('id', vrednost)


def pronadji_najmanje_zaduzenog():
    min = pacijenti[0]
    for pac in pacijenti:
        if pac['zaduzenje'] < min['zaduzenje'] :
            min = pac
    return min

def pronadji_navise_zaduzenog():
    max = pacijenti[0]
    for pac in pacijenti:
        if pac['zaduzenje'] > max['zaduzenje'] :
            max = pac
    return max

def pronadji_prosecno_zaduzenje():
    ukupno = 0.00
    for pac in pacijenti:
        ukupno += pac['zaduzenje']
    return ukupno/float(len(pacijenti))

def pronadji_ukupno_zaduzenje():
    ukupno = 0.00
    for pac in pacijenti:
        ukupno += pac['zaduzenje']
    return ukupno

def dodaj_pacijente():

    pacijent = {
        'id' : 2,
        'ime' : 'Marko',
        'prezime' : 'Markovic',
        'jmbg' : '12345678910',
        'datum_rodjenja' : '13.11.1991',
        'adresa' : 'Nusiceva 4',
        'krvna_grupa' : 'A-',
        'lista_pregleda': 'jedan | dva | tri',
        'zaduzenje' : 460.11
    }

    pacijent2 = {
        'id' : 3,
        'ime' : 'Pera',
        'prezime' : 'Peric',
        'jmbg' : '67676544544',
        'datum_rodjenja' : '01.01.2001',
        'adresa' : '4. jula',
        'krvna_grupa' : 'A+',
        'lista_pregleda': 'jedan | dva | tri',
        'zaduzenje' : 5556.00
    }

    pacijent3 = {
        'id' : 1,
        'ime' : 'Milica',
        'prezime' : 'Markov',
        'jmbg' : '54534344444',
        'datum_rodjenja' : '11.10.2002',
        'adresa' : 'Knez Mihajlova 21',
        'krvna_grupa' : '0+',
        'lista_pregleda': 'jedan | dva | tri',
        'zaduzenje' : 643.55
    }
    dodaj_pacijenta(pacijent)
    dodaj_pacijenta(pacijent2)
    dodaj_pacijenta(pacijent3)




def main():
    dodaj_pacijente()
    obrisi_pacijenta(1)
    prikazi_tabelu_pacijenata()
    sacuvaj_pacijente()


if __name__ == '__main__':
    main()


