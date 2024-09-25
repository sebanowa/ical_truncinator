from icalendar import Calendar
from datetime import timedelta
import os

# Funktion zur Abfrage des Dateipfads
def get_file_path(prompt):
    while True:
        path = input(prompt)
        if os.path.exists(path):
            return path
        else:
            print(f"Datei '{path}' nicht gefunden. Bitte erneut versuchen.")

# Pfad zur Eingabedatei abfragen
input_file = get_file_path("Bitte den Pfad zur .ics-Datei eingeben: ")

# Automatischer Ausgabedateiname mit Suffix "-trunc"
file_name, file_extension = os.path.splitext(input_file)
output_file = f"{file_name}-trunc{file_extension}"

# .ics Datei öffnen und parsen
with open(input_file, 'rb') as f:
    cal = Calendar.from_ical(f.read())

# Enddaten um einen Tag anpassen
for component in cal.walk():
    if component.name == "VEVENT" and 'DTEND' in component:
        component['DTEND'].dt = component['DTEND'].dt - timedelta(days=1)

# Angepasste Datei speichern
with open(output_file, 'wb') as f:
    f.write(cal.to_ical())

print(f"Angepasste Datei wurde als '{output_file}' gespeichert.")