import requests

def get_vehicle_info(license_plate):
    base_url = "https://opendata.rdw.nl/resource/m9d7-ebf2.json"
    params = {"kenteken": license_plate.replace("-", "").upper()}
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        data = response.json()
        if data:
            return data[0]  # Retourneer de eerste match
        else:
            return None
    else:
        response.raise_for_status()

kenteken = input("Voer het kenteken in (bijv. AB-123-C): ")
info = get_vehicle_info(kenteken)
if info:
    print(f"Merk: {info.get('merk', 'Onbekend')}")
    print(f"Handelsbenaming: {info.get('handelsbenaming', 'Onbekend')}")
    print(f"Voertuigsoort: {info.get('voertuigsoort', 'Onbekend')}")
    print(f"Eerste toelating: {info.get('datum_eerste_toelating', 'Onbekend')}")
    print(f"Aantal cilinders: {info.get('aantal_cilinders', 'Onbekend')}")
    print(f"Cilinderinhoud: {info.get('cilinderinhoud', 'Onbekend')} cc")
    print(f"Massa ledig voertuig: {info.get('massa_ledig_voertuig', 'Onbekend')} kg")
    print(f"Brandstof: {info.get('brandstof_omschrijving', 'Onbekend')}")
    print(f"CO₂-uitstoot: {info.get('co2_uitstoot_comb', 'Onbekend')} g/km")
else:
    print("Geen gegevens gevonden voor dit kenteken.")