import wx
import wx.grid  # Add this line to import the wx.grid module
import pandas as pd
from pathlib import Path


def read_xlsx(file_path):
    """Excelファイルを読み込み、ヘッダー、データ、幅を返す"""
    df = pd.read_excel(file_path)
    header = list(df.columns)
    data = df.values.tolist()
    width = [len(str(item)) for item in header]
    return header, data, width


class MainFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(MainFrame, self).__init__(*args, **kw)
        self.panel = wx.Panel(self)
        self.grid = wx.grid.Grid(self.panel)
        self.grid.CreateGrid(0, 0)
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.grid, 1, wx.EXPAND)
        self.panel.SetSizer(sizer)

    def update_table(self, header, data, width):
        self.grid.ClearGrid()
        self.grid.AppendCols(len(header))
        self.grid.AppendRows(len(data))
        for col, col_label in enumerate(header):
            self.grid.SetColLabelValue(col, col_label)
            self.grid.SetColSize(col, width[col])
        for row, row_data in enumerate(data):
            for col, value in enumerate(row_data):
                self.grid.SetCellValue(row, col, str(value))


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
    xlsx_path = Path("/sample_data/material.sample.xlsx")
    assert xlsx_path.exists()
    header, data, width = read_xlsx(xlsx_path)

    app = wx.App()
    frame = MainFrame(None, "グリッドテーブルを表示")
    frame.update_table(header=header, data=data, width=width)
    frame.Show()
    app.MainLoop()
