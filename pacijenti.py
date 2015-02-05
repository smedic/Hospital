__author__ = 'stevan'

pacijenti = []

def dodaj_pacijenta(pacijent):
    pacijenti.append(pacijent)

def obrisi_pacijenta(id):
    pacijenti.remove(id)

def pac2str(pac):
    string = ' '.join([str(pac['id']),pac['ime'], pac['prezime'], pac['jmbg'], \
                    pac['datum_rodjenja'], pac['adresa'], pac['krvna_grupa']])
    for pregled in pac['lista_pregleda']:
        string += ' '
        string += pregled
    string += ' '
    string += str(pac['zaduzenje'])
    return string

def main():

    lista_pregleda = [ 'jedan', 'dva', 'tri']

    pacijent = {
        'id' : 1,
        'ime' : 'Pera',
        'prezime' : 'Peric',
        'jmbg' : '123456',
        'datum_rodjenja' : '1.1.2001',
        'adresa' : 'Nusiceva 4',
        'krvna_grupa' : 'A-',
        'lista_pregleda': lista_pregleda,
        'zaduzenje' : 5556
    }
    dodaj_pacijenta(pacijent)
    dodaj_pacijenta(pacijent)
    dodaj_pacijenta(pacijent)

    for pac in pacijenti:
        print(pac2str(pac))


if __name__ == '__main__':
    main()


