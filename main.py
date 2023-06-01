#8
def filter_capitalized_strings(strings):
    capitalized_strings = [string for string in strings if string[0].isupper()]
    return capitalized_strings

vvod_strings = ["Салам", "Алейкум", "діма", "магазин" , "Вова" , "Лох"]
filtered_strings = filter_capitalized_strings(vvod_strings)
print("Результат:", filtered_strings)
