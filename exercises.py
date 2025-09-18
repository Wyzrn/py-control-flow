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

# Exercise 5: What's the Season?

def determine_season():
    # Your control flow logic goes here
    month_input = input("Enter the month of the year (Jan - Dec): ").strip()[:3].title()
    try:
        day_input = input("Enter the day of the month: ")
        day = int(day_input)
        if not (1 <= day <= 31):
            print("Invalid day. Please enter a number between 1 and 31.")
            return
    except ValueError:
        print("Invalid day. Please enter a valid number.")
        return
    
    winter_months = ['Dec', 'Jan', 'Feb', 'Mar']
    spring_months = ['Mar', 'Apr', 'May', 'Jun']
    summer_months = ['Jun', 'Jul', 'Aug', 'Sep']
    fall_months = ['Sep', 'Oct', 'Nov', 'Dec']
    
    valid_months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    if month_input not in valid_months:
        print("Invalid month. Please enter a three-letter month (Jan - Dec).")
        return
    
    season = ""
    if month_input in winter_months:
        if (month_input == 'Dec' and day >= 21) or (month_input == 'Jan') or (month_input == 'Feb') or (month_input == 'Mar' and day <= 19):
            season = "Winter"
        else:
            season = "Spring" if month_input == 'Mar' else "Fall" if month_input == 'Dec' else ""
    elif month_input in spring_months:
        if month_input == 'Mar' and day >= 20:
            season = "Spring"
        elif month_input in ['Apr', 'May'] or (month_input == 'Jun' and day <= 20):
            season = "Spring"
        else:
            season = "Summer"
    elif month_input in summer_months:
        if month_input == 'Jun' and day >= 21:
            season = "Summer"
        elif month_input in ['Jul', 'Aug'] or (month_input == 'Sep' and day <= 21):
            season = "Summer"
        else:
            season = "Fall"
    elif month_input in fall_months:
        if month_input == 'Sep' and day >= 22:
            season = "Fall"
        elif month_input in ['Oct', 'Nov'] or (month_input == 'Dec' and day <= 20):
            season = "Fall"
        else:
            season = "Winter"
    
    if season:
        print(f"{month_input} {day:02d} is in {season}.")
    else:
        print("Unable to determine season for this date.")

# Call the function
determine_season()