import tkinter
import random


class ColorGame:
    _time_left = 30

    def __init__(self, window):
        window.title("Color Game")
        window.geometry("400x250")

        self._instruction_label = tkinter.Label(window, text="Type the color of the word, not the text!",
                                                font=("Arial", 14))
        self._instruction_label.pack()

        self._start_label = tkinter.Label(window, text="Press Enter to Start.", font=("Arial", 12))
        self._start_label.pack()

        # self._time_label = tkinter.Label(window, text="Time Left: " + str(self._time_left), font=("Arial", 14))
        # self._time_label.pack()


new_window = tkinter.Tk()

game = ColorGame(new_window)

new_window.mainloop()
