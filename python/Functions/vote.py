def check_age(age):
    if age >= 18:
        return "You are an adult. Eligible to vote"
    else:
        return "You are a minor. Not eligible to vote"

age_input = int(input("Enter your age: "))
message = check_age(age_input)
print(message)
