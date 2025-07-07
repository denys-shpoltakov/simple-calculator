val_1 = int(input("Enter your first value: "))
val_2 = int(input("Enter your second value: "))
operator = (input("Choose an option +, -, *, / : "))


if operator == '+':
    print(f"Result: {val_1 + val_2}")
    
elif operator == '-':
    print(f"Result: {val_1 - val_2}")

elif operator == '*':
    print(f"Result: {val_1 * val_2}")

elif operator == '/':
    print(f"Result: {val_1 / val_2}")

print('This is where program stops')