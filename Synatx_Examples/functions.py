# Function examples
def isEven(num):
    return num % 2 == 0


def partition(arr, callback):
    """
    Iterates over arr and calls the function callback for each member
    Returns a list containing two lists of even and odd numbers
    """
    truthy_list = []
    falsey_list = []
    for i in arr:
        if callback(i):
            truthy_list.append(i)
        else:
            falsey_list.append(i)
    return [truthy_list, falsey_list]


print(partition([1, 2, 3, 4], isEven))

# Alternatives


def partition(lst, fn):
    return [[val for val in lst if fn(val)], [val for val in lst if not fn(val)]]


print(partition([1, 2, 3, 4], isEven))


def partition(l, callback):
    return [[l.pop(l.index(i)) for i in l if callback(i)], l]


print(partition([1, 2, 3, 4], isEven))


def intersection(l1, l2):
    """ Accepts two lists. Returns a list with values contained in both lists. Assumes lists same length """
    return [val for val in l1 if val in l2]


def contains_purple(*args):
    if "purple" in args:
        return True
    return False


def combine_words(word, **kwargs):
    if kwargs.get("prefix"):  # Could use if "prefix" in kwargs etc.
        return "{}{}".format(kwargs["prefix"], word)
    elif kwargs.get("suffix"):
        return "{}{}".format(word, kwargs["suffix"])
    else:
        return word

# ==============================
# Lambdas and Built-In Functions
# ==============================

# List comprehensions considered better than using map and filter in most cases
# Map example


def decrement_list(nums):
    return list(map(lambda x: x - 1, nums))


# Filter example


def remove_negatives(l):
    return list(filter(lambda n: n >= 0, l))


# Any and All examples
def is_all_string(l):
    return all(type(x) == str for x in l)


def extremes(l):
    ''' Gets min and max of iterable '''
    return (min(l), max(l))


print(extremes([1, 2, 3, 4, 5]))
print(extremes((99, 25, 30, -7)))
print(extremes('alcatraz'))


def max_magnitude(l):
    return max((abs(x) for x in l))


print(max_magnitude([300, 4, -900]))


def sum_even_values(*args):
    return sum(x for x in args if x % 2 == 0)


print(sum_even_values(1, 2, 3, 4, 5, 6))  # 12
print(sum_even_values(4, 2, 1, 10))  # 16
print(sum_even_values(1))  # 0


def sum_floats(*args):
    return sum(n for n in args if isinstance(n, float))


print(sum_floats(1.5, 2.4, 'awesome', [], 1))  # 3.9
print(sum_floats(1, 2, 3, 4, 5))  # 0


def interleave(str1, str2):
    return "".join("".join(s) for s in zip(str1, str2))


print(interleave("hi", "ha"))  # hhia


def triple_and_filter(nums):
    # Alternative answer: [x * 3 for x in [y for y in nums if y % 4 == 0]]
    return list(map(lambda x: x*3, filter(lambda n: n % 4 == 0, nums)))


print(triple_and_filter([1, 2, 3, 4]))  # [12]
print(triple_and_filter([6, 8, 10, 12]))  # [24,36]

print()


def extract_full_name1(names):
    return [f"{n['first']} {n['last']}" for n in names]


def extract_full_name2(l):
    return list(map(lambda val: "{} {}".format(val['first'], val['last']), l))


names = [{'first': 'Ellie', 'last': 'Schoppik'},
         {'first': 'Colt', 'last': 'Steele'}]
print(extract_full_name1(names))
print(extract_full_name2(names))
