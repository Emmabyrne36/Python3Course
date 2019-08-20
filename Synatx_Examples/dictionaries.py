donations = dict(sam=25.0, lena=88.99, chuck=13.0, linus=99.5,
                 stan=150.0, lisa=50.25, harrison=10.0)

# Dictionary Methods
# fromkeys: Creates key-value pairs from comma seperated values
# Often used to make default dictionaries
# Pass in iterable collection as first argument
{}.fromkeys(["a"], "b")  # {'a': 'b'}
new_user = {}.fromkeys(['name', 'score', 'email'], 'unknown')
print(new_user)

# get() returns the value at the key if it exists, None otherwise
print(donations.get('sam'))  # 25.0

# pop(key) - pops given key from dictionary
# popitem() - removes random entry from dictionary

# ============================================
# Data modelling using Dictionaries and Lists
# ============================================
playlist = {
    'name': 'Playlist Name',
    'author': 'Author',
    'songs': [{
        'title': 'song 1',
        'artist': ['blue'],
        'duration': 2.5
    }, {
        'title': 'song 2',
        'artist': ['kitty', 'djcat'],
        'duration': 5.25
    }]
}

# Get total of the duration
print(playlist['songs'])
total_time = 0
for song in playlist['songs']:
    total_time += song['duration']
print(total_time)


# =========================
# Dictionary Comprehension
# =========================
# Syntax { __: __ for __ in __ }
# Iterates over keys by default
numbers = dict(first=1, second=2, third=3)
squared_nums = {key: value ** 2 for key, value in numbers.items()}
print(squared_nums)

# ====================================
# Conditional Logic with Dictionaries
# ====================================
num_list = [1, 2, 3, 4]
even_odd = {num: ("even" if num % 2 == 0 else "odd") for num in num_list}
print(even_odd)

# Map ASCII number to char for capital letters
# {65: 'A, 66: 'B'} etc.
map_ASCII = {char: chr(char) for char in range(65, 91)}
