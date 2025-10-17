def aantal_dagen(bestand):
    try:
        f = open(bestand, "r")
        regels = f.readlines()
        f.close()
        return len(regels) - 1
    except:
        print("Bestand niet gevonden.")
        return 0


def auto_bereken(input_bestand, output_bestand):
    try:
        f = open(input_bestand, "r")
        regels = f.readlines()
        f.close()
    except:
        print("Inputbestand niet gevonden.")
        return

    resultaten = []

    for regel in regels[1:]:
        data = regel.split()
        if len(data) < 5:
            print("Onvolledige regel, gestopt.")
            return

        datum, personen, setpoint, buiten, regen = data
        try:
            personen = int(personen)
            setpoint = float(setpoint)
            buiten = float(buiten)
            regen = float(regen)
        except:
            print("Fout in data, programma gestopt.")
            return

        verschil = setpoint - buiten
        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        ventilatie = personen + 1
        if ventilatie > 4:
            ventilatie = 4

        if regen < 3:
            bewatering = True
        else:
            bewatering = False

        resultaten.append(datum + ";" + str(cv) + ";" + str(ventilatie) + ";" + str(bewatering))

    try:
        f = open(output_bestand, "w")
        for regel in resultaten:
            f.write(regel + "\n")
        f.close()
        print("Berekening opgeslagen in", output_bestand)
    except:
        print("Kon niet schrijven naar bestand.")


def waarde_aanpassen(output_bestand):
    try:
        f = open(output_bestand, "r")
        regels = f.readlines()
        f.close()
    except:
        print("Outputbestand niet gevonden. Gebruik eerst optie 2.")
        return

    datum = input("Datum die je wil aanpassen: ")
    gevonden = False

    for i in range(len(regels)):
        if regels[i].startswith(datum):
            gevonden = True
            onderdelen = regels[i].strip().split(";")
            print("1 = CV ketel, 2 = Ventilatie, 3 = Bewatering")
            keuze = input("Wat wil je aanpassen (1-3): ")

            if keuze == "1":
                nieuw = input("Nieuwe waarde CV ketel (0-100): ")
                if nieuw.isdigit() and 0 <= int(nieuw) <= 100:
                    onderdelen[1] = nieuw
                else:
                    print("Ongeldige waarde.")
                    return

            elif keuze == "2":
                nieuw = input("Nieuwe waarde ventilatie (0-4): ")
                if nieuw.isdigit() and 0 <= int(nieuw) <= 4:
                    onderdelen[2] = nieuw
                else:
                    print("Ongeldige waarde.")
                    return

            elif keuze == "3":
                nieuw = input("Nieuwe waarde bewatering (True/False): ").capitalize()
                if nieuw in ["True", "False"]:
                    onderdelen[3] = nieuw
                else:
                    print("Ongeldige waarde.")
                    return
            else:
                print("Verkeerde keuze.")
                return

            regels[i] = ";".join(onderdelen) + "\n"
            break

    if not gevonden:
        print("Datum niet gevonden.")
        return

    try:
        f = open(output_bestand, "w")
        for r in regels:
            f.write(r)
        f.close()
        print("Waarde aangepast.")
    except:
        print("Fout bij opslaan.")


def smart_app():
    input_bestand = "input.txt"
    output_bestand = "output.txt"

    while True:
        print("\n--- Smart App Controller ---")
        print("1. Aantal dagen weergeven")
        print("2. Automatisch berekenen")
        print("3. Waarde aanpassen")
        print("4. Stoppen")

        keuze = input("Kies een optie: ")

        if keuze == "1":
            dagen = aantal_dagen(input_bestand)
            print("Aantal dagen in bestand:", dagen)
        elif keuze == "2":
            auto_bereken(input_bestand, output_bestand)
        elif keuze == "3":
            waarde_aanpassen(output_bestand)
        elif keuze == "4":
            print("Programma gestopt.")
            break
        else:
            print("Ongeldige keuze.")


if __name__ == "__main__":
    smart_app()
