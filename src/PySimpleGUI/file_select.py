import TkEasyGUI as eg

# import PySimpleGUI as sg
import os

FILE_EXTS = [".dfr", ".txt", ".csv", ".xlsx"]

# GUIレイアウト
layout = [
    [eg.Text("フォルダーを選択:")],
    [eg.Input(key="-DIR-"), eg.FolderBrowse()],
    [eg.Text("拡張子を選択:")],
    [eg.Combo(FILE_EXTS, default_value=FILE_EXTS[0], key="-EXTENSION-")],
    [eg.Button("Show Files")],
    [eg.Multiline(size=(60, 10), key="-FILE LIST-")],
]

# Create the window
window = eg.Window("File Selection", layout)

window.font = ("ＭＳ ゴシック", 16)

# Event loop
while True:
    event, values = window.read()
    if event == eg.WINDOW_CLOSED:
        break
    if event == "Show Files":
        folder_path = values["-DIR-"]
        file_extension = ".dfr"  # Change this to your desired file extension
        file_list = [
            file for file in os.listdir(folder_path) if file.endswith(file_extension)
        ]
        window["-FILE LIST-"].update("\n".join(file_list))

# Close the window
window.close()
