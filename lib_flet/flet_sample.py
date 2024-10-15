# -*- coding: utf-8 -*-

import flet as ft


def main(page: ft.Page):
    # メイン画面のサイズを設定
    page.window_width = 400
    page.window_height = 200

    # Text Control 生成
    t = ft.Text(value="Fletの表示サンプル", color="blue", font_family="ＭＳ ゴシック")

    # ページのコントロールリストに Control を追加
    assert page.controls is not None
    page.controls.append(t)

    # ページを更新
    page.update()


if __name__ == "__main__":
    ft.app(target=main)
