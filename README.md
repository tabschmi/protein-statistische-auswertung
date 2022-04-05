# Statistische Auswertung von Proteinanalysen

Das Ziel des Programmes ist es, die statistische Auswertung von Messdaten zu automatisieren. Grundlage hierfür ist das in der Praxis alltägliche Vorgehen
unter Einhaltung der in der Statistik üblichen Berechnungsschritte und ihrer Reihenfolge. Die essentielle Voraussetzung für eine erfolgreiche Durchführung
ist eine Normalverteilung der auszuwertenden Messdaten.

Das Programm ist im Rahmen meines Praxissemesters des Studiengangs "Umweltmonitoring und forensische Chemie" entstanden, welches ich am Leibniz-Institut für
Arbeitsforschung der TU Dortmund (IfADo) durchgeführt habe. Mein persönliches Ziel hinter der Erstellung des Programmes war es, die täglich anfallenden
statistischen Auswertungen zu erleichtern und den Prozess zu automatisieren, um eine Zeitersparnis verzeichnen zu können. 
 
## Installation

Zur Vereinfachung der Installation, ist es möglich, das Programm mit `git` zu clonen und die nötigen Abhängigkeiten über `pip` zu installieren. Es wird empfohlen,
dabei `virtualenv` zu verwenden. Folgende Befehle werden benötigt, um die Installation des Programmes erfolgreich durchführen zu können:

```sh
git clone https://github.com/tabschmi/protein-statistische-auswertung.git
cd protein-statistische-auswertung
pip install -r requirements.txt
```
 
## Verwendung

Um das Programm anschließend erfolgreich ausführen zu können, muss als Argument des Befehles ein Dateipfad angegeben werden, der auf die Datei mit den
auszuwertenden Messdaten verweist. Sollte kein Dateipfad angegeben werden, erscheint eine Fehlermeldung, die darauf hinweist, das entsprechende Argument
zu ergänzen. Der Befehl zur korrekten Verwendung des Programmes sollte wie folgt aussehen:

```sh
python auswertung.py <dateipfad>
```

Nach korrektem Einlesen eines Dateipfades und damit erfolgreicher Ausführung des Programmes erscheint als Output eine tabellarische Auflistung der Proteine, bei
denen ein signifikanter Unterschied zwischen den analysierten Gruppen vorhanden ist. Als Default-Wert für den p-Wert, der das Signifikanzniveau bestimmt, ist
`p = 0.95` festgelegt. Die drei Spalten der Tabelle, die ausgegeben wird, sind mit `Protein`, `p-Value` und `Significance` benannt. Damit wird für das Protein
mit einem signifikanten Unterschied zwischen den analysierten Gruppen der Proteinname, der berechnete p-Wert und der Begriff "significant" angegeben. Für einen
genaueren Blick in die Daten und Zwischenschritte können die einzelnen Rechenschritte des Programmes durch einen Aufruf der entsprechende Variable eingesehen
werden. 
 
### Voraussetzungen Datensatz

Damit der Datensatz mit Hilfe des Programmes ausgewertet werden kann, muss die Datei bestimmte Voraussetzungen erfüllen. Hierfür ist es wichtig, dass der
Datensatz als csv-Datei vorliegt. In dieser Datei sollte eine Kopfzeile vorhanden sein, die die einzelnen Spalten mit der entsprechenden Replikatsbezeichnung
benennt. Die erste Spalte sollte die Namen der Proteine enthalten, welche vermessen wurden. Des Weiteren ist es für eine korrekte Auswertung wichtig, dass der
Datensatz normalverteilt vorliegt. Sollte dies nicht der Fall sein, müssen die Daten zunächst noch durch entsprechende Methoden normiert werden.
 
#### Testdatensatz

Um die Verwendung des Programmes zu demonstrieren und zu zeigen, wie der Datensatz aussehen sollte, wird als Beispiel ein Testdatensatz zu Verfügung gestellt.
Dieser beinhaltet lediglich beispielhafte Daten, die keiner Messung entstammen und somit keinem Muster folgen. Dieser Datensatz kann mit folgendem Befehl
ausgewertet werden:

```sh
python auswertung.py data/Testdatensatz.csv
```

Sofern der Datensatz richtig eingelesen wurde, wird als Output eine Tabelle mit lediglich einer Zeile ausgegeben. In dieser sollte der berechnete p-Wert und das
Signifikanzniveau ("significant") von "Protein_39" angezeigt werden.
