seconds_per_hour=3600
seconds_per_minute=60

def seconds_calculator():
    hours = int(input("enter the hours: "))
    minutes = int(input("enter the minutes: "))
    seconds = int(input("enter the seconds: "))

    result = hours * seconds_per_hour + minutes * seconds_per_minute + seconds
    print(result)
    
seconds_calculator()
