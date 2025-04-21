from cell import Cell
import time

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()

    def _create_cells(self):
        self._cells = []
        for i in range(self.num_cols):
            col = []
            for j in range(self.num_rows):
                col.append(Cell(None, None, None, None, None))
            self._cells.append(col)

        for i in range(len(self._cells)):
            for j in range(len(self._cells[i])):
                self._draw_cell(i, j)
    
    def _draw_cell(self, i, j):
        if self.win == None:
            return
        left_edge = self.x1 + (self.cell_size_x * i)
        top_edge = self.y1 + (self.cell_size_y * j)
        c = Cell(left_edge, left_edge + self.cell_size_x, top_edge, top_edge + self.cell_size_y, self.win)
        c.draw()

        self._animate()

    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.05)