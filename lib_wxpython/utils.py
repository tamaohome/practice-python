from functools import wraps
from pathlib import Path
import json
import openpyxl


def handle_exceptions(func):
    """
    try-except文を使って例外をキャッチするデコレータ
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(e)

    return wrapper


@handle_exceptions
def read_json(filepath: Path | str) -> dict[str, list]:
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"{filepath}が見つかりません")
    with filepath.open("r", encoding="utf-8") as file:
        data = json.load(file)
    return data


# xlsxファイルを読み込み、2次元配列を返す
def read_xlsx(filepath: Path | str) -> list[list]:
    filepath = Path(filepath)
    if not filepath.exists():
        raise FileNotFoundError(f"{filepath}が見つかりません")
    wb = openpyxl.load_workbook(filepath)
    ws = wb.active
    assert ws is not None

    data = []
    for row in ws.iter_rows(values_only=True):
        data.append(list(row))

    return data
