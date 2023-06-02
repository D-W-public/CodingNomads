# Write a function that prints out nicely formatted information about a
# real estate advertisement. The information can vary for every advertisement, which
# is why your function should be able to take an arbitrary amount of
# keyword arguments, and display them all in a list form with some 
# introductory information.

def real_ad(stats):
    print("""
Our newest, hottes, bestets Property at X-lane 1337.
If you buy now you get \n""")
    for k,  v in stats.items():
        print(f"{k:<30} : {v}")
    print("\nBUY! BUY! BUY")


property_stats = {"Space": "200m2", "Distance to the beach": "2min", "Commute Downtown": "15min", "Price": "2 megaflorps"}

real_ad(property_stats)