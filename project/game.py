# Project Overview:
# Your task is to create a text-based Wordle game where players attempt to guess a hidden 
# word within a limited number of attempts in a file named `wordle.py`. Check out the inspiration/blueprint for this Milestone project here and try the game out yourself first.

# Objective: Create a game where players have to guess a 5-letter word within 6 attempts.

# Game Rules:
# - The computer selects a random word from a predefined list of 5-letter words.
# - The player has 6 attempts to guess the hidden word.
# - After each guess, the game provides feedback on the correctness of the guess:
# 	- Letters that are in the correct position are marked in green.
# 	- Letters that are in the word but not in the correct position are marked in yellow.
# 	- Letters that are not in the word i.e. not in any spot are marked in red.
# Game Flow:
# - Display instructions on how to play the game.
# - Display the wordle board and keyboard.
# - Prompt the player to enter a 5-letter word guess.
# - Provide feedback on the guess and update the wordle board and keyboard.
# - Continue the game until the player guesses the word correctly or runs out of attempts.

# Game Setup:
# - Create a 6x5 board to represent the wordle board.
# - Create a keyboard layout to display the letters and their current state (untried, correct position, incorrect position). The keyboard layout will not actually be used to enter input, it simply shows the letters that have been tried or untried and their current state.
# - Choose a random 5-letter word for the player to guess.

# Tips:
# - Use the tabulate library to display the board in a tabular form.
# - Use the termcolor library to color text green, red, or yellow in the terminal.
# - You can re-print the board (6X5 table) on the terminal each time you collect
#   the player’s guess to show the updated game state.

# Pro-tip: You need to look up how to install Python packages using pip.
# Bonus point if you can install them in a virtual environment.
# Check the next slide for installation steps.


# Wordle Bank: Here is a list of 5-letter words you can user_input for the wordle game. Simply copy the contents of the file and user_input it in your code as is.

# Setting things up:
# Since you would be using third-party libraries for this milestone project, 
# you are advised to create and activate a virtual environment. 
# Read this article for how to do so and why it is advisable (You can ignore the `requirements.txt` part in the article).
# With your virtual environment activated and an active internet connection, run the following command in the terminal: 
# `pip install termcolor tabulate`
# Add the following imports to the top of your wordle.py file:
# `from tabulate import tabulate`
# `from termcolor import colored`
# You are now ready to user_input the libraries in building the game. Here is an example of how to user_input the libraries:
# print(colored(text, ‘red’, attrs=["bold"]))  # termcolor

# wordle_board = [['', '', '', '', ''] for _ in range(6)]  # create 6X5 grid
# board_tabulated = tabulate(wordle_board, tablefmt="heavy_grid")  # tabulate
# print(board_tabulated)
# Now you can color text and create nicely formatted tables with python!
# 





import random
from termcolor import colored



