# Function to check if number is Weird
# If number is odd its weird
# If the number is even and in the inclusive range of 2to5, it "Not Weird"
# If its even and in the inclusive range of 6to20, its "Weird".
# It is even greater than 20 its "Not Weird."
def is_weird(n):
    if n & 1:
        return "Weird"
    elif (1 < n < 6) or n > 20:
        return "Not Weird"
    elif 6 < n < 21:
        return "Weird"


n = int(input("Enter the number : \n"))
print(is_weird(n))
