from functools import wraps
import json


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
def read_json(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return data
