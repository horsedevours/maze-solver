from window import Window
from line import Line
from point import Point
from cell import Cell
from maze import Maze

def main():
    win = Window(800, 600)
    p1 = Point(3, 6)
    p2 = Point(7, 11)
    win.draw_line(Line(p1, p2), "black")
    p3 = Point(25, 98)
    p4 = Point(100, 111)
    win.draw_line(Line(p3, p4), "blue")

    c1 = Cell(25, 100, 98, 111, win)
    c1.draw()
    c2 = Cell(55, 100, 200, 300, win, False)
    c2.draw()

    m = Maze(5, 5, 20, 20, 10, 10, win)

    win.wait_for_close()

main()