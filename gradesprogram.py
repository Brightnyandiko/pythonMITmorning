# 80 - 100 - A
# 60 - 79 - B
# 50 - 59 - C
# 30 - 49 - D
# below
# 30 - Fail
# negative and above 100 - invalid input

num = int(input("Enter marks :"))

if num >= 80 and num <= 100:
    print(num, "is grade A")
elif num >= 60 and num <= 79:
    print(num, "is grade B")
elif num >= 50 and num <= 59:
    print(num, "is grade C")
elif num >= 30 and num <= 49:
    print(num, "is grade D")
elif num < 30 and num >= 0:
    print(num, "the grade is a fail")
elif num < 0:
    print("Invalid input")
elif num > 100:
    print("invalid input")
else:
    print("Invalid input")
