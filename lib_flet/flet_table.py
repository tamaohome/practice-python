# -*- coding: utf-8 -*-

import flet as ft
import pandas as pd


def read_xlsx(filepath: str):
    """Excelファイルを読み込み、ヘッダー、データ、幅を返す"""
    df = pd.read_excel(filepath)
    headers: list[str] = list(df.columns)
    data: list = df.values.tolist()
    width: list[int] = [len(str(item)) for item in headers]
    return headers, data, width


def main(page: ft.Page):
    # メイン画面のサイズを設定
    page.window_width = 600
    page.window_height = 400

    # データの読み込み
    sample_data = "sample_data/material_sample.xlsx"
    headers, data, width = read_xlsx(sample_data)

    # テーブルの作成
    columns = [ft.DataColumn(ft.Text(header)) for header in headers]
    rows = [ft.DataRow(cells=[ft.DataCell(ft.Text(str(cell))) for cell in row]) for row in data]
    table = ft.DataTable(columns=columns, rows=rows)

    # ページにテーブルを追加
    page.add(table)


if __name__ == "__main__":
    ft.app(target=main)
