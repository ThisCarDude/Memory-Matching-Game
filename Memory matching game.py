import tkinter as tk
import random

class MemoryGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Memory Matching Game")
        self.buttons = []
        self.cards = list(range(8)) * 2
        random.shuffle(self.cards)
        self.selected = []
        self.create_buttons()
        self.revealed = [False] * 16

    def create_buttons(self):
        for i in range(16):
            btn = tk.Button(self.root, text='', font=('Arial', 16), width=4, height=2,
                            command=lambda i=i: self.reveal_card(i))
            btn.grid(row=i // 4, column=i % 4)
            self.buttons.append(btn)

    def reveal_card(self, index):
        if self.revealed[index] or len(self.selected) == 2:
            return
        self.buttons[index].config(text=str(self.cards[index]), state='disabled')
        self.selected.append(index)
        if len(self.selected) == 2:
            self.root.after(1000, self.check_match)

    def check_match(self):
        i, j = self.selected
        if self.cards[i] == self.cards[j]:
            self.revealed[i] = self.revealed[j] = True
        else:
            self.buttons[i].config(text='', state='normal')
            self.buttons[j].config(text='', state='normal')
        self.selected = []
        if all(self.revealed):
            self.root.title("You Win!")

if __name__ == "__main__":
    root = tk.Tk()
    game = MemoryGame(root)
    root.mainloop()
