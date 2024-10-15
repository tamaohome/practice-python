import TkEasyGUI as eg  # PySimpleGUIのラッパー

FONT_SETTING = ("ＭＳ ゴシック", 10)

header = ["NO", "CODE", "名前"]

data = [
    [1, "TEST1", "テスト1"],
    [2, "TEST2", "テスト2"],
    [3, "TEST3", "テスト3"],
    [4, "TEST4", "テスト4"],
    [5, "TEST5", "テスト5"],
    [6, "TEST6", "テスト6"],
]

layout = [
    [eg.Text("テーブルのサンプル", font=FONT_SETTING)],
    [eg.Table(data, header, font=FONT_SETTING)],
]

window = eg.Window("サンプル", layout, size=("400", 600), resizable=True)


while True:
    event, values = window.read()

    if event == None:
        break

window.close()
