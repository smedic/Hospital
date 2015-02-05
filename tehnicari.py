__author__ = 'stevan'

tehnicari = []


def teh2str(teh):
    return ' '.join(teh['ime'], teh['prezime'], teh['korisnicko_ime'], teh['lozinka'])


def str2teh(red) :
    if red[-1] == '\n':
        red = red[:-1]
    ime, prezime, korisnicko_ime, lozinka = red.split(' | ')
    teh = {
        'ime': ime,
        'prezime': prezime,
        'korisnicko_ime': korisnicko_ime,
        'lozinka': lozinka
    }
    return teh


def proveri_postojanje(teh) :
    for tehnicar in tehnicari:
        if teh['korisnicko_ime'] == tehnicar['korisnicko_ime']:
            print("Tehnicar vec postoji u listi!")
            return False
    return True


def ucitaj_tehnicare():
    for red in open('tehnicari.txt', 'r').readlines():
        if len(red) > 1:
            teh = str2teh(red)
            if proveri_postojanje(teh):
                tehnicari.append(teh)


def uloguj_se(korisnicko_ime, lozinka):
    for teh in tehnicari:
        if korisnicko_ime==teh['korisnicko_ime'] and lozinka==teh['lozinka']:
            print("Uspesno ste se prijavili kao korisnik " + teh['ime'] + " " + teh['prezime'])
            return True
    return False


def main():
    ucitaj_tehnicare()

if __name__ == "__main__":
    main()
