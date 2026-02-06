import tkinter as tk
from tkinter import messagebox
import random

class SamitWordGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Samit's Word Guesser")
        self.root.geometry("600x550")
        self.root.configure(bg="#1a1a2e") # Dark theme

        # Your custom data
        self.data = {
            "python": "A popular Programming language",
            "jupiter": "The largest planet in our solar system",
            "galaxy": "A massive system of stars, gas, and dust",
            "logic": "The science of reasoning and logic",
            "apple": "A fruit that originates in Kashmir",
            
            
        }

        self.reset_game()
        self.create_widgets()

    def reset_game(self):
        """Initializes or resets the game state."""
        self.secret_word = random.choice(list(self.data.keys())).lower()
        self.hint = self.data[self.secret_word]
        self.guessed_letters = []
        self.attempts = 6

    def create_widgets(self):
        """Creates all the buttons and labels."""
        # Main Title
        tk.Label(self.root, text="WORD GUESSER", font=("Impact", 32), 
                 bg="#1a1a2e", fg="#e94560").pack(pady=20)

        # Hint Display
        self.hint_label = tk.Label(self.root, text=f"HINT: {self.hint}", 
                                   font=("Arial", 12, "italic"), bg="#1a1a2e", 
                                   fg="#bdc3c7", wraplength=500)
        self.hint_label.pack(pady=10)

        # The Word Display (_ _ _ _)
        self.word_label = tk.Label(self.root, text=self.get_display_word(), 
                                   font=("Courier", 36, "bold"), bg="#1a1a2e", fg="#f1c40f")
        self.word_label.pack(pady=30)

        # Lives Counter
        self.lives_label = tk.Label(self.root, text=f"Attempts Left: {self.attempts}", 
                                    font=("Arial", 14), bg="#1a1a2e", fg="#ff4d4d")
        self.lives_label.pack()

        # Input Area
        self.input_frame = tk.Frame(self.root, bg="#1a1a2e")
        self.input_frame.pack(pady=20)

        self.entry = tk.Entry(self.input_frame, font=("Arial", 18), width=5, justify='center')
        self.entry.pack(side=tk.LEFT, padx=10)
        self.entry.bind("<Return>", lambda event: self.make_guess()) # Press Enter to play

        self.guess_btn = tk.Button(self.input_frame, text="GUESS", command=self.make_guess, 
                                   bg="#0f3460", fg="white", font=("Arial", 12, "bold"), width=10)
        self.guess_btn.pack(side=tk.LEFT)

        # History of Guessed Letters
        self.history_label = tk.Label(self.root, text="Guessed: ", font=("Arial", 10), 
                                      bg="#1a1a2e", fg="#95a5a6")
        self.history_label.pack(pady=10)

    def get_display_word(self):
        """Builds the string of underscores and guessed letters."""
        return " ".join([letter if letter in self.guessed_letters else "_" for letter in self.secret_word])

    def make_guess(self):
        guess = self.entry.get().lower().strip()
        self.entry.delete(0, tk.END)

        # Validation
        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Oops!", "Please enter a single letter.")
            return

        if guess in self.guessed_letters:
            messagebox.showinfo("Wait!", f"You already tried '{guess}'.")
            return

        self.guessed_letters.append(guess)
        self.history_label.config(text=f"Guessed: {', '.join(self.guessed_letters)}")

        if guess in self.secret_word:
            self.word_label.config(text=self.get_display_word())
            if "_" not in self.get_display_word():
                messagebox.showinfo("Winner!", f"✨ Correct! The word was: {self.secret_word.upper()}")
                self.restart_query()
        else:
            self.attempts -= 1
            self.lives_label.config(text=f"Attempts Left: {self.attempts}")
            if self.attempts == 0:
                messagebox.showerror("Game Over", f"Out of lives! The word was: {self.secret_word.upper()}")
                self.restart_query()

    def restart_query(self):
        """Ask the user if they want to play again or quit."""
        answer = messagebox.askyesno("Play Again?", "Would you like to start a new game?")
        if answer:
            self.reset_game()
            self.word_label.config(text=self.get_display_word())
            self.hint_label.config(text=f"HINT: {self.hint}")
            self.lives_label.config(text=f"Attempts Left: {self.attempts}")
            self.history_label.config(text="Guessed: ")
        else:
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    game = SamitWordGame(root)

    root.mainloop()
