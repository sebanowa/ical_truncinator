# ical_truncinator.py

Das Skript `ical_truncinator.py` ist ein Tool zum Anpassen von `.ics`-Kalenderdateien. Es verschiebt automatisch das Enddatum aller Termine um einen Tag nach vorne, um Konflikte zu vermeiden, insbesondere beim Import in überbuchte Kalendersysteme.

## Funktionen
- Verarbeitet `.ics`-Dateien und passt die Enddaten aller Termine um einen Tag an.
- Fragt den Dateipfad der .ics-Datei über eine Nutzereingabe ab.
- Speichert die modifizierte Kalenderdatei automatisch mit dem Suffix `-trunc` im Dateinamen.
- Stellt sicher, dass die Originaldatei nicht überschrieben wird.

## Anwendung
1. Starte das Skript und gib den Pfad zur `.ics`-Datei ein, wenn du dazu aufgefordert wirst.
2. Das Skript erstellt eine neue `.ics`-Datei, bei der die Enddaten aller Termine um einen Tag verkürzt werden.

```bash
python3 ical_truncinator.py