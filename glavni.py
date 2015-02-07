__author__ = 'stevan'

import pacijenti
import tehnicari
from datetime import datetime

def proveri_datum(datum):
    try:
        datetime.strptime(datum, "%d/%m/%Y")
    except ValueError:
        print("Nepravilan format!")
        return False
    if datetime.strptime(datum, "%d/%m/%Y") > datetime.now():
        print("Unesite ispravan datum rodjenja!")
        return False

def logovanje():
    korisnicko_ime = input("Korisnicko ime >> ")
    lozinka = input("Lozinka >> ")
    return tehnicari.uloguj_se(korisnicko_ime, lozinka)

def meni():
    prikazi_meni()
    komanda = input(">> ")
    while komanda.upper() not in ('1', '2', '3', '4', '5', '6', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        prikazi_meni()
        komanda = input(">> ")
    return komanda.upper()

def prikazi_meni():
    print("\nIzaberite opciju:")
    print(" 1 - prikaz svih pacijenata")
    print(" 2 - pretraga pacijenata")
    print(" 3 - pronalazenje pacijenata po identifikatoru")
    print(" 4 - unos novog pacijenta")
    print(" 5 - brisanje pacijenta iz evidencije")
    print(" 6 - prikaz statistike")
    print(" x - prekid programa")

########################################################################################################################
## opcija 1 ##

def opcija_1():
    pacijenti.sortiraj_pacijente('id')
    pacijenti.prikazi_tabelu_pacijenata()
    komanda = '0'
    while komanda != 'X':
        komanda = meni_1()
        if komanda == '1':
            pacijenti.sortiraj_pacijente('id')
            pacijenti.prikazi_tabelu_pacijenata()
        elif komanda == '2':
            pacijenti.sortiraj_pacijente('ime')
            pacijenti.prikazi_tabelu_pacijenata()
        elif komanda == '3':
            pacijenti.sortiraj_pacijente('prezime')
            pacijenti.prikazi_tabelu_pacijenata()

def meni_1():
    prikazi_meni_1()
    komanda = input(">> ")
    while komanda.upper() not in ('1', '2', '3', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        prikazi_meni_1()
        komanda = input(">> ")
    return komanda.upper()


def prikazi_meni_1():
    print('\n[1] Izaberite opciju:')
    print(" 1 - sortiraj po identifikatoru")
    print(" 2 - sortiraj po imenu")
    print(" 3 - sortiraj po prezimenu")
    print(" x - vrati se u glavni meni")


########################################################################################################################
## opcija 2 ##

def opcija_2():
    pacijenti.sortiraj_pacijente('id')
    pacijenti.prikazi_tabelu_pacijenata()
    komanda = '0'
    while komanda != 'X':
        komanda = meni_2()
        if komanda == '1':
            vrednost = input("Unesite id za pretragu >>")
            pronadjeni = pacijenti.pretraga_pacijenata('id', vrednost)
            pacijenti.sortiraj_listu_pacijenata('id', pronadjeni)
            pacijenti.prikazi_listu_pacijenata(pronadjeni)
        elif komanda == '2':
            vrednost = input("Unesite ime za pretragu >>")
            pronadjeni = pacijenti.pretraga_pacijenata('ime', vrednost)
            pacijenti.sortiraj_listu_pacijenata('ime', pronadjeni)
            pacijenti.prikazi_listu_pacijenata(pronadjeni)
        elif komanda == '3':
            vrednost = input("Unesite prezime za pretragu>>")
            pronadjeni = pacijenti.pretraga_pacijenata('prezime', vrednost)
            pacijenti.sortiraj_listu_pacijenata('prezime', pronadjeni)
            pacijenti.prikazi_listu_pacijenata(pronadjeni)


def meni_2():
    prikazi_meni_2()
    komanda = input(">> ")
    while komanda.upper() not in ('1', '2', '3', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        prikazi_meni_2()
        komanda = input(">> ")
    return komanda.upper()

def prikazi_meni_2():
    print('\n[2] Izaberite opciju:')
    print(" 1 - pretraga po identifikatoru")
    print(" 2 - pretraga po imenu")
    print(" 3 - pretraga po prezimenu")
    print(" x - vrati se u glavni meni")


########################################################################################################################
## opcija 3 ##

def opcija_3():

    vrednost = input("\nUnesite id pacijenta >>")
    while not vrednost.isdigit() :
        vrednost = input("Nepravilan unos! Ponovite unos >>")
    pac = pacijenti.pronadji_pacijenta_po_id(vrednost)

    komanda = '0'
    while komanda != 'X':

        if pac != '':
            prikazi_sve_informacije(pac)
            komanda = meni_3()

            if komanda == '1':
                izvestaj = input("Unesite izvestaj >>")
                cena = input("Unesite cenu >>")
                pregled = str(izvestaj) + " " + str(cena);
                print(pregled)
                pac['lista_pregleda'] += " | " + pregled
                pac['zaduzenje'] += float(cena)
            elif komanda == '2':
                iznos = input("Koliko novca zelite da uplatite >>")
                if float(iznos) < pac['zaduzenje']:
                    pac['zaduzenje'] -= float(iznos)
                else:
                    kusur = float(iznos) - pac['zaduzenje']
                    pac['zaduzenje'] = 0
                    print("Vas kusur je: " + format(kusur, '.2f') + " rsd")

def meni_3():
    prikazi_meni_3()
    komanda = input(">> ")
    while komanda.upper() not in ('1', '2', 'X'):
        print("\nUneli ste pogresnu komandu.\n")
        prikazi_meni_3()
        komanda = input(">> ")
    return komanda.upper()

def prikazi_meni_3():
    print('\n[3] Izaberite opciju:')
    print(" 1 - evidencija pregleda")
    print(" 2 - evidencija placanja")
    print(" x - vrati se u glavni meni")

def prikazi_sve_informacije(pac):
    print(pacijenti.formatiraj_zaglavlje())
    print(pacijenti.formatiraj_pacijenta(pac))
    print(pacijenti.formatiraj_zaglavlje_list_pregleda())
    print(pacijenti.formatiraj_listu_pregleda(pac))


########################################################################################################################
## opcija 4 ##

def opcija_4():
    print()
    print("[4] Unos novog pacijenta\n")
    pac = {}
    pac['id'] = 0 #ovom polju ce se dodati prava vrednost naknadno

    ime = input("Unesite ime >> ")
    while len(ime) == 0:
        ime = input("Polje ne sme biti prazno. Unesite ponovo >>")
    pac['ime'] = ime;

    prezime = input("Unesite prezime >> ")
    while len(prezime) == 0:
        prezime = input("Polje ne sme biti prazno. Unesite ponovo >>")
    pac['prezime'] = prezime;

    jmbg = str(input("Unesite jmbg:"))
    while len(jmbg) != 13:
        jmbg = input("Nepravilan unos! Duzina JMBG mora biti 13! Unesite ponovo >>")
    pac['jmbg'] = jmbg

    datum = input("unesite datum rodjenja u formatu DD/MM/YYYY>>")
    while proveri_datum(datum) == False:
        datum = input("Nepravilan unos! Unesite datum u formatu DD/MM/YYYY>>")
    pac['datum_rodjenja'] = datum

    adresa = input("Unesite adresu >>")
    while len(adresa) == 0:
        adresa = input("Polje ne sme biti prazno. Unesite ponovo >>")
    pac['adresa'] = adresa

    krvna_grupa = input("Unesite krvnu grupu >> ")
    while krvna_grupa.upper() not in ('A-','A+','AB-','AB+','0-','0+','B-','B+'):
        print("Niste uneli ispravnu krvnu grupu!")
        krvna_grupa = input("Unesti krvnu grupu ponovo >>")
    pac['krvna_grupa'] = krvna_grupa.upper()

    lista_pregleda = input("Unesite listu pregleda >>")
    while len(lista_pregleda) == 0:
        lista_pregleda = input("Polje ne sme biti prazno. Unesite ponovo >>")
    pac['lista_pregleda'] = lista_pregleda

    zaduzenje = input("Unesite zaduzenje >>")
    while len(zaduzenje) == 0 or float(zaduzenje) < 0:
        if len(zaduzenje) == 0 :
            zaduzenje = input("Polje ne sme biti prazno!. Unesite ponovo >>")
        if float(zaduzenje) < 0:
            zaduzenje = input("Zaduzenje ne sme biti negativan broj. Unesite ponovo >>")

    print("zaduzenje:" + zaduzenje)
    pac['zaduzenje'] = float(zaduzenje)

    if pacijenti.dodaj_pacijenta(pac):
        print("Pacijent uspesno dodat")
        pacijenti.sacuvaj_pacijente()

########################################################################################################################
## opcija 5 ##

def opcija_5():
    pacijenti.prikazi_tabelu_pacijenata()
    id = input("\nUneti id pacijenta koga zelite da obrisite iz liste >>")
    pacijenti.obrisi_pacijenta(id)
    pacijenti.prikazi_tabelu_pacijenata()


def opcija_6():
    pac = pacijenti.pronadji_najmanje_zaduzenog()
    print("\n[6]Najmanje zaduzen je: " + pac['ime'] + " " + pac['prezime'] + \
        " i duzan je: " + format(pac['zaduzenje'], '.2f'))
    pac = pacijenti.pronadji_navise_zaduzenog()
    print("Najvise zaduzen je: " + pac['ime'] + " " + pac['prezime'] + \
        " i duzan je: " + format(pac['zaduzenje'], '.2f'))
    print("Prosecno zaduzenje: " + format(pacijenti.pronadji_prosecno_zaduzenje(), '.2f'))
    print("Ukupno zaduzenje: " + format(pacijenti.pronadji_ukupno_zaduzenje(), '.2f'))

########################################################################################################################
## MAIN ##


def main():
    tehnicari.ucitaj_tehnicare()
    pacijenti.dodaj_pacijente()
    print()
    print("Evidencija pacijenata")
    print("====================")
    print()
    if not logovanje():
        print("\nNiste uneli postojece ime i lozinku!")
        return
    komanda = '0'
    while komanda != 'X':
        komanda = meni()
        if komanda == '1':
            if pacijenti.broj_pacijenata() > 0:
                opcija_1()
            else:
                print("Nema pacijenata u bazi!")
        elif komanda == '2':
            if pacijenti.broj_pacijenata() > 0:
                opcija_2()
            else:
                print("Nema pacijenata u bazi!")
        elif komanda == '3':
            if pacijenti.broj_pacijenata() > 0:
                opcija_3()
            else:
                print("Nema pacijenata u bazi!")
        elif komanda == '4':
            opcija_4()
        elif komanda == '5':
            if pacijenti.broj_pacijenata() > 0:
                opcija_5()
            else:
                print("Nema pacijenata u bazi!")
        elif komanda == '6':
            if pacijenti.broj_pacijenata() >0:
                opcija_6()
            else:
                print("Nema pacijenata u bazi!")
        else:
            print("Kraj programa!")

if __name__ == "__main__":
    main()