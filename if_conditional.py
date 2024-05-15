# 1. Basic if Statement
x = 10
if (x > 5):
    print("x is greater than 5")

# 2. if-else Statement
x = 3
if (x > 5):
    print("x is greater than 5")
else:
    print("x is not greater than 5")

# 3. if-elif-else Statement
x = 5
if x > 10:
    print("x is greater than 10")
elif x == 5:
    print("x is equal to 5")
else:
    print("x is less than 10 and not equal to 5")

# 4. Nested if Statement
x = 25
if x > 10:
    print("x is greater than 10")
    if x > 20:
        print("x is also greater than 20")
    else:
        print("but x is not greater than 20")

# 5. Using and and or Operators
x, y = 5, 10
if x == 5 and y == 10:
    print("Both conditions are true")

if x == 5 or y == 20:
    print("At least one of the conditions is true")

# 6. Inline if (Ternary Operator)
x = 10
message = "Even" if x % 2 == 0 else "Odd"
print(message)

# 7. Using if with Lists
fruits = ["apple", "banana", "cherry"]
if "banana" in fruits:
    print("Yes, banana is in the fruits list")

# 8. Using if to Check for Empty Lists or Strings
my_list = []
if not my_list:
    print("The list is empty")

my_string = ""
if not my_string:
    print("The string is empty")
