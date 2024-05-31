DataType = list[list]

class Table:
    def __init__(self):
        self.cells = []
        self.max_rows = 0
        self.max_cols = 0


class DefaultCell:
    def __init__(self, value):
        self.value = value

