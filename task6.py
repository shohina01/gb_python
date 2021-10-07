a = int(input('a = '))
b = int(input('b = '))
day = 1
print(f'{day} - й день: {a}')
while b > a:
    day += 1
    percent = a / 10
    a += percent
    print(f'{day} - й день: {a:.2f}')
print(f'На {day}-й день спортсмен достиг результата — не менее {b} км')

