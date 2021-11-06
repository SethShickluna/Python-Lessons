# we want a function to tell us to wake up in the morning unless its the weekend or we are on vacation 

def wake_up(day, vacation): 
    # day is a string -> name of a weekday 
    # vacation is a boolean -> either true or false 
    # return "Wake up!" or "Sleep in"
    
    # if vacation is true 
    # if day == "Saturday" or "Sunday"
    # otherwise we have to wake up 

    if vacation: 
        return "Sleep in!"

    # check if day is a weekday
    # or day is a weekend 
    if day == "Saturday" or day == "Sunday":
        return "Sleep in!"

    return "Wake up!"
    

print(wake_up("Monday", False))

print(wake_up("Saturday", False))

print(wake_up("Thursday", True))