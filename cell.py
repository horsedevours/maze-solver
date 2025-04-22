from point import Point
from line import Line

class Cell:
    def __init__(self, x1, x2, y1, y2, window=None, has_right_wall=True, has_left_wall=True, has_bottom_wall=True, has_top_wall=True):
        self.has_right_wall = has_right_wall
        self.has_left_wall = has_left_wall
        self.has_bottom_wall = has_bottom_wall
        self.has_top_wall = has_top_wall
        self._x1 = x1
        self._x2 = x2
        self._y1 = y1
        self._y2 = y2
        self._w = window
        self.visited = False
    
    def draw(self):
        upper_left = Point(self._x1, self._y1)
        upper_right = Point(self._x2, self._y1)
        lower_left = Point(self._x1, self._y2)
        lower_right = Point(self._x2, self._y2)
        if self.has_bottom_wall:
            self._w.draw_line(Line(lower_left, lower_right), "blue")
        else:
            self._w.draw_line(Line(lower_left, lower_right), "white")
        if self.has_left_wall:
            self._w.draw_line(Line(upper_left, lower_left), "blue")
        else:
            self._w.draw_line(Line(upper_left, lower_left), "white")
        if self.has_right_wall:
            self._w.draw_line(Line(upper_right, lower_right), "blue")
        else:
            self._w.draw_line(Line(upper_right, lower_right), "white")
        if self.has_top_wall:
            self._w.draw_line(Line(upper_left, upper_right), "blue")
        else:
            self._w.draw_line(Line(upper_left, upper_right), "white")
    
    def draw_move(self, to_cell, undo=False):
        color = "red"
        if undo:
            color = "gray"
        self._w.draw_line(Line(self.mid_point(), to_cell.mid_point()), color)
    
    def mid_point(self):
        mid_x = (self._x1 + self._x2) / 2
        mid_y = (self._y1 + self. _y2) / 2
        return Point(mid_x, mid_y)