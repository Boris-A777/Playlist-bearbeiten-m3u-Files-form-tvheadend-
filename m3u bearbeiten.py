import tkinter as tk
from tkinter import filedialog, Toplevel, messagebox

def load_m3u(file_path):
    """Lädt die M3U-Datei und gibt die Zeilen als Liste von Blöcken zurück."""
    with open(file_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()

    header = lines[0].strip() if lines[0].strip() == '#EXTM3U' else None
    channels = []

    for i in range(1, len(lines), 2):
        if lines[i].startswith('#EXTINF'):
            channel = (lines[i].strip(), lines[i + 1].strip())
            channels.append(channel)

    return header, channels

def save_m3u(file_path, header, channels):
    """Speichert die Kanäle in der M3U-Datei."""
    with open(file_path, 'w', encoding='utf-8') as file:
        if header:
            file.write(header + '\n')
        for channel in channels:
            file.write(channel[0] + '\n')
            file.write(channel[1] + '\n')

def update_listbox():
    """Aktualisiert die Listbox mit den Kanälen aus der channels-Liste."""
    listbox.delete(0, tk.END)
    for channel in channels:
        name = channel[0].split(',')[1].strip()
        listbox.insert(tk.END, name)

def remove_selected():
    """Entfernt die ausgewählten Kanäle aus der Liste und der Listbox."""
    selected_indices = listbox.curselection()
    if not selected_indices:
        return

    for index in sorted(selected_indices, reverse=True):
        del channels[index]

    update_listbox()

def open_file():
    """Öffnet eine M3U-Datei und lädt die Kanäle."""
    file_path = filedialog.askopenfilename(filetypes=[("M3U files", "*.m3u")])
    if file_path:
        global header, channels
        header, channels = load_m3u(file_path)
        update_listbox()

def save_file():
    """Speichert die Kanäle in eine M3U-Datei."""
    file_path = filedialog.asksaveasfilename(defaultextension=".m3u", filetypes=[("M3U files", "*.m3u")])
    if file_path:
        save_m3u(file_path, header, channels)

def open_sort_window():
    """Öffnet ein neues Fenster zum Sortieren der Kanäle per Drag-and-Drop."""
    sort_window = Toplevel(root)
    sort_window.title("Sort Channels")

    sort_listbox = tk.Listbox(sort_window, selectmode=tk.SINGLE, width=40, height=20)
    sort_listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    button_frame = tk.Frame(sort_window)
    button_frame.pack(side=tk.RIGHT, fill=tk.Y, padx=10, pady=10)

    def on_drag_start(event):
        widget = event.widget
        widget.start_index = widget.nearest(event.y)

    def on_drag_motion(event):
        widget = event.widget
        current_index = widget.nearest(event.y)
        if current_index < widget.size():
            widget.selection_clear(0, tk.END)
            widget.selection_set(current_index)

    def on_drag_drop(event):
        widget = event.widget
        end_index = widget.nearest(event.y)
        widget.selection_clear(0, tk.END)

        if end_index < widget.size():
            channel = channels.pop(widget.start_index)
            channels.insert(end_index, channel)
            update_sort_listbox()
            widget.selection_set(end_index)

    def update_sort_listbox():
        """Aktualisiert die Sortier-Listbox nach einer Verschiebung."""
        sort_listbox.delete(0, tk.END)
        for channel in channels:
            name = channel[0].split(',')[1].strip()
            sort_listbox.insert(tk.END, name)

    def apply_sorting():
        """Übernimmt die Sortierung und schließt das Fenster."""
        update_listbox()
        sort_window.destroy()

    def move_up():
        selected_indices = sort_listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            if index > 0:
                channel = channels.pop(index)
                channels.insert(index - 1, channel)
                update_sort_listbox()
                sort_listbox.selection_set(index - 1)

    def move_down():
        selected_indices = sort_listbox.curselection()
        if selected_indices:
            index = selected_indices[0]
            if index < len(channels) - 1:
                channel = channels.pop(index)
                channels.insert(index + 1, channel)
                update_sort_listbox()
                sort_listbox.selection_set(index + 1)

    sort_listbox.bind('<Button-1>', on_drag_start)
    sort_listbox.bind('<B1-Motion>', on_drag_motion)
    sort_listbox.bind('<ButtonRelease-1>', on_drag_drop)

    apply_button = tk.Button(button_frame, text="Apply", command=apply_sorting)
    apply_button.pack(side=tk.BOTTOM, pady=10)

    up_button = tk.Button(button_frame, text="Up", command=move_up)
    up_button.pack(side=tk.TOP, pady=5)

    down_button = tk.Button(button_frame, text="Down", command=move_down)
    down_button.pack(side=tk.TOP, pady=5)

    update_sort_listbox()
    sort_window.geometry("600x400")

def auto_select_non_hd():
    """Wählt automatisch alle Kanäle aus, die kein 'HD' im Namen haben."""
    listbox.selection_clear(0, tk.END)
    for index, channel in enumerate(channels):
        name = channel[0].split(',')[1].strip()
        if 'HD' not in name:
            listbox.selection_set(index)

# GUI setup
root = tk.Tk()
root.title("M3U Editor")

root.geometry("800x500")
root.minsize(600, 400)

frame = tk.Frame(root)
frame.pack(fill=tk.BOTH, expand=True, pady=10, padx=10)

listbox = tk.Listbox(frame, selectmode=tk.EXTENDED, width=40, height=20)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL)
scrollbar.config(command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

button_frame = tk.Frame(root)
button_frame.pack(pady=10)

open_button = tk.Button(button_frame, text="Open M3U", command=open_file)
open_button.pack(side=tk.LEFT, padx=5)

save_button = tk.Button(button_frame, text="Save M3U", command=save_file)
save_button.pack(side=tk.LEFT, padx=5)

remove_button = tk.Button(button_frame, text="Remove Selected", command=remove_selected)
remove_button.pack(side=tk.LEFT, padx=5)

sort_button = tk.Button(button_frame, text="Sort Channels", command=open_sort_window)
sort_button.pack(side=tk.LEFT, padx=5)

auto_select_button = tk.Button(button_frame, text="Auto-Select Non-HD", command=auto_select_non_hd)
auto_select_button.pack(side=tk.LEFT, padx=5)

root.mainloop()
