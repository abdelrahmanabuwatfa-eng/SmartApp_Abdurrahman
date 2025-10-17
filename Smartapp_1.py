def Fahrenheit(temp_celcius):
    return 32 + 1.8 * temp_celcius

def gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid):
    return temp_celcius - (luchtvochtigheid / 100) * windsnelheid

def weerrapport(temp_celcius, windsnelheid, luchtvochtigheid):
    x = gevoelstemperatuur(temp_celcius, windsnelheid, luchtvochtigheid)
    if x < 0 and windsnelheid > 10:
        return "Het is heel koud en het stormt! Verwarming helemaal aan!"
    elif x < 0 and windsnelheid <= 10:
        return "Het is behoorlijk koud! Verwarming aan op de benedenverdieping!"
    elif 0 <= x < 10 and windsnelheid > 12:
        return "Het is best koud en het waait; verwarming aan en roosters dicht!"
    elif 0 <= x < 10 and windsnelheid <= 12:
        return "Het is een beetje koud, elektrische kachel op de benedenverdieping aan!"
    elif 10 <= x < 22:
        return "Heerlijk weer, niet te koud of te warm."
    else:
        return "Warm! Airco aan!"

def weerstation():
    temperaturen = []

    for dag in range(1, 8):
        t = input(f"Wat is op dag {dag} de temperatuur[C]: ")
        if t == "":
            print("bye")
            return

        temp_celcius = float(t)
        windsnelheid = float(input(f"Wat is op dag {dag} de windsnelheid[m/s]: "))
        luchtvochtigheid = float(input(f"Wat is op dag {dag} de vochtigheid[%]: "))

        temperaturen.append(temp_celcius)

        print(f"Het is {temp_celcius}C ({round(Fahrenheit(temp_celcius), 1)}F)")
        print(weerrapport(temp_celcius, windsnelheid, luchtvochtigheid))
        print(f"Gem. temp tot nu toe is {round(sum(temperaturen)/len(temperaturen), 1)}")
        print("========================================")

if __name__ == "__main__":
    weerstation()

