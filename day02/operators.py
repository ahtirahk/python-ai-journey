# ============================================
# Day 2 - All Operators in Python
# ============================================

# 1. ARITHMETIC OPERATORS
print("===== Arithmetic Operators =====")
x = 10
y = 3
print(f"{x} + {y} = {x + y}")       # 13
print(f"{x} - {y} = {x - y}")       # 7
print(f"{x} * {y} = {x * y}")       # 30
print(f"{x} / {y} = {x / y}")       # 3.333
print(f"{x} // {y} = {x // y}")     # 3
print(f"{x} % {y} = {x % y}")       # 1
print(f"{x} ** {y} = {x ** y}")     # 1000

# 2. COMPARISON OPERATORS
print("\n===== Comparison Operators =====")
print(f"{x} == {y} is {x == y}")    # False
print(f"{x} != {y} is {x != y}")    # True
print(f"{x} > {y} is {x > y}")      # True
print(f"{x} < {y} is {x < y}")      # False
print(f"{x} >= {y} is {x >= y}")    # True
print(f"{x} <= {y} is {x <= y}")    # False

# 3. LOGICAL OPERATORS
print("\n===== Logical Operators =====")
print(f"x > 5 and y < 10 is {x > 5 and y < 10}")   # True
print(f"x > 5 and y > 10 is {x > 5 and y > 10}")   # False
print(f"x > 20 or y < 10 is {x > 20 or y < 10}")   # True
print(f"x > 20 or y > 10 is {x > 20 or y > 10}")   # False
print(f"not(x > 5) is {not(x > 5)}")                # False
print(f"not(x > 20) is {not(x > 20)}")              # True

# 4. ASSIGNMENT OPERATORS
print("\n===== Assignment Operators =====")
score = 0
print(f"Start: score = {score}")
score += 10
print(f"After += 10: score = {score}")
score -= 3
print(f"After -= 3: score = {score}")
score *= 2
print(f"After *= 2: score = {score}")
score //= 3
print(f"After //= 3: score = {score}")
score **= 2
print(f"After **= 2: score = {score}")
score %= 5
print(f"After %= 5: score = {score}")

# 5. MEMBERSHIP OPERATORS
print("\n===== Membership Operators =====")
fruits = ["apple", "banana", "mango"]
print(f"apple in fruits: {'apple' in fruits}")       # True
print(f"grape in fruits: {'grape' in fruits}")       # False
print(f"grape not in fruits: {'grape' not in fruits}") # True

name = "Ahmed"
print(f"A in Ahmed: {'A' in name}")                  # True
print(f"z in Ahmed: {'z' in name}")                  # False

# 6. TYPE CONVERSION
print("\n===== Type Conversion =====")
num_str = "10"
num_int = int(num_str)
num_float = float(num_str)
print(f"String: {num_str} → Type: {type(num_str)}")
print(f"Integer: {num_int} → Type: {type(num_int)}")
print(f"Float: {num_float} → Type: {type(num_float)}")
back_to_str = str(num_int)
print(f"Back to String: {back_to_str} → Type: {type(back_to_str)}")

# 7. IF/ELIF/ELSE
print("\n===== If/Elif/Else =====")
age = int(input("Enter your age: "))
if age < 13:
    print("You are a child")
elif age < 18:
    print("You are a teenager")
elif age < 60:
    print("You are an adult")
else:
    print("You are a senior")