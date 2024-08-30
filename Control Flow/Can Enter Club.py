# Function to Determine if a person is eligible to enter a club.
# The club allows people who are 21 years old or older.
# Return True if the person can enter a club.
# Return False if the person cannot enter a club
# For the input age = 30, the output will be True
def can_enter_club(age):
    if age >= 21:
        return True
    else:
        return False


age = int(input("Enter the Age:\n"))
print(can_enter_club(age))
