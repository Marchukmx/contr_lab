#9

def filter_python_strings(strings):
    python_strings = [i for i in strings if "Python" in i]
    return python_strings

user_strings = ["петух", "world", "Python легче C++", "вивчаю Python"]
gotovi = filter_python_strings(user_strings)
print("Результат:", gotovi)
