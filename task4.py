n = int(input('Введите число: '))
largest = 0
while n > 0:
    number = n % 10
    if largest < number:
        largest = number
    n = n // 10
print(f'Наибольшая цифра: {largest}')

