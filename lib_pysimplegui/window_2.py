import TkEasyGUI as eg

layout = [[eg.Multiline("Enter your notes here:\n", size=(30, 5))], [eg.Button("Save")]]
window = eg.Window("Multiline Widget Example", layout)

while True:
    event, values = window.read()
    if event == eg.WIN_CLOSED:
        break
    if event == "Save":
        notes = values
        eg.popup(f"Notes saved:\n{notes}")

window.close()
