## k-Means Clustering

### Einrichten

#### Repository herunterladen und virtual environment aktivieren

```{shell}
git clone git@github.com:valentin-carl/kmeans.git
cd kmeans
```

#### virtual environment aktivieren
```{shell}
virtualenv venv
source venv/bin/activate
pip install -r requirements
```

### k-Means benutzen

In der Datei `Clustering.py`, unter `if __name__ == "__name__:"` finden sich die Funktionsaufrufe, um die k-Means-Funktion zu verwenden. Es kann die Datei `data.csv` nach Belieben angepassen/ausgetauscht werden. In der `main` lässt sich dann die Anzahl der Cluster angeben, das Ergebnis wird automatisch geplottet. Nächste Schritten wären beispielweise, die Distanz- oder Stopfunktion anzupassen.

----

> Bei Fehlern bitte Nachricht an [v.carl@campus.tu-berlin.de](mailto::v.carl@campus.tu-berlin.de)
