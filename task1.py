age = int(input('Чтобы начать введите возраст: '))
if age < 18:
    print("Салют брооо, че как?")
    answer = input()
    print('У меня также')
    name = input("А звать тебя как?")
    print(f'Приятно познакомиться, {name}!')
elif age <= 18:
    print('Здравствуйте, как ваши дела?')
    answer = input()
    print('У меня также')
    name = input("Представьтесь, пожалуйста ")
    print(f'Приятно познакомиться, {name}!')
else:
    print('До свидания!')
