import random

def number_guessing_game():
    # Generate random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = 7
    
    print("Welcome to the Number Guessing Game!")
    print(f"I'm thinking of a number between 1 and 100. You have {max_attempts} attempts.")
    
    while attempts < max_attempts:
        try:
            # Get player input
            guess = int(input(f"\nAttempt {attempts + 1}/{max_attempts} - Enter your guess: "))
            attempts += 1
            
            # Check guess
            if guess == secret_number:
                print(f"🎉 Congratulations! You guessed it in {attempts} attempts!")
                return
            elif guess < secret_number:
                print("📈 Too low! Try higher.")
            else:
                print("📉 Too high! Try lower.")
                
            # Show remaining attempts
            print(f"Remaining attempts: {max_attempts - attempts}")
            
        except ValueError:
            print("❌ Please enter a valid number!")
            attempts -= 1  # Don't count invalid input as attempt
    
    print(f"\n💀 Game Over! The number was {secret_number}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
