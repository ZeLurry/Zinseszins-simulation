# Arbeitschritte des Projekts
    #  1. Grundgerüst und Berechnung
    # 2. Erste Visualisierung
    # 3. Interaktive Eingaben
    # 4. Dynamisches Diagramm und Vergleich
    # 5. Sparziel und Benutzeroberfläche
    # 6. Testing und Feinschliff

def berechne_zinseszins(startkapital, zinssatz, laufzeit):
    endkapital = startkapital * (1 + zinssatz / 100) ** laufzeit
    return endkapital


startkapital = 1000
zinssatz = 5
laufzeit = 10

endkapital = berechne_zinseszins(startkapital, zinssatz, laufzeit)

print(f"Endkapital nach {laufzeit} Jahren: {endkapital:.2f} CHF")