import random

def get_random_word():
    words = ['python', 'java', 'javascript', 'c', 'html', 'css']
    return random.choice(words)

def display_word(word, guessed_letters):
    return ' '.join([letter if letter in guessed_letters else '_' for letter in word])

def word_guessing_game():
    word = get_random_word()
    guessed_letters = set()
    attempts = 6
    guessed_word = '_' * len(word)
    
    print("Welcome to the Word Guessing Game!")
    print(f"The word has {len(word)} letters.")
    
    while attempts > 0:
        print("\n" + display_word(word, guessed_letters))
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            print("Good guess!")
        else:
            print("Incorrect guess.")
            attempts -= 1
        
        # Check if the player has guessed all letters
        if set(word) <= guessed_letters:
            print(f"Congratulations! You've guessed the word: {word}")
            break
    else:
        print(f"Game Over! The word was: {word}")

if __name__ == "__main__":
    word_guessing_game()
