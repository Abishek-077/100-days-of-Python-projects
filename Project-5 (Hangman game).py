import tkinter as tk
from tkinter import messagebox
import random
from collections import Counter

# List of words
someWords = '''apple banana mango strawberry orange grape pineapple apricot lemon coconut watermelon cherry papaya berry peach lychee muskmelon'''
someWords = someWords.split(' ')

# Function to choose a word
def choose_word():
    return random.choice(someWords)

# Function to update the display of the word
def update_displayed_word():
    displayed_word.set(' '.join([char if char in guessed_letters else '_' for char in word]))

# Function to handle guessing a letter
def guess_letter():
    letter = entry.get().lower()
    entry.delete(0, tk.END)
    if len(letter) != 1 or not letter.isalpha():
        messagebox.showwarning('Warning', 'Please enter a single alphabetical character.')
        return
    if letter in guessed_letters:
        messagebox.showinfo('Info', 'You have already guessed that letter.')
        return
    guessed_letters.add(letter)
    if letter in word:
        if Counter(guessed_letters) == Counter(word):
            messagebox.showinfo('Congratulations', 'You won!')
            button.config(state='disabled')
        else:
            info.set('Correct!')
    else:
        info.set('Incorrect!')
    update_displayed_word()

# Function to start a new game
def new_game():
    global word, guessed_letters
    word = choose_word()
    guessed_letters = set()
    update_displayed_word()
    info.set('Guess the word! HINT: word is a name of a Fruits ')
    button.config(state='normal')

# Main window
root = tk.Tk()
root.title('Hangman Game')
root.configure(bg='light blue')

# Variables
word = choose_word()
guessed_letters = set()
displayed_word = tk.StringVar()
info = tk.StringVar()

# Custom fonts
word_display_font = ('Helvetica', 24, 'bold')
info_font = ('Helvetica', 14)

# Layout
word_display_label = tk.Label(root, textvariable=displayed_word, font=word_display_font, bg='#f7f7f7')
word_display_label.pack(pady=20)
entry = tk.Entry(root, font=info_font)
entry.pack(pady=10)
button = tk.Button(root, text='Guess', command=guess_letter, font=info_font, bg='#8ecae6', fg='white')
button.pack(pady=5)
info_label = tk.Label(root, textvariable=info, font=info_font, bg='#f7f7f7')
info_label.pack(pady=10)
new_game_button = tk.Button(root, text='New Game', command=new_game, font=info_font, bg='#219ebc', fg='white')
new_game_button.pack(pady=20)

# Initialize game
new_game()

# Start the GUI event loop
root.mainloop()