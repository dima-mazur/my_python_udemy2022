vowels = ['a', 'e', 'i', 'o', 'u', 'y']


def count_vowels(string):
    result = 0
    for i in string.lower():
        if i in vowels:
            result += 1
    return result
