def get_words():
    return ['Robolox','Nvidia','Facebook','Mircosoft']

def check_words(correct_guesses,incorrect_guesses):
#if any value in getwords is input it returned a boolean true and if not return false
# otherwise return false
    if correct_guesses in get_words():
        return True
    if incorrect_guesses in get_words():
        return True
    return False

# Take in 2 parameters corrects guesses and incorrect guesses and return a string based on the number of guesses
def check_total(correct_guesses,incorrect_guesses):
#return winner if the number of correct guesses greater than 4
    if correct_guesses > 4:
        return 'Winner'
# return loser if the number of incorrect guesses greather than 4
    if incorrect_guesses > 4:
        return 'Loser'
# return draw if the number of correct and incorrect guesses are equal
    if correct_guesses == incorrect_guesses:
        return 'Draw'

#The main function runs the guessing game
def main():
    correct_guesses = 0
    incorrect_guesses = 0

#This is the loop for guesses 
    for x in range(8):
        get_words()
        guess = input("Guess one of the names of the software companies: ")

#This checks if the guess is correct
        if check_words(guess, get_words()) == True:
            correct_guesses = correct_guesses + 1

#This checks if the guess is incorrect
        if check_words(guess, get_words()) == False:
            incorrect_guesses = incorrect_guesses + 1
    print(correct_guesses)
    print(incorrect_guesses)
    

#This determines if the player is a wins, loses, or draws
    print(check_total(correct_guesses,incorrect_guesses))
main()
