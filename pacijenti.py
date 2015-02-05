__author__ = 'stevan'

pacijenti = []


def sacuvaj_pacijente():
    file = open('pacijenti.txt', 'w')
    for pac in pacijenti:
        file.write(pac2str(pac))
        file.write('\n')
    file.close()


def dodaj_pacijenta(pacijent):
    pronadjen = False
    for pac in pacijenti:
        if pac['id'] == pacijent['id'] or pac['jmbg'] == pacijent['jmbg']:
            pronadjen = True
    if not pronadjen:
        pacijenti.append(pacijent)


def obrisi_pacijenta(id):
    for pac in pacijenti:
        if pac['id'] == id:
            pacijenti.remove(pac)


def pac2str(pac):
    string = ' '.join([str(pac['id']),pac['ime'], pac['prezime'], pac['jmbg'], \
                    pac['datum_rodjenja'], pac['adresa'], pac['krvna_grupa']])
    for pregled in pac['lista_pregleda']:
        string += ' '
        string += pregled
    string += ' '
    string += str(pac['zaduzenje'])
    return string


def formatiraj_zaglavlje():
    return \
        "\nId   |   Ime    |  Prezime   |    JMBG     |Datum rodj.|      adresa        |krv.grupa| zaduzenje  \n" \
        "-----+----------+------------+-------------+-----------+--------------------+---------+-------------"


def formatiraj_pacijenta(pac):
    return "{0:5}|{1:10}|{2:12}|{3:13}|{4:11}|{5:>20}|{6:>9}|{7:>13}".format(
        str(pac['id']), pac['ime'], pac['prezime'], pac['jmbg'], pac['datum_rodjenja'], pac['adresa'], pac['krvna_grupa'],
        str(pac['zaduzenje']) + ',00 rsd')


def prikazi_tabelu_pacijenata():
    print(formatiraj_zaglavlje())
    for pac in pacijenti:
        print(formatiraj_pacijenta(pac))


def main():

    lista_pregleda = [ 'jedan', 'dva', 'tri']

    pacijent = {
        'id' : 1,
        'ime' : 'Marko',
        'prezime' : 'Markovic',
        'jmbg' : '12345678910',
        'datum_rodjenja' : '13.11.1991',
        'adresa' : 'Nusiceva 4',
        'krvna_grupa' : 'A-',
        'lista_pregleda': lista_pregleda,
        'zaduzenje' : 460
    }

    pacijent2 = {
        'id' : 2,
        'ime' : 'Pera',
        'prezime' : 'Peric',
        'jmbg' : '67676544544',
        'datum_rodjenja' : '01.01.2001',
        'adresa' : '4. jula',
        'krvna_grupa' : 'A+',
        'lista_pregleda': lista_pregleda,
        'zaduzenje' : 5556
    }

    pacijent3 = {
        'id' : 3,
        'ime' : 'Milica',
        'prezime' : 'Markov',
        'jmbg' : '54534344444',
        'datum_rodjenja' : '11.10.2002',
        'adresa' : 'Knez Mihajlova 21',
        'krvna_grupa' : '0+',
        'lista_pregleda': lista_pregleda,
        'zaduzenje' : 643
    }
    dodaj_pacijenta(pacijent)
    dodaj_pacijenta(pacijent2)
    dodaj_pacijenta(pacijent3)
    obrisi_pacijenta(1)
    prikazi_tabelu_pacijenata()

    sacuvaj_pacijente()


if __name__ == '__main__':
    main()


