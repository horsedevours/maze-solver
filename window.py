from tkinter import Tk, BOTH, Canvas

class Window:

    def __init__(self, width, height):
        print("Initializing Window...")
        self.root = Tk()
        self.root.title = "Maze Solver"
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.canvas = Canvas(height=height, width=width, bg="white")
        self.canvas.pack()
        self.running = False
    
    def redraw(self):
        self.root.update_idletasks()
        self.root.update()
    
    def wait_for_close(self):
        self.running = True
        print(f"Running? {self.running}")
        while self.running:
            self.redraw()
    
    def close(self):
        print("Closing...")
        self.running = False
    
    def draw_line(self, line, fill_color):
        line.draw(self.canvas, fill_color)