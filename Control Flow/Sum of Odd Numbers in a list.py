# Function to find the sum of odd numbers in a list.
# For the input: [1, 2, 3, 4, 5] the result will be 9.
def sum_of_odds(numbers):
    result = 0
    for i in numbers:
        if i % 2 == 1:
            result = i + result
    return result


numbers = [1, 2, 3, 4, 5]
print(sum_of_odds(numbers))
