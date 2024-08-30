# Function to return Up if the input number is +ve, Down if the input number is -ve.
# Return Zero if the input number is 0.
def up_down(n):
    if n == 0:
        return "Zero"
    elif n <= 0:
        return "Down"
    elif n > 0:
        return "Up"


n = int(input("Enter the Number : \n"))
print(up_down(n))
