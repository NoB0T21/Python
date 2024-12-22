def day_of_week(day):
    match day:
        case 1:
            return "it's Sunday"
        case 2:
            return "it's Monday"
        case 3:
            return "it's Tusday"
        case 4:
            return "it's Thursday"
        case 5:
            return "it's Friday"
        case 6:
            return "it's Saturday"
        case _:
            return "it's not a valid day"

n = int(input("Enter 1-7 to check days"))   
print (day_of_week(n))