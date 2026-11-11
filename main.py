# Arbeitsschritte des Projekts
    # 1. Grundgerüst und Berechnung         (done)
    # 2. Erste Visualisierung               (done)
    # 3. Interaktive Eingaben               (working on)
    # 4. Dynamisches Diagramm und Vergleich (working on)
    # 5. Sparziel und Benutzeroberfläche
    # 6. Testing und Feinschliff

# Bibliothek von Matplotlib zur Darstellung von Diagrammen
import matplotlib

    # Werkzeugleiste von Matplotlib ausblenden
matplotlib.rcParams["toolbar"] = "None"

import matplotlib.pyplot as plt

    # Import des Slider-Elements für interaktive Eingaben
from matplotlib.widgets import Slider

# --------------------------------------------------
# Arbeitsschritt 1: Grundgerüst und Berechnung
# --------------------------------------------------
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

# --------------------------------------------------
# Arbeitsschritt 2: Erste Visualisierung 
# --------------------------------------------------
# Erstellung zwei leere Listen
jahre = []
kapitalwerte = []

    # Ergebnis auf zwei Nachkommastellen gerundet
for jahr in range(laufzeit + 1):
    kapital = berechne_zinseszins(startkapital, zinssatz, jahr)

    # Jahr und berechneten Kapitalwert in den Listen speichern
    jahre.append(jahr)
    kapitalwerte.append(kapital)

# --------------------------------------------------
# Aufbau des Programmfensters
# --------------------------------------------------

# Grösse des gesamten Fensters festlegen
fig = plt.figure(figsize=(13, 7))

# Titel des Programmfensters
fig.canvas.manager.set_window_title("Zinseszins-Simulation")

# Titel des Programms
fig.suptitle(
    "Zinseszins erleben",
    fontsize=18,
    fontweight="bold"
)

# --------------------------------------------------
# Rechter Bereich: Diagramm
# --------------------------------------------------

# Position des Diagramms:
# [links, unten, Breite, Höhe]
ax = fig.add_axes([0.42, 0.12, 0.54, 0.78])

# Kapitalentwicklung als Linie darstellen
linie, = ax.plot(
    jahre,
    kapitalwerte,
    linewidth=2
)

# Beschriftung des Diagramms
ax.set_title("Entwicklung des Sparguthabens")
ax.set_xlabel("Jahre")
ax.set_ylabel("Kapital in CHF")

# Gitternetz zur besseren Lesbarkeit
ax.grid(True)

# --------------------------------------------------
# Linker Bereich: Werte und Slider
# --------------------------------------------------

# Überschrift des Bedienbereichs
fig.text(
    0.07,
    0.87,
    "Einstellungen",
    fontsize=15,
    fontweight="bold"
)

# --------------------------------------------------
# Startkapital
# --------------------------------------------------

fig.text(
    0.07,
    0.80,
    "Startkapital",
    fontsize=11
)

# Feld zur Anzeige des aktuellen Startkapitals
text_startkapital = fig.text(
    0.07,
    0.755,
    f"{startkapital:.0f} CHF",
    fontsize=12,
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="white",
        edgecolor="gray"
    )
)

# Bereich für den Slider des Startkapitals
achse_startkapital = fig.add_axes(
    [0.07, 0.69, 0.27, 0.035]
)

# Slider für das Startkapital
slider_startkapital = Slider(
    achse_startkapital,
    "",
    100,
    10000,
    valinit=startkapital,
    valstep=100
)

# --------------------------------------------------
# Zinssatz
# --------------------------------------------------

fig.text(
    0.07,
    0.62,
    "Zinssatz",
    fontsize=11
)

# Feld zur Anzeige des aktuellen Zinssatzes
text_zinssatz = fig.text(
    0.07,
    0.575,
    f"{zinssatz:.1f} %",
    fontsize=12,
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="white",
        edgecolor="gray"
    )
)

# Bereich für den Slider des Zinssatzes
achse_zinssatz = fig.add_axes(
    [0.07, 0.51, 0.27, 0.035]
)

# Slider für den Zinssatz
slider_zinssatz = Slider(
    achse_zinssatz,
    "",
    0,
    10,
    valinit=zinssatz,
    valstep=0.1
)

# --------------------------------------------------
# Laufzeit
# --------------------------------------------------

fig.text(
    0.07,
    0.44,
    "Laufzeit",
    fontsize=11
)

