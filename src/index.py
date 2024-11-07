from varasto import Varasto

def lisataan_mehua(mehua):
    print("Mehu setterit:")
    print("Lisätään 50.7")
    mehua.lisaa_varastoon(50.7)
    print(f"Mehuvarasto: {mehua}")

def otetaan_mehua(mehua):
    print("Otetaan 3.14")
    mehua.ota_varastosta(3.14)
    print(f"Mehuvarasto: {mehua}")

def virhetilanteet():
    print("Virhetilanteita:")
    print("Varasto(-100.0);")
    huono = Varasto(-100.0)
    print(huono)

    print("Varasto(100.0, -50.7)")
    huono = Varasto(100.0, -50.7)
    print(huono)

def lisataan_olutta(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.lisaa_varastoon(1000.0)")
    olutta.lisaa_varastoon(1000.0)
    print(f"Olutvarasto: {olutta}")

def lisataan_mehua_neg(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.lisaa_varastoon(-666.0)")
    mehua.lisaa_varastoon(-666.0)
    print(f"Mehuvarasto: {mehua}")

def otetaan_olutta(olutta):
    print(f"Olutvarasto: {olutta}")
    print("olutta.ota_varastosta(1000.0)")
    saatiin = olutta.ota_varastosta(1000.0)
    print(f"saatiin {saatiin}")
    print(f"Olutvarasto: {olutta}")

def otetaan_mehua_neg(mehua):
    print(f"Mehuvarasto: {mehua}")
    print("mehua.otaVarastosta(-32.9)")
    saatiin = mehua.ota_varastosta(-32.9)
    print(f"saatiin {saatiin}")
    print(f"Mehuvarasto: {mehua}")


def main():
    mehua = Varasto(100.0)
    olutta = Varasto(100.0, 20.2)

    print("Luonnin jälkeen:\n"
          f"Mehuvarasto: {mehua}\n"
          f"Olutvarasto: {olutta}\n"
          "Olut getterit:\n"
          f"saldo = {olutta.saldo}\n"
          f"tilavuus = {olutta.tilavuus}\n"
          f"paljonko_mahtuu = {olutta.paljonko_mahtuu()}")

    lisataan_mehua(mehua)
    otetaan_mehua(mehua)
    virhetilanteet()
    lisataan_olutta(olutta)
    lisataan_mehua_neg(mehua)
    otetaan_olutta(olutta)
    otetaan_mehua_neg(mehua)

if __name__ == "__main__":
    main()
