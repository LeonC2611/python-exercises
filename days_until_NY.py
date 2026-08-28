from datetime import date
#import date function from datetime module
def main():
    print(f"It is {days_until_new_year()} days until the new year")

# Use date function to assign new year date to a variable as well as today's date
def days_until_new_year():
    new_year = date(2027, 1, 1)
    today = date.today()
    difference = new_year - today
    return difference.days
# This function returns how many days it is until the new year

main()
