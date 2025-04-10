prijzen = [45, 23, 45, 56, 67, 23, 52, 85, 44, 99, 55, 22, 47]

auteurs = ['Johny de Mol', 'Linda de Mol', 'Kees de Mol']

def halve_prijs(prijs):
    return prijs/2
def dubbele_prijs(prijs):
    return prijs*2

def auteur(naam):
    naam = naam.split(' ')
    return naam[1] + naam[2]

auteur_functie = [auteur(naam) for naam in auteurs]
halve_prijzen_lst = [halve_prijs(prijs) for prijs in prijzen]
prijs_auteur = [halve_prijs(prijs) for prijs in halve_prijzen_lst]

hoogste_prijzen = [prijs for prijs in prijzen if prijs > 55]
print(hoogste_prijzen)


nieuwe_prijzen = []
for prijs in prijzen:
    nieuwe_prijs = 50 + prijs
    nieuwe_prijzen.append(nieuwe_prijs)

print(nieuwe_prijzen)

auto = [halve_prijs(prijs) for prijs in halve_prijzen_lst]
print(auto + 6000)




