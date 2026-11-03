# Arbeitsschritte des Projekts
    # 1. Grundgerüst und Berechnung
    # 2. Erste Visualisierung
    # 3. Interaktive Eingaben
    # 4. Dynamisches Diagramm und Vergleich
    # 5. Sparziel und Benutzeroberfläche
    # 6. Testing und Feinschliff

    # Bibliothek von Matplotlib zur Darstellung von Diagrammen
import matplotlib.pyplot as plt

# Arbeitsschritt 1: Grundgerüst und Berechnung
    # Funktion Berechnung des Endkapitals mit Zinseszins
def berechne_zinseszins(startkapital, zinssatz, laufzeit):
    endkapital = startkapital * (1 + zinssatz / 100) ** laufzeit
    return endkapital

    # Festlegung der Ausgangswerte für die Berechnung
startkapital = 1000
zinssatz = 5
laufzeit = 10

    # Funktion zur Berechnung des Endkapitals
endkapital = berechne_zinseszins(startkapital, zinssatz, laufzeit)

#Arbeitsschritt 2: Erste Visualisierung 
    # Erstellung zwei leere Listen
jahre = []
kapitalwerte = []

    # Ergebnis auf zwei Nachkommastellen gerundet
for jahr in range(laufzeit + 1):
    kapital = berechne_zinseszins(startkapital, zinssatz, jahr)

    jahre.append(jahr)
    kapitalwerte.append(kapital)

print(f"Endkapital nach {laufzeit} Jahren: {endkapital:.2f} CHF")

    # Entwicklung Kapital als Liniendiagramm
plt.plot(jahre, kapitalwerte)

    # Diagrammerstellung (Achsen, Titel, Gitternetz)
plt.title("Entwicklung des Sparguthabens")
plt.xlabel("Jahre")
plt.ylabel("Kapital in CHF")

plt.grid(True)
plt.show()