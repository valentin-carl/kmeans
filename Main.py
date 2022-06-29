from Table import Table
import Cluster


if __name__ == '__main__':

    # Daten aus der Datei 'data.csv' laden und Tabelle erstellen
    tabelle = Table('data/data.csv', hasHeader=True)

    # Gibt die ersten 5 Zeilen in der Konsole aus
    tabelle.peek(tabelle.shape[0])

    # Plot erstelleb
    tabelle.plot()
