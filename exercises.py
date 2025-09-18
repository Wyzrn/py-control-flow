# Exercise 1: Vowel or Consonant
def check_letter():
    letter = input("Enter a letter (a-z or A-Z): ")
    letter = letter.lower()
    if len(letter) == 1 and letter.isalpha():
        if letter in 'aeiou':
            print(f"The letter {letter} is a vowel.")
        else:
            print(f"The letter {letter} is a consonant.")
    else:
        print("Invalid input. Please enter a single letter.")

# Call the function
check_letter()

# Exercise 2: Old enough to vote?

def check_voting_eligibility():
    # Your control flow logic goes here
    try:
        age_input = input("Please enter your age: ")
        age = int(age_input)
        voting_age = 18
        if age < 0:
            print("Age cannot be negative. Please enter a valid age.")
        elif age >= voting_age:
            print("You are eligible to vote.")
        else:
            print("You are not old enough to vote.")
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")

# Call the function
check_voting_eligibility()