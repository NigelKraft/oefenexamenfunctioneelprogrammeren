from prettytable import PrettyTable
from datetime import datetime
personeel = {
    "id_1": {"naam":"Johnny", "geslacht":"man", "afdeling":"marketing", "jaar indiensttreding":2022, "maandloon":3000},
    "id_2": {"naam":"Anne", "geslacht":"vrouw", "afdeling":"verkoop", "jaar indiensttreding":2021, "maandloon":2500},
    "id_3": {"naam":"Paulo", "geslacht":"man", "afdeling":"ontwikkeling", "jaar indiensttreding":2016, "maandloon":3500},
    "id_4": {"naam":"Robin", "geslacht":"vrouw", "afdeling":"ontwikkeling", "jaar indiensttreding":2012, "maandloon":3000},
    "id_5": {"naam":"Nomi", "geslacht":"vrouw", "afdeling":"financiën", "jaar indiensttreding":2022, "maandloon":3000},
    "id_6": {"naam":"Tomas", "geslacht":"man", "afdeling":"support", "jaar indiensttreding":2023, "maandloon":2000},
    "id_7": {"naam":"Eros", "geslacht":"man", "afdeling":"ontwikkeling", "jaar indiensttreding":2018, "maandloon":3000},
    "id_8": {"naam":"Jill", "geslacht":"vrouw", "afdeling":"marketing", "jaar indiensttreding":2018, "maandloon":2500},
    "id_9": {"naam":"Lucio", "geslacht":"man", "afdeling":"ontwikkeling", "jaar indiensttreding":2016, "maandloon":2500},
    "id_10": {"naam":"Habib", "geslacht":"man", "afdeling":"support", "jaar indiensttreding":2021, "maandloon":2000}
            }

admin = {
    "admin1": {"gebruikersnaam":"admin1", "wachtwoord":"admineen"},
    "admin2": {"gebruikersnaam":"admin2", "wachtwoord":"admintwee"}
            }

#menu#
def menu():
    print("1: toon alle info in een tabel.")
    print("2: toon alle mannen/vrouwen.")
    print("3: toon iedereen van een afdeling.")
    print("4: toon iedereen die meer verdient dan x per maand.")
    print("5: toon iedereen die langer dan x jaar in dienst is.")
    print("6: toon admin menu.")

def admin_menu():
    print("1: Voeg een personeelslid toe.")
    print("2: Voeg personeelsleden toe.")
    print("3: Verwijder een personeelslid. ")
    print("4: Verhoog loon van personeelslid")
    print("5: Verhoog alle lonen")
    print("6: Toon admins(id, naam, wachtwoord versleuteld (CeasarRotatie + 4)")
#menu#

#invoer#
def gebruikers_invoer():
    menu()
    invoer = input("geef je keuze in")
    return invoer

def gebruikers_invoer_admin():
    admin_menu()
    invoer = input("geef je keuze in")
    return invoer
#invoer#

#functies#
def dictionary_table(personeel):
    table = PrettyTable(['ID', 'Naam', 'Geslacht', 'Afdeling', 'Jaar indiensttreding', 'Maandloon'])
    for key, value in personeel.items():
        table.add_row([key, value['naam'], value['geslacht'], value['afdeling'], value['jaar indiensttreding'], value['maandloon']])
    print(table)

def mannen_en_vrouwen(personeel):
    mannen = []
    vrouwen = []
    for persoon in personeel:
        if personeel[persoon]["geslacht"] == "man":
            mannen.append(personeel[persoon]["naam"])
        elif personeel[persoon]["geslacht"] == "vrouw":
            vrouwen.append(personeel[persoon]["naam"])
    print("Mannen:", mannen)
    print("Vrouwen:", vrouwen)

def toon_persoon_afdeling(personeel):
    afdeling = input("van welke afdeling wilt u iedereen weergeven")
    for persoon in personeel.values():
        if persoon["afdeling"] == afdeling:
            for persoon in persoon.items():
                print(persoon)
            print("")

def verdiensten_per_maand(personeel):
    minimum = int(input("geef de minimun verdiensten in"))
    for persoon in personeel.values():
        if persoon["maandloon"] >= minimum:
            print(persoon["naam"],"verdient",persoon["maandloon"])

def bereken_duur_dienst(personeel):
    huidig_jaar = datetime.now().year
    duur_dienst = {}
    for key, value in personeel.items():
        naam = value["naam"]
        jaar_indiensttreding = value["jaar indiensttreding"]
        dienstduur = huidig_jaar - jaar_indiensttreding
        duur_dienst[naam] = dienstduur
    return duur_dienst

def toon_personeel_langer_dan_x_jaar(personeel):
    tijd = int(input("geef het aantal jaar dat iemand in dienst moet zitten"))
    duur_dienst = bereken_duur_dienst(personeel)
    langer_dan_x_jaar = []
    for naam, dienstduur in duur_dienst.items():
        if dienstduur > tijd:
            langer_dan_x_jaar.append(naam)
    print(langer_dan_x_jaar)
#functies#

#admin functies#
def voeg_een_persoon_toe(personeel):
    naam = input("Geef de naam van de medewerker: ")
    geslacht = input("Geef het geslacht van de medewerker: ")
    afdeling = input("Geef de afdeling van de medewerker: ")
    jaar_indiensttreding = int(input("Geef het jaar van indiensttreding van de medewerker: "))
    maandloon = int(input("Geef het maandloon van de medewerker: "))
    nieuw_id = "id_" + str(len(personeel) + 1)
    personeel[nieuw_id] = {"naam": naam, "geslacht": geslacht, "afdeling": afdeling, "jaar indiensttreding": jaar_indiensttreding, "maandloon": maandloon}
    print(dictionary_table(personeel))

def voeg_meerdere_personen_toe(personeel):
    aantal_personen = int(input("Geef het aantal personen dat je wilt toevoegen: "))
    for i in range(aantal_personen):
        naam = input("Geef de naam van de medewerker: ")
        geslacht = input("Geef het geslacht van de medewerker: ")
        afdeling = input("Geef de afdeling van de medewerker: ")
        jaar_indiensttreding = int(input("Geef het jaar van indiensttreding van de medewerker: "))
        maandloon = int(input("Geef het maandloon van de medewerker: "))
        nieuw_id = "id_" + str(len(personeel) + 1)
        personeel[nieuw_id] = {"naam": naam, "geslacht": geslacht, "afdeling": afdeling, "jaar indiensttreding": jaar_indiensttreding, "maandloon": maandloon}
    print(dictionary_table(personeel))

def verwijder_personeelslid(personeel):
    print(dictionary_table(personeel))
    personeel_id = input("wat is het personeels lid id:")
    del personeel[personeel_id]
    print("Personeels lid met ID: " + personeel_id + " is verwijderd")
    print(dictionary_table(personeel))

def verhoog_maandloon_een(personeel):
    print(dictionary_table(personeel))
    id = input("van welk id wilt u het loon verhogen:")
    bedrag = int(input("met hoeveel wilt u het loon verhogen:"))
    personeel[id]["maandloon"] += bedrag
    print(dictionary_table(personeel))

def verhoog_maandloon_meerderen(personeel):
    print(dictionary_table(personeel))
    bedrag = int(input("geef het bedrag in waarmee u de lonen wilt verhogen"))
    for personeelslid in personeel:
        personeel[personeelslid]["maandloon"] += bedrag
    print(dictionary_table(personeel))

def admin_info(admin):
    for admin_id, data in admin.items():
        gebruikersnaam = data["gebruikersnaam"]
        wachtwoord = ""
        for letter in data["wachtwoord"]:
            wachtwoord += chr(ord(letter) + 4) # caesarrotatie + 4
        print(f"Admin ID: {admin_id}, Gebruikersnaam: {gebruikersnaam}, Wachtwoord: {wachtwoord}")
#admin functies#

invoer = gebruikers_invoer()
while not invoer == "stop":
    if invoer == "1":
        dictionary_table(personeel)
    elif invoer == "2":
        mannen_en_vrouwen(personeel)
    elif invoer == "3":
        toon_persoon_afdeling(personeel)
    elif invoer == "4":
        verdiensten_per_maand(personeel)
    elif invoer == "5":
        toon_personeel_langer_dan_x_jaar(personeel)
    elif invoer == "6":
        break
    else:
        print("foutieve invoer")
    invoer = gebruikers_invoer()


while not invoer == "stop":
    print("========Admin========")
    gebruikersnaam = input("Gebruikersnaam:")
    wachtwoord = input("Wachtwoord: ")
    if gebruikersnaam in admin and admin[gebruikersnaam]["wachtwoord"] == wachtwoord:
        while not invoer == "stop":
            invoer = gebruikers_invoer_admin()
            if invoer == "1":
                voeg_een_persoon_toe(personeel)
            elif invoer == "2":
                voeg_meerdere_personen_toe(personeel)
            elif invoer == "3":
                verwijder_personeelslid(personeel)
            elif invoer == "4":
                verhoog_maandloon_een(personeel)
            elif invoer == "5":
                verhoog_maandloon_meerderen(personeel)
            elif invoer == "6":
                admin_info(admin)
            elif invoer == "stop":
                break
            else:
                print("foutieve invoer")
    else:
        print("De ingevoerde gegevens kloppen niet")

