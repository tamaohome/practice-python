# -*- coding: utf-8 -*-

import xdwlib


def main():
    xdw_path = "sample.xdw"

    # 新しいDocuWorks文書を作成
    doc = xdwlib.Document(path=xdw_path)

    obj = xdwlib.Page(doc=doc, pos=0)  # 例として新しいページを追加
    doc.append(obj)


if __name__ == "__main__":
    main()
