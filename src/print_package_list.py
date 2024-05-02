# -*- coding: utf-8 -*-

# Pythonのインストールされたパッケージ一覧を取得

import pkgutil


[print(module.name) for module in pkgutil.iter_modules()]
