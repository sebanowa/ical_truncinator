# ical_truncinator.py

Das Skript `ical_truncinator.py` ist ein Tool zum Anpassen von `.ics`-Kalenderdateien. Es verschiebt automatisch das Enddatum aller Termine um einen Tag nach vorne, um Konflikte zu vermeiden, insbesondere beim Import in überbuchte Kalendersysteme.

## Funktionen
- Verarbeitet `.ics`-Dateien und passt die Enddaten aller Termine an.
- Speichert die angepasste Kalenderdatei automatisch mit dem Suffix `-trunc` im Dateinamen.
- Stellt sicher, dass die Originaldatei nicht überschrieben wird.

## Anwendung
1. Platziere deine `.ics`-Datei im gleichen Verzeichnis wie das Skript oder gib den vollständigen Pfad an.
2. Führe das Skript im Terminal aus und gib den Dateipfad gemäß der Aufforderungen ein.
3. Das Skript erstellt eine neue `.ics`-Datei mit den angepassten Enddaten.

```bash
python3 ical_truncinator.py