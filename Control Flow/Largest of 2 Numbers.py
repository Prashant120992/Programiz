# Function to find of largest of 2 Numbers
# Return a largest of 2 numbers.
# Return a number if both are equal.
def find_largest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2
    if num1 == num2:
        return


num1 = int(input("Enter the num1 :\n"))
num2 = int(input("Enter the num2 :\n"))
print(find_largest(num1, num2))
