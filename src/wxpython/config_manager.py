# coding: utf-8

from configparser import ConfigParser
from pathlib import Path

from .utils import handle_exceptions
from .config_items import Position, Size, ConfigItem, CoordinateType


class ConfigManager(ConfigParser):
    """
    設定ファイルを読み書きするクラス

    Attributes:
        ini_file (Path): 設定ファイルのパス
        position (Position): ウィンドウの位置
        size (Size): ウィンドウのサイズ

    Methods:
        read_ini: 設定ファイルを読み込む
        save_ini: 設定ファイルを保存する
    """

    def __init__(self, ini_path: Path | str | None = None):
        super().__init__()
        self._ini_file = self._ini_file_parser(ini_path)

        self._position = Position()
        self._size = Size()

        for item in (self._position, self._size):
            self._update_config(item)

        self.read_ini()

    def _update_config(self, item: ConfigItem) -> None:
        if not self.has_section(item.name):
            self.add_section(item.name)
        for key, value in item.items():
            self.set(item.name, key, str(value))

    @property
    def position(self) -> Position:
        return self._position

    @property
    def size(self) -> Size:
        return self._size

    @position.setter
    def position(self, xy: CoordinateType):
        self._position.update(xy)
        self._update_config(self._position)

    @size.setter
    def size(self, wh: CoordinateType):
        self._size.update(wh)
        self._update_config(self._size)

    @handle_exceptions
    def read_ini(self) -> None:
        if self.ini_file.exists():
            self.read(self.ini_file)

    @handle_exceptions
    def save_ini(self) -> None:
        with self.ini_file.open("w") as f:
            self.write(f)

    def _ini_file_parser(self, ini_path: Path | str | None = None) -> Path:
        if isinstance(ini_path, Path):
            return ini_path
        elif isinstance(ini_path, str):
            return Path(ini_path)
        else:
            return Path(__file__).with_suffix(".ini")

    @property
    def ini_file(self) -> Path:
        return self._ini_file

    @ini_file.setter
    def ini_file(self, value: Path | str):
        self._ini_file = self._ini_file_parser(value)
        self.read_ini()