wordle_bank = ["About", "Alert", "Argue", "Beach", "Above", "Alike", "Arise", "Began", "Abuse", "Alive", "Array", "Begin", "Actor", "Allow", "Aside", "Begun", "Acute", "Alone", "Asset", "Being", "Admit", "Along", "Audio", "Below", "Adopt", "Alter", "Audit", "Bench", "Adult", "Among", "Avoid", "Billy", "After", "Anger", "Award", "Birth", "Again", "Angle", "Aware", "Black", "Agent", "Angry", "Badly", "Blame", "Agree", "Apart", "Baker", "Blind", "Ahead", "Apple", "Bases", "Block", "Alarm", "Apply", "Basic", "Blood", "Album", "Arena", "Basis", "Board", "Boost", "Buyer", "China", "Cover", "Booth", "Cable", "Chose", "Craft", "Bound", "Calif", "Civil", "Crash", "Brain", "Carry", "Claim", "Cream", "Brand", "Catch", "Class", "Crime", "Bread", "Cause", "Clean", "Cross", "Break", "Chain", "Clear", "Crowd", "Breed", "Chair", "Click", "Crown", "Brief", "Chart", "Clock", "Curve", "Bring", "Chase", "Close", "Cycle", "Broad", "Cheap", "Coach", "Daily", "Broke", "Check", "Coast", "Dance", "Brown", "Chest", "Could", "Dated", "Build", "Chief", "Count", "Dealt", "Built", "Child", "Court", "Death", "Debut", "Entry", "Forth", "Group", "Delay", "Equal", "Forty", "Grown", "Depth", "Error", "Forum", "Guard", "Doing", "Event", "Found", "Guess", "Doubt", "Every", "Frame", "Guest", "Dozen", "Exact", "Frank", "Guide", "Draft", "Exist", "Fraud", "Happy", "Drama", "Extra", "Fresh", "Harry", "Drawn", "Faith", "Front", "Heart", "Dream", "False", "Fruit", "Heavy", "Dress", "Fault", "Fully", "Hence", "Drill", "Fibre", "Funny", "Night", "Drink", "Field", "Giant", "Horse", "Drive", "Fifth", "Given", "Hotel", "Drove", "Fifty", "Glass", "House", "Dying", "Fight", "Globe", "Human", "Eager", "Final", "Going", "Ideal", "Early", "First", "Grace", "Image", "Earth", "Fixed", "Grade", "Index", "Eight", "Flash", "Grand", "Inner", "Elite", "Fleet", "Grant", "Input", "Empty", "Floor", "Grass", "Issue", "Enemy", "Fluid", "Great", "Irony", "Enjoy", "Focus", "Green", "Juice", "Enter", "Force", "Gross", "Joint", "Judge", "Metal", "Media", "Newly", "Known", "Local", "Might", "Noise", "Label", "Logic", "Minor", "North", "Large", "Loose", "Minus", "Noted", "Laser", "Lower", "Mixed", "Novel", "Later", "Lucky", "Model", "Nurse", "Laugh", "Lunch", "Money", "Occur", "Layer", "Lying", "Month", "Ocean", "Learn", "Magic", "Moral", "Offer", "Lease", "Major", "Motor", "Often", "Least", "Maker", "Mount", "Order", "Leave", "March", "Mouse", "Other", "Legal", "Music", "Mouth", "Ought", "Level", "Match", "Movie", "Paint", "Light", "Mayor", "Needs", "Paper", "Limit", "Meant", "Never", "Party", "Peace", "Power", "Radio", "Round", "Panel", "Press", "Raise", "Route", "Phase", "Price", "Range", "Royal", "Phone", "Pride", "Rapid", "Rural", "Photo", "Prime", "Ratio", "Scale", "Piece", "Print", "Reach", "Scene", "Pilot", "Prior", "Ready", "Scope", "Pitch", "Prize", "Refer", "Score", "Place", "Proof", "Right", "Sense", "Plain", "Proud", "Rival", "Serve", "Plane", "Prove", "River", "Seven", "Plant", "Queen", "Quick", "Shall", "Plate", "Sixth", "Stand", "Shape", "Point", "Quiet", "Roman", "Share", "Pound", "Quite", "Rough", "Sharp", "Sheet", "Spare", "Style", "Times", "Shelf", "Speak", "Sugar", "Tired", "Shell", "Speed", "Suite", "Title", "Shift", "Spend", "Super", "Today", "Shirt", "Spent", "Sweet", "Topic", "Shock", "Split", "Table", "Total", "Shoot", "Spoke", "Taken", "Touch", "Short", "Sport", "Taste", "Tough", "Shown", "Staff", "Taxes", "Tower", "Sight", "Stage", "Teach", "Track", "Since", "Stake", "Teeth", "Trade", "Sixty", "Start", "Texas", "Treat", "Sized", "State", "Thank", "Trend", "Skill", "Steam", "Theft", "Trial", "Sleep", "Steel", "Their", "Tried", "Slide", "Stick", "Theme", "Tries", "Small", "Still", "There", "Truck", "Smart", "Stock", "These", "Truly", "Smile", "Stone", "Thick", "Trust", "Smith", "Stood", "Thing", "Truth", "Smoke", "Store", "Think", "Twice", "Solid", "Storm", "Third", "Under", "Solve", "Story", "Those", "Undue", "Sorry", "Strip", "Three", "Union", "Sound", "Stuck", "Threw", "Unity", "South", "Study", "Throw", "Until", "Space", "Stuff", "Tight", "Upper", "Upset", "Whole", "Waste", "Wound", "Urban", "Whose", "Watch", "Write", "Usage", "Woman", "Water", "Wrong", "Usual", "Train", "Wheel", "Wrote", "Valid", "World", "Where", "Yield", "Value", "Worry", "Which", "Young", "Video", "Worse", "While", "Youth", "Virus", "Worst", "White", "Worth", "Visit", "Would", "Vital", "Voice"]





    


def play_game():
        secret_word = list(wordle_bank.pop(random.randint(0, len(wordle_bank))).lower())
        print(secret_word)
        attempts_left = 6
        
        for attempt in range(attempts_left):
            attempts_left -= 1
            
            
            guess = list(input("\nEnter your guess: ").strip().lower())
            if len(guess) != len(secret_word):
                print(f"Guess must be {len(secret_word)} letters long")
            
            

            if guess == secret_word:
                print(colored("\n🎉 Congratulations! You've won! 🎉", 'green'))
                print(f"\nYou won in {attempt + 1} attempts!")
                break
                


            if attempts_left == 0:
                print(colored(f"\nGame Over! The word was: {secret_word.upper()}", 'red'))
                break
            
            for i in range(len(secret_word)):
                if guess[i] not in secret_word:
                    guess[i] = colored(guess[i], "red")
                if guess[i] != secret_word[i]:
                    guess[i] = colored(guess[i], "yellow")
                    
                guess[i] = colored(guess[i], "green")
                
            print("".join(guess))
                

def main():
    print("Welcome to Wordle!")
    print("Try to guess the 5-letter word.")
    print("Green = Correct letter, correct spot")
    print("Yellow = Correct letter, wrong spot")
    print("Red = Letter not in word")
    
    
    play_game()
                


main()