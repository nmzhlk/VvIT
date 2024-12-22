def writer(text=''):
    with open('user_input.txt', 'w') as f:
        f.write(text)


def editor(name, text=''):
    with open(name, 'a') as f:
        f.write('\n')
        f.write(text)


choice = int(input('Новый файл (1) или изменить существующий (2)? --- '))
if choice == 1:
    writer(input('Введите строчку ниже:\n'))
if choice == 2:
    editor(input('Введите название файла: '), input('Введите строчку ниже:\n'))
else:
    exit()