# Feld zur Anzeige der aktuellen Laufzeit
text_laufzeit = fig.text(
    0.07,
    0.395,
    f"{laufzeit} Jahre",
    fontsize=12,
    bbox=dict(
        boxstyle="round,pad=0.5",
        facecolor="white",
        edgecolor="gray"
    )
)

# Bereich für den Slider der Laufzeit
achse_laufzeit = fig.add_axes(
    [0.07, 0.33, 0.27, 0.035]
)

# Slider für die Laufzeit
slider_laufzeit = Slider(
    achse_laufzeit,
    "",
    1,
    100,
    valinit=laufzeit,
    valstep=1
)

# --------------------------------------------------
# Formel
# --------------------------------------------------

fig.text(
    0.07,
    0.255,
    "Zinseszinsformel",
    fontsize=11,
    fontweight="bold"
)

# Formel mit den momentan gewählten Werten
text_formel = fig.text(
    0.07,
    0.205,
    (
        rf"$K_{{{laufzeit}}} = "
        rf"{startkapital:.0f} \cdot "
        rf"(1 + \frac{{{zinssatz:.1f}}}{{100}})"
        rf"^{{{laufzeit}}}$"
    ),
    fontsize=13
)

# --------------------------------------------------
# Ergebnis
# --------------------------------------------------

text_ergebnis = fig.text(
    0.07,
    0.12,
    (
        f"Endkapital nach {laufzeit} Jahren:\n"
        f"{endkapital:.2f} CHF"
    ),
    fontsize=12,
    fontweight="bold"
)

# --------------------------------------------------
# Arbeitsschritt 3 / 4:
# Aktualisierung durch die Slider
# --------------------------------------------------

def aktualisiere_diagramm(wert):

    # Aktuelle Werte aus den Slidern auslesen
    neues_startkapital = slider_startkapital.val
    neuer_zinssatz = slider_zinssatz.val
    neue_laufzeit = int(slider_laufzeit.val)

    # Neue Listen für die Kapitalentwicklung
    neue_jahre = []
    neue_kapitalwerte = []

    # Kapital für jedes Jahr neu berechnen
    for jahr in range(neue_laufzeit + 1):

        kapital = berechne_zinseszins(
            neues_startkapital,
            neuer_zinssatz,
            jahr
        )

        neue_jahre.append(jahr)
        neue_kapitalwerte.append(kapital)

    # Diagrammlinie mit den neuen Werten aktualisieren
    linie.set_data(
        neue_jahre,
        neue_kapitalwerte
    )

    # Achsen an die neue Kapitalentwicklung anpassen
    ax.relim()
    ax.autoscale_view()

    # ----------------------------------------------
    # Wertefelder aktualisieren
    # ----------------------------------------------

    text_startkapital.set_text(
        f"{neues_startkapital:.0f} CHF"
    )

    text_zinssatz.set_text(
        f"{neuer_zinssatz:.1f} %"
    )

    text_laufzeit.set_text(
        f"{neue_laufzeit} Jahre"
    )

    # ----------------------------------------------
    # Formel aktualisieren
    # ----------------------------------------------

    text_formel.set_text(
        (
            rf"$K_{{{neue_laufzeit}}} = "
            rf"{neues_startkapital:.0f} \cdot "
            rf"(1 + \frac{{{neuer_zinssatz:.1f}}}{{100}})"
            rf"^{{{neue_laufzeit}}}$"
        )
    )

    # ----------------------------------------------
    # Endkapital neu berechnen
    # ----------------------------------------------

    neues_endkapital = berechne_zinseszins(
        neues_startkapital,
        neuer_zinssatz,
        neue_laufzeit
    )

    # Ergebnis im Programmfenster aktualisieren
    text_ergebnis.set_text(
        (
            f"Endkapital nach {neue_laufzeit} Jahren:\n"
            f"{neues_endkapital:.2f} CHF"
        )
    )

    # Diagramm neu zeichnen
    fig.canvas.draw_idle()

# --------------------------------------------------
# Slider mit der Aktualisierungsfunktion verbinden
# --------------------------------------------------

slider_startkapital.on_changed(
    aktualisiere_diagramm
)

slider_zinssatz.on_changed(
    aktualisiere_diagramm
)

slider_laufzeit.on_changed(
    aktualisiere_diagramm
)

# --------------------------------------------------
# Anzeige des fertigen Fensters
# --------------------------------------------------

plt.show()