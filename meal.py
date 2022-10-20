def main():

    # Get time from user
    answer=input("What time is it? ")
    # Call the convert function
    time=convert(answer)
    
    # Breakfast between = 7:00-8:00
    if time >=7 and time<=8:
        print("breakfast time")
    # Lunch time between = 12:00-13:00
    if time >=12 and time<=13:
        print("lunch time")
    # Dinner between = 18:00-19:00
    if time >=18 and time<=19:
        print("dinner time")

def convert(time):
    # Get hour and minute
    hours, minutes = time.split(":")
    # Convert time into a float number
    new_minute=float(minutes)/60
    return float(hours)+new_minute
    # Return the result to main function

if __name__ == "__main__":
    main()
