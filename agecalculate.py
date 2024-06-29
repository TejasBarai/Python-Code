from datetime import date
 
#def calculateAge(birthDate):
   # days_in_year = 365.2425   
    #age = int((date.today() - birthDate).days / days_in_year)
    #return age
         
#print(calculateAge(date(1997, 2, 3)), "years")
def get_user_birthday():
    birth_year = int(input('Please enter your birth year: '))
    birth_month = int(input('Please enter your birth month: '))
    birth_day = int(input('Please enter your birth day: '))

    #Convert user input into datetime object
    user_birthday = date(birth_year, birth_month, birth_day)

    return user_birthday

def calculate_age(user_birthday):
    #Get current date
    today = date.today()
    #Calculate the years difference
    year_diff = today.year - user_birthday.year
    #Check if birth month and birth day preced current month and current day
    precedes_flag = ((today.month, today.day) < (user_birthday.month, user_birthday.day))
    #Calculate the user's age
    age = year_diff - precedes_flag
    #Return the age value
    return age


if __name__ == "__main__":
    user_birthday = get_user_birthday()
    current_age = calculate_age(user_birthday)
    print(f"Your age is: {current_age}")
2