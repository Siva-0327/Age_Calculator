from datetime import datetime
import sys
from with_hours_minutes_seconds import AgeCalculating

def play_again():
    again = input("Do you want to see another one (yes/no):")

    if again.lower() == 'yes':
        return True
    elif again.lower() == 'no':
        return False
    else:
        print("Please enter yes or no")
        return play_again()  

def main():
    while True:
        name = input("Enter your Name:")
        if not name.isalpha():
            print("Please enter alphabets.")
        else:
            break

    while True:
        date = input("Enter your date of birth in given format 'yyyy-mm-dd':")
        try:
            datetime.strptime(date, "%Y-%m-%d")
            break
        except ValueError:
            print("Please enter the date in the correct format 'yyyy-mm-dd'.")

    obj = AgeCalculating(name, date)
    print(f"Hey {obj.name}, your age is {obj.years()} years ",end=' ')
    print(f"{obj.months()} months {obj.days_count()} days.")

    print("More information:")

    print(f"       {obj.total_months()} months {obj.mon_remain_days()} days")

    print(f"       {obj.total_week()} weeks {obj.total_week_remain()} days")

    print(f"       {obj.day()} days.")
    print(f"       {obj.hours()} hours.")
    print(f"       {obj.minutes()} minutes.")
    print(f"       {obj.seconds()} seconds.")


    

    

    while True:
        play = play_again()
        if play:
            main()
        else:
            print("Goodbye!")
            sys.exit()

main()
