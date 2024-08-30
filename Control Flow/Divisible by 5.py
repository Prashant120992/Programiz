# Return True if the number is divisible by 5
def is_divisible_by_five(n):
    if n % 5 == 0:
        return True
    else:
        return False


n = int(input("Enter the number\n"))
print(is_divisible_by_five(n))
