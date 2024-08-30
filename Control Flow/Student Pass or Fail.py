# Function to determine if student Pass or Fail
# Return "Passed" if the student scores more than or equal to 50.
# Return "Failed" if the student scores less than 50

def pass_fail(score):
    if score >= 50:
        return "Passed"
    else:
        return "Failed"


score = int(input("Enter the Score :\n"))
print(pass_fail(score))
