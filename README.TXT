M3U Playlist Editor
Beschreibung:

Der M3U Playlist Editor ist eine grafische Benutzeroberfläche (GUI) für die Bearbeitung von M3U-Playlisten. Dieses Python-Skript verwendet das tkinter-Modul, um eine benutzerfreundliche Anwendung zum Verwalten von M3U-Playlists bereitzustellen. Die Anwendung ermöglicht das Öffnen, Bearbeiten, Sortieren und Speichern von M3U-Dateien, die häufig für das Streaming von TV-Kanälen verwendet werden.

Funktionen:

Datei öffnen:
Öffnet eine M3U-Datei zur Bearbeitung über einen Dateiauswahldialog. Die Playlist wird in einer Listbox angezeigt.

Datei speichern:
Speichert die bearbeitete M3U-Datei über einen Speichern-Dialog.

Kanäle entfernen:
Ermöglicht das Entfernen von ausgewählten Kanälen. Die Kanäle werden aus der Listbox entfernt und die Datei entsprechend aktualisiert.

Kanäle sortieren:
Sortiert die Kanäle alphabetisch nach ihrem Namen. Die Header-Zeile #EXTM3U wird beim Sortieren ignoriert und bleibt immer an erster Stelle.

Kanal hinzufügen:
Öffnet ein Dialogfenster, in dem ein neuer Kanal mit URL und Namen hinzugefügt werden kann.

Kanal bearbeiten:
Ermöglicht das Bearbeiten der Namen von ausgewählten Kanälen.

Manuelles Sortieren:
Öffnet ein neues Fenster, in dem Kanäle per Drag-and-Drop oder mit den Pfeiltasten nach oben und unten verschoben werden können. Die Änderungen werden auf die ursprüngliche Playlist angewendet, wenn der Benutzer auf „Übernehmen“ klickt.

Kanäle automatisch auswählen:
Wählt alle Kanäle aus, deren Namen nicht „HD“ enthalten, um sie bei weiteren Aktionen wie dem Entfernen oder Bearbeiten gezielt auswählen zu können.

Technische Details:
Modul: tkinter für die GUI
Dateiformat: M3U
Features:
GUI für Dateiverwaltung und -bearbeitung
Unterstützung für die Sortierung und Bearbeitung von Kanälen
Drag-and-Drop-Unterstützung für manuelles Sortieren

Installation:
Um dieses Skript auszuführen, müssen folgende Python-Module installiert sein:
tkinter (ist standardmäßig in Python enthalten)

Verwendung:
Starten Sie das Skript: Führen Sie das Python-Skript aus, um die GUI-Anwendung zu starten.
Verwenden Sie die Buttons:
Klicken Sie auf „Open M3U“, um eine M3U-Datei zu öffnen.
Verwenden Sie „Save M3U“, um die Änderungen zu speichern.
Verwenden Sie „Remove Selected“, um ausgewählte Kanäle zu entfernen.
Verwenden Sie „Sort Channels“, um die Kanäle alphabetisch zu sortieren.
Fügen Sie neue Kanäle hinzu oder bearbeiten Sie bestehende Kanäle über die entsprechenden Buttons.
Klicken Sie auf „Sort Channels“ und verschieben Sie Kanäle nach Bedarf im neuen Fenster.

Hinweis:
Sicherstellen, dass die M3U-Dateien korrekt formatiert sind, um die beste Leistung der Anwendung zu gewährleisten.

Anleitung zur Verwendung des Python-Skripts und zur Verwaltung auf GitHub
1. Python unter Windows installieren
Python herunterladen:
https://www.python.org/downloads/

Module installieren:
Öffne die Eingabeaufforderung (CMD).
pip install tk

