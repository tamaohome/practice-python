import TkEasyGUI as eg

import os

FILE_EXTS = [".txt", ".csv", ".xlsx", ".log", ".dfr", ".dxf"]

FONT_SETTING = ("ＭＳ ゴシック", 10)

table_header = ["ファイル名"]
file_list = []

# GUIレイアウト
layout = [
    [
        eg.Text("フォルダーを選択:", width=20, font=FONT_SETTING),
        eg.Input(key="-DIR-", width=40, font=FONT_SETTING),
        eg.FolderBrowse(),
    ],
    [
        eg.Text("拡張子を選択:", width=20, font=FONT_SETTING),
        eg.Combo(
            FILE_EXTS,
            default_value=FILE_EXTS[0],
            key="-EXTENSION-",
            enable_events=True,
            font=FONT_SETTING,
        ),
    ],
    [eg.HSeparator()],
    [
        eg.Button(" 更新 ", key="update_file_list", font=FONT_SETTING),
        eg.Button("すべて選択", key="select_all", pad=(5, 0), font=FONT_SETTING),
        eg.Button("選択解除", key="deselect_all", font=FONT_SETTING),
    ],
    [
        eg.Table(
            file_list,
            table_header,
            key="-FILE LIST-",
            font=FONT_SETTING,
            col_widths=[40],
        )
    ],
]

# ウインドウの作成
window = eg.Window("ファイル選択画面のサンプル", layout)

# イベントループ
while True:
    event, values = window.read()
    if event == eg.WINDOW_CLOSED:
        break

    if event in ["update_file_list", "-EXTENSION-"]:
        # # 更新前の選択されているアイテムのインデックスを取得
        # selected_indices = window["-FILE LIST-"].Widget.curselection()
        # # 更新前の選択されているアイテムの値を取得
        # selected_items = [window["-FILE LIST-"].Values[i] for i in selected_indices]

        folder_path = values["-DIR-"]
        file_extension = values["-EXTENSION-"]
        file_list = [
            [file] for file in os.listdir(folder_path) if file.endswith(file_extension)
        ]
        window["-FILE LIST-"].update(file_list)

        # # 更新後のリストで、以前選択されていたアイテムを再選択
        # for i, file in enumerate(file_list):
        #     if file in selected_items:
        #         window["-FILE LIST-"].Widget.selection_set(i)

    if event == "select_all":
        # window["-FILE LIST-"].update(set_to_index=all_items)
        window["-FILE LIST-"].Widget.selection_set(0, "end")

    if event == "deselect_all":
        window["-FILE LIST-"].Widget.selection_clear(0, "end")

# ウインドウを閉じる
window.close()
