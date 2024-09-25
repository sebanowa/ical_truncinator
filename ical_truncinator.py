import os
from datetime import datetime, timedelta

def adjust_ics_dates(input_file):
    # Erstelle den Ausgabedateinamen mit dem Suffix "-trunc"
    file_name, file_extension = os.path.splitext(input_file)
    output_file = f"{file_name}-trunc{file_extension}"

    # Öffne die .ics-Datei mit ISO-8859-1-Kodierung und lies sie Zeile für Zeile
    with open(input_file, 'r', encoding='ISO-8859-1') as file:
        lines = file.readlines()

    # Neues Array für die modifizierten Zeilen
    new_lines = []
    
    for line in lines:
        # Überprüfe, ob es sich um eine Zeile mit einem Enddatum handelt
        if line.startswith("DTEND"):
            # Extrahiere das Datum
            date_str = line.strip().split(":")[1]
            try:
                # Konvertiere das Datum in ein datetime-Objekt
                end_date = datetime.strptime(date_str, "%Y%m%d")
                # Verkürze das Datum um einen Tag
                new_end_date = end_date - timedelta(days=1)
                # Schreibe das neue Datum im ics-Format zurück
                new_line = f"DTEND:{new_end_date.strftime('%Y%m%d')}\n"
                new_lines.append(new_line)
            except ValueError:
                new_lines.append(line)
        else:
            new_lines.append(line)

    # Schreibe die modifizierten Zeilen in die neue Datei
    with open(output_file, 'w', encoding='ISO-8859-1') as file:
        file.writelines(new_lines)

    print(f"Die Datei {output_file} wurde erstellt und Enddaten wurden um einen Tag verkürzt.")

# Nutzereingabe für den Dateinamen, bereinige Leerzeichen am Anfang und Ende
input_ics = input("Bitte den Pfad zur .ics-Datei eingeben: ").strip()

# Skript ausführen
adjust_ics_dates(input_ics)