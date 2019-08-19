# List comprehensions in Python 3
# Syntax: [ __ for __ in __ ]

nums = [1, 2, 3, 4, 5]
# For each value in x, multiply it by 10 and make a new list
nums2 = [x * 10 for x in nums]
print(nums)
print(nums2)

message = "hello"
print([char.upper() for char in message])  # HELLO

print([bool(c) for c in [0, [], '', 1]])  # False, False, False, True

# Cast list from list of ints to list of strings
str_list = [str(x) for x in nums]
print(str_list)

# ===========================================
# List Comprehensions with Conditional Logic
# ===========================================
evens = [n for n in nums if n % 2 == 0]
odds = [n for n in nums if n % 2 != 0]
print(f"Nums list: {nums}")
print(f"Evens list: {evens}")
print(f"Odds list: {odds}")

# Multiply by 2 if even, divide by two if odd
mult_list = [n * 2 if n % 2 == 0 else n / 2 for n in nums]
print(mult_list)

list_1 = [1, 2, 3, 4]
list_2 = [3, 4, 5, 6]
list_3 = ["Ellie", "Tim", "Matt"]

in_list1_and_list2 = [num for num in list_1 if num in list_2]

# The slice [::-1] is a quick way to reverse a string
rev_list_3 = [name[::-1].lower() for name in list_3]

str_example = "amazing"
str_example_no_vowels = [c for c in str_example if c not in "aeiou"]
print(str_example_no_vowels)

# ==========================
# Nested List comprehension
# ==========================
nested_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
[[print(f"{val}", end=" ") for val in l] for l in nested_list]

print()
board = [["X" if num % 2 == 0 else "O" for num in range(1, 4)]
         for val in range(1, 4)]
print(board)

# 2D Grid
grid = [["*" for x in range(3)] for i in range(3)]
print(grid)
