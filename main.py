#2
start = int(input("Введіть початкове число: "))
end = int(input("Введіть кінцеве число: "))

if start > end:
    start, end = end, start

summa = 0
for i in range(start, end + 1):
    summa += i

print("Сума чисел у діапазоні від", start, "до", end, "дорівнює", summa)
