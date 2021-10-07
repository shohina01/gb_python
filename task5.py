proceed = int(input('Введите значение выручки: '))
costs = int(input('Введите значение  издержек: '))
if proceed > costs:
    print('Работа фирмы : прибыль')
else:
    print('Работа фирмы : убытки')
profitability = (proceed - costs) / proceed * 100
print(f'Рентабельность выручки составляет: {profitability:.2f} %')
number_of_workers = int(input('Введите количество сотрудников фирмы: '))
profit_per_person = (proceed - costs) / number_of_workers
print(f'Прибыль фирмы в расчете на одного сотрудника составляет: {profit_per_person:.2f}')

