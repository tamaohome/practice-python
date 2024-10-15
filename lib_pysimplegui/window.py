import TkEasyGUI as eg

# ウィンドウの作成 --- (*1)
layout = [
    [eg.Text("名前を入力してください。")],
    [eg.Input("", key="-name-")],
    [eg.Button("OK"), eg.Button("キャンセル")],
]
window = eg.Window("テスト", layout=layout)

# イベントループ --- (*2)
while window.is_alive():
    # イベントと値を取得
    event, values = window.read()
    # OKボタンを押した時
    if event == "OK":
        name = values["-name-"]
        eg.popup(f"{name}が入力されました。")
        break
window.close()
