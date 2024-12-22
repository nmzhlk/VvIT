def choose_word(age):
    if age % 10 in (2, 3, 4):
        return 'года'
    elif age % 10 == 1:
        return 'год'
    else:
        return 'лет'


def describe_person(name, age=30):
    word = choose_word(age)
    print(f'Это {name}. Возраст: {age} {word}.')


describe_person(input(), int(input()))
