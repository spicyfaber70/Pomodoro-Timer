import tkinter as tk
from settings import *

class TimerInterface:
    def __init__(self, root, start_callback, reset_callback):
        self.root = root
        self.root.title("Focus Timer")
        self.root.config(padx=50, pady=50, bg=COLOR_BG)
        
        self.start_callback = start_callback
        self.reset_callback = reset_callback

        self._setup_widgets()

    def _setup_widgets(self):
        self.title_label = tk.Label(text="Timer", fg=COLOR_GREEN, bg=COLOR_BG, 
                                    font=(FONT_NAME, 40, "bold"))
        self.title_label.grid(column=1, row=0)

        # circle
        self.canvas = tk.Canvas(width=300, height=300, bg=COLOR_BG, highlightthickness=0)
        self.canvas.create_oval(20, 20, 280, 280, fill=COLOR_HIGHLIGHT, outline=COLOR_DARK, width=2)
        self.canvas.create_oval(30, 30, 270, 270, fill=COLOR_BG, outline=COLOR_DARK, width=1)
        
        self.timer_text = self.canvas.create_text(150, 150, text="00:00", fill=COLOR_DARK, 
                                                  font=(FONT_NAME, 35, "bold"))
        self.canvas.grid(column=1, row=1)

        # buttons
        self.start_btn = tk.Button(text="Start", highlightthickness=0, 
                                   command=self.start_callback, font=(FONT_NAME, 10, "bold"))
        self.start_btn.grid(column=0, row=2)

        self.reset_btn = tk.Button(text="Reset", highlightthickness=0, 
                                   command=self.reset_callback, font=(FONT_NAME, 10, "bold"))
        self.reset_btn.grid(column=2, row=2)

        # checkmarks
        self.check_marks = tk.Label(text="", fg=COLOR_GREEN, bg=COLOR_BG, font=(FONT_NAME, 15, "bold"))
        self.check_marks.grid(column=1, row=3)

    
    def update_timer_text(self, text):
        self.canvas.itemconfig(self.timer_text, text=text)

    def update_title(self, text, color):
        self.title_label.config(text=text, fg=color)

    def update_checkmarks(self, marks):
        self.check_marks.config(text=marks)