from .config_manager import ConfigManager

from pprint import pprint

if __name__ == "__main__":
    ini_path = "config.ini"
    config = ConfigManager(ini_path)

    config.position = (100, 200)
    config.size = 300, 400

    print("ウインドウの位置:", dict(config["Window Position"]))
    print("ウインドウのサイズ:", dict(config["Window Size"]))
    print(f"上記の設定を [{config.ini_file.name}] に保存します。")

    config.save_ini()

    print("iniファイルを以下の通り保存しました。")
    print(config.ini_file.read_text())
