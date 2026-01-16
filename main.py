import tkinter as tk
import math
from settings import *
from interface import TimerInterface

class PomodoroController:
    def __init__(self, root):
        self.root = root
        
        self.timer_mechanism = None
        self.is_running = False
        self.schedule_index = 0
        self.marks = ""

        self.ui = TimerInterface(
            root=self.root, 
            start_callback=self.start_timer, 
            reset_callback=self.reset_timer
        )

    def start_timer(self):
        if self.is_running:
            return

        self.is_running = True
        
        if self.schedule_index < len(SESSION_SCHEDULE):
            mins, mode = SESSION_SCHEDULE[self.schedule_index]
            
            if mode == "Work":
                self.ui.update_title("Work", COLOR_GREEN)
            else:
                self.ui.update_title("Break", COLOR_RED)
            
            self.count_down(mins * 60)
        else:
            self.ui.update_title("Done!", COLOR_DARK)
            self.is_running = False

    def count_down(self, count):
        # recursive timer logic
        count_min = math.floor(count / 60)
        count_sec = count % 60

        # 5 -> "05"
        if count_sec < 10:
            count_sec = f"0{count_sec}"

        self.ui.update_timer_text(f"{count_min}:{count_sec}")

        if count > 0:
            self.timer_mechanism = self.root.after(1000, self.count_down, count - 1)
        else:
            self._handle_session_complete()

    def _handle_session_complete(self):
        self.is_running = False
        
        current_mode = SESSION_SCHEDULE[self.schedule_index][1]
        if current_mode == "Work":
            self.marks += "✓"
            self.ui.update_checkmarks(self.marks)

        self.schedule_index += 1
        self.start_timer()

    def reset_timer(self):
        if self.timer_mechanism:
            self.root.after_cancel(self.timer_mechanism)
        
        # reset Logic
        self.schedule_index = 0
        self.marks = ""
        self.is_running = False
        
        # reset UI
        self.ui.update_timer_text("00:00")
        self.ui.update_title("Timer", COLOR_GREEN)
        self.ui.update_checkmarks("")

if __name__ == "__main__":
    window = tk.Tk()
    app = PomodoroController(window)
    window.mainloop()