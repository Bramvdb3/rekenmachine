hoofdsteden = {}
hoofdsteden['Nederland:'] = 'Amsterdam'
hoofdsteden['Duitsland:'] = 'Berlijn'
hoofdsteden['Finland:'] = 'Helsinki'
hoofdsteden['Kroatie'] = 'Zagreb'
print(hoofdsteden)

prijzen = [23, 56, 78, 34, 23, 45, 93, 12, 32, 65, 87]
halved = []

for prijs in prijzen:
    halve_prijs = prijs/2
    halved.append(halve_prijs)
print(halved)


galf = [prijs/2 for prijs in prijzen]
print(galf)
kalf = [prijs+400 for prijs in prijzen]
print(kalf)

ui = [hoofdstad+ ' hoofdstad' for hoofdstad in hoofdsteden]
print(ui)

hoofdsteden['Albanie'] = 'Tirana'
hoofdsteden['Belgie'] = 'Brussel'


