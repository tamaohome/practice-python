# -*- coding: utf-8 -*-

from pathlib import Path
import xdwlib


def main():
    xdw_path = Path("lib_xdwlib/blank.xdw")
    assert xdw_path.exists()

    # 新しいDocuWorks文書を作成
    doc = xdwlib.Document(path=xdw_path)

    print("doc.pages:", doc.pages)
    print(type(doc.pages))

    obj = xdwlib.Page(doc=doc, pos=doc.pages)
    doc.append(obj)


if __name__ == "__main__":
    main()
