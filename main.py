from Table import Table
import Cluster


if __name__ == '__main__':

    # Daten aus der Datei 'data.csv' laden und Tabelle erstellen
    tabelle = Table('data.csv', hasHeader=True)

    # Gibt die erste 5 Zeilen in der Konsole aus
    tabelle.peek(tabelle.shape[0])

    # Erstellt ein Diagramm
    tabelle.plot()
