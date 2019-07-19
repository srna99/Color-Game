import tkinter
import random


class ColorGame:

    colors = ["Red", "Yellow", "Orange", "Green", "Blue", "Purple", "Black", "Brown", "Pink", "Gray"]
    time_left = 30
    score = 0

    def __init__(self, window):

        window.title("Color Game")
        window.geometry("400x250")

        self.instruction_label = tkinter.Label(window, text="Type the color of the word, not the text!",
            font=("Arial", 14))
        self.instruction_label.pack(pady=10)

        self.start_label = tkinter.Label(window, text="Press Enter to Start.", font=("Arial", 12))
        self.start_label.pack()

        self.score_label = tkinter.Label(window, text="Score: 0", font=("Arial", 14))

        self.time_label = tkinter.Label(window, text="Time Left: " + str(self.time_left),
            font=("Arial", 14))

        self.color_text_label = tkinter.Label(window, fg=self.colors[0], text="Color", font=("Times", 40))

        self.textfield = tkinter.Entry(window, font=("Arial", 14))

        window.bind("<Return>", self.play_game)

    def play_game(self, event):

        self.start_label.pack_forget()
        self.score_label.pack()
        self.time_label.pack()
        self.color_text_label.pack()
        self.textfield.pack(fill="x", padx=100)

        self.textfield.focus_set()

        # if self.time_label == 30:
        #     self.countdown()

        self.change_color()

    def change_color(self):

        random_color = self.colors[random.randint(0, len(self.colors)-1)]
        random_color_text = self.colors[random.randint(0, len(self.colors)-1)]

        self.color_text_label.config(fg=random_color, text=random_color_text)
        self.color_text_label.pack(pady=13)

        self.check_answer(random_color)

    def check_answer(self, correct_color):

        global score

        if self.textfield.get().lower() == correct_color.lower():

            self.score += 1
            print(self.score)
            self.score_label.config(text="Score: " + str(self.score))

        self.textfield.delete(0, tkinter.END)

    def countdown(self):

        pass


# -- Main Driver Code --

new_window = tkinter.Tk()

game = ColorGame(new_window)

new_window.mainloop()
