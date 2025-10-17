import requests
from Smartapp_1 import weerstation
from Smartapp_2 import smart_app


def weer_api():
    try:
        response = requests.get(
            "https://api.open-meteo.com/v1/forecast",
            params={"latitude": 52.09, "longitude": 5.12, "current_weather": True}
        )
        temp = response.json()["current_weather"]["temperature"]
        print(f"\n De temperatuur in Utrecht is {temp}°C\n")
    except:
        print(" Fout: kan temperatuur niet ophalen.\n")



def hoofdmenu():
    while True:
        print("\n===== SMART PLATFORM =====")
        print("1. Weerstation starten (Smartapp 1)")
        print("2. Smart Home Controller starten (Smartapp 2)")
        print("3. Huidige temperatuur via API")
        print("4. Stoppen")

        keuze = input("Maak je keuze (1-4): ")

        if keuze == "1":
            weerstation()
        elif keuze == "2":
            smart_app()
        elif keuze == "3":
            weer_api()
        elif keuze == "4":
            print("Programma gestopt. Tot de volgende keer!")
            break
        else:
            print("Ongeldige keuze, probeer opnieuw.\n")

if __name__ == "__main__":
    hoofdmenu()


