# Write a program with three functions. Each function must call
# at least one other function and use the return value
# of that function to do something with it. You can have more
# than three functions, and they don't need to call each other
# in a circular way.
def years_to_days(years):
    days = years/365
    return days

def years_to_hours(years):
    days = years_to_days(years)
    hours = days/24
    return hours

def years_to_minutes(years):
    hours = years_to_hours(years)
    minutes = hours/60
    return minutes

def years_to_seconds(years):
    minutes = years_to_minutes(years)
    seconds = minutes/60
    return seconds

print(years_to_seconds(1))
