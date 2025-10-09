def aantal_dagen():
    f = open("input.txt", "r")
    regels = f.readlines()
    f.close()
    dagen = len(regels) - 1
    print("Aantal dagen in het bestand is:", dagen)

def auto_bereken():
    f = open("input.txt", "r")
    regels = f.readlines()
    f.close()
    resultaten = []

    for regel in regels[1:]:
        # elke regel heeft: datum, mensen, setpoint, buiten, regen
        datum, mensen, setpoint, buiten, regen = regel.split()
        mensen = int(mensen)
        setpoint = float(setpoint)
        buiten = float(buiten)
        regen = float(regen)

        verschil = setpoint - buiten
        if verschil >= 20:
            cv = 100
        elif verschil >= 10:
            cv = 50
        else:
            cv = 0

        ventilatie = mensen + 1
        if ventilatie > 4:
            ventilatie = 4

        if regen < 3:
            bewatering = True
        else:
            bewatering = False

        resultaten.append(f"{datum};{cv};{ventilatie};{bewatering}")

    f = open("output.txt", "w")
    for r in resultaten:
        f.write(r + "\n")
    f.close()

    print("De berekeningen zijn gedaan en opgeslagen in output.txt!")


def waarde_aanpassen():
    f = open("output.txt", "r")
    regels = f.readlines()
    f.close()

    datum = input("Welke datum wil je veranderen? ")

    for i in range(len(regels)):
        if regels[i].startswith(datum):
            onderdelen = regels[i].strip().split(";")
            print("1 = CV ketel, 2 = Ventilatie, 3 = Bewatering")
            keuze = input("Wat wil je aanpassen? ")

            if keuze == "1":
                nieuw = input("Nieuwe waarde voor CV ketel: ")
                onderdelen[1] = nieuw
            elif keuze == "2":
                nieuw = input("Nieuwe waarde voor ventilatie: ")
                onderdelen[2] = nieuw
            elif keuze == "3":
                nieuw = input("Nieuwe waarde voor bewatering (True/False): ")
                onderdelen[3] = nieuw

            regels[i] = ";".join(onderdelen) + "\n"
            break

    f = open("output.txt", "w")
    for r in regels:
        f.write(r)
    f.close()

    print("De waarde is aangepast!")


def smart_app():
    while True:
        print("\n--- Smart App Controller ---")
        print("1. Aantal dagen weergeven")
        print("2. Berekenen en opslaan")
        print("3. Waarde aanpassen")
        print("4. Stoppen")

        keuze = input("Kies een optie: ")

        if keuze == "1":
            aantal_dagen()
        elif keuze == "2":
            auto_bereken()
        elif keuze == "3":
            waarde_aanpassen()
        elif keuze == "4":
            print("Programma gestopt.")
            break
        else:
            print("Verkeerde keuze, probeer opnieuw.")


if __name__ == "__main__":
    smart_app()

