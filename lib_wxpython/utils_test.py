# -*- coding: utf-8 -*-

import os
from pprint import pprint

from .utils import *


if __name__ == "__main__":
    json_path = "sample_data/prefs.json"
    data = read_json(json_path)
    print(os.getcwd())  # 現在のディレクトリを表示
    pprint(data)
