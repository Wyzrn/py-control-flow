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

# Exercise 3: Calculate Dog Years

def calculate_dog_years():
    # Your control flow logic goes here
    try:
        dog_age_input = input("Input a dog's age: ")
        dog_age = int(dog_age_input)
        if dog_age <= 0:
            print("Invalid age. Please enter a positive number.")
        else:
            if dog_age == 1:
                dog_years = 10
            elif dog_age == 2:
                dog_years = 20
            else:
                dog_years = 20 + (dog_age - 2) * 7
            print(f"The dog's age in dog years is {dog_years}.")
    except ValueError:
        print("Invalid input. Please enter a valid number for age.")

# Call the function
calculate_dog_years()

# Exercise 4: Weather Advice

def weather_advice():
    # Your control flow logic goes here
    is_cold_input = input("Is it cold? (yes/no): ").lower()
    is_raining_input = input("Is it raining? (yes/no): ").lower()
    
    is_cold = is_cold_input == 'yes'
    is_raining = is_raining_input == 'yes'
    
    if is_cold and is_raining:
        print("Wear a waterproof coat.")
    elif is_cold and not is_raining:
        print("Wear a warm coat.")
    elif not is_cold and is_raining:
        print("Carry an umbrella.")
    elif not is_cold and not is_raining:
        print("Wear light clothing.")
    else:
        print("Invalid input. Please enter yes or no.")

# Call the function
weather_advice()