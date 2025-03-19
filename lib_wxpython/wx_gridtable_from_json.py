# -*- coding: utf-8 -*-

"""
jsonデータをグリッドテーブルに表示
"""

import wx
import wx.grid

from utils import read_json

HeaderList = list[str]
WidthList = list[int]
CellType = str | int | float
RowType = list[CellType]
DataList = list[RowType]


class MainFrame(wx.Frame):

    header: HeaderList = []
    data: DataList = []
    width: WidthList = []

    def __init__(self, parent, title):
        super(MainFrame, self).__init__(parent, title=title, size=(600, 400))

        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.panel.SetSizer(self.sizer)

        self.grid = wx.grid.Grid(self.panel)
        self.grid_font = self.font_settings(14)
        self.grid.SetDefaultCellFont(self.grid_font)
        self.grid.SetDefaultCellAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)
        self.grid.SetDefaultRowSize(30)
        self.grid.DisableDragRowSize()
        self.grid.SetLabelFont(self.grid_font)

        self.draw_table()

    def update_table(
        self, *, header: HeaderList, data: DataList, width: WidthList = []
    ) -> None:
        """テーブルを更新する"""
        self.header = header
        self.data = data
        self.width = width

        self.grid.ClearGrid()
        self.draw_table()

    def draw_table(self) -> None:
        """テーブルを描画する"""
        # tableが空の場合は何もしない
        if not self.data:
            return

        self.grid.CreateGrid(len(self.data), len(self.header))

        # ヘッダーを追加
        for i, label in enumerate(self.header):
            self.grid.SetColLabelValue(i, label)
            # セル幅を設定
            if len(self.width) == len(self.header):
                self.grid.SetColSize(i, self.width[i])

        # セルに値を追加
        for i, row in enumerate(self.data):
            for j, value in enumerate(row):
                self.grid.SetCellValue(i, j, str(value))

        self.grid.SetColFormatNumber(2)
        self.grid.SetColFormatFloat(3, 2)

        sizer = self.panel.GetSizer()
        sizer.Add(self.grid, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)

    # !
    # def set_col_format(self) -> None:
    #     """列の表示形式を自動設定"""
    #     for i, cell in enumerate(self.data[0]):
    #         if type(cell) ==

    def font_settings(self, size=12) -> wx.Font:
        """フォント設定を返す"""
        font_name = "MS Gothic" if wx.Platform == "__WXMSW__" else "Osaka"
        return wx.Font(
            size,
            wx.FONTFAMILY_DEFAULT,
            wx.FONTSTYLE_NORMAL,
            wx.FONTWEIGHT_NORMAL,
            faceName=font_name,
        )


if __name__ == "__main__":
    json_path = "sample_data/prefs.json"
    json_data = read_json(json_path)
    assert isinstance(json_data, dict)
    header, data, width = json_data["header"], json_data["data"], json_data["width"]

    app = wx.App()
    frame = MainFrame(None, "グリッドテーブルを表示")
    frame.update_table(header=header, data=data, width=width)
    frame.Show()
    app.MainLoop()
