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


# Data modelling using Dictionaries and Lists
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
