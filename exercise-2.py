# Check if a number is divisible by 2 and/or 3

a = int(input("Enter an integer: "))

if a%2 == 0:
    if a%3 == 0:
        print("Divisible by 2 and 3")
    else:
        print("Divisible by 2 and not by 3")
elif a%3 == 0:
    print("Divisible by 3 and not by 2")

if a%2 == 0 and a%3 == 0:
    print("Divisible by 2 and 3")

print("Done with condition")