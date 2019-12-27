class Board(object):
    def __init__(self, cols, rows):
        self._cols = cols
        self._rows = rows
        self._array = []

    def get_cols(self):
        return self._cols

    def get_rows(self):
        return self._rows

    def get_array(self):
        return self._array

    def set_cols(self, rows):
        self._rows = rows

    def set_rows(self, cols):
        self._cols = cols

    def set_array(self, array):
        self._array = array
