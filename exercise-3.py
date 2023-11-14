# Given two numbers, check if numbers are equals it prints they are equal if not prints which one are smaller

x = float(input("Enter a number for x: "))
y = float(input("Enter a nubmer of y: "))

if x == y:
    print("x and y are equal")
elif x < y:
    print("x is smaller than y")
else:
    print("y is smaller than y")