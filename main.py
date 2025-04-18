from window import Window
from line import Line
from point import Point

def main():
    win = Window(800, 600)
    p1 = Point(3, 6)
    p2 = Point(7, 11)
    win.draw_line(Line(p1, p2), "black")
    p3 = Point(25, 98)
    p4 = Point(100, 111)
    win.draw_line(Line(p3, p4), "blue")
    win.wait_for_close()

main()