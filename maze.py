from cell import Cell
import time, random

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
        seed=None
    ):
        self.x1 = x1
        self.y1 = y1
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.cell_size_x = cell_size_x
        self.cell_size_y = cell_size_y
        self.win = win
        self._create_cells()
        self._break_entrance_and_exit()
        if seed:
            random.seed(seed)
        self._break_walls_r(0, 0)

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
        self._cells[i][j] = c
        c.draw()

        self._animate()

    def _animate(self):
        if self.win == None:
            return
        self.win.redraw()
        time.sleep(0.05)

    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._cells[0][0].draw()

        self._cells[self.num_cols-1][self.num_rows-1].has_bottom_wall = False
        self._cells[self.num_cols-1][self.num_rows-1].draw()
    
    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            to_visit = []
            if i-1>0 and not self._cells[i-1][j].visited:
                to_visit.append((i-1, j))
            if i+1<self.num_cols and not self._cells[i+1][j].visited:
                to_visit.append((i+1, j))
            if j-1>0 and not self._cells[i][j-1].visited:
                to_visit.append((i, j-1))
            if j+1<self.num_rows and not self._cells[i][j+1].visited:
                to_visit.append((i, j+1))
            if not to_visit:
                self._cells[i][j].draw()
                return
            else:
                c = random.choices(to_visit)[0]
                if c[0] < i:
                    self._cells[i][j].has_left_wall = False
                    self._cells[i][j].draw()
                    self._cells[i-1][j].has_right_wall = False
                    self._cells[i-1][j].draw()
                elif c[0] > i:
                    self._cells[i][j].has_right_wall = False
                    self._cells[i][j].draw()
                    self._cells[i+1][j].has_left_wall = False
                    self._cells[i+1][j].draw()
                if c[1] < j:
                    self._cells[i][j].has_top_wall = False
                    self._cells[i][j].draw()
                    self._cells[i][j-1].has_bottom_wall = False
                    self._cells[i][j-1].draw()
                if c[1] > j:
                    self._cells[i][j].has_bottom_wall = False
                    self._cells[i][j].draw()
                    self._cells[i][j+1].has_top_wall = False
                    self._cells[i][j+1].draw()

                self._break_walls_r(c[0], c[1])