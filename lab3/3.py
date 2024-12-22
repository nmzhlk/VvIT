def file_viewer(name='', style='all'):
    try:
        with open(name, 'r') as f:
            if style == 'all':
                print(f.read())
            elif style == 'str':
                for line in f:
                    print(line, end='')
            else:
                print('(!) Неизвестный метод чтения :(')
    except FileNotFoundError:
        print('(!) Файл с таким названием не найден :(')


name = input('Введите название файла с расширением: ')
style = input('Введите метод чтения: all - f.read() / str - for loop: ')
file_viewer(name, style)
