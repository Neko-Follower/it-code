if __name__ == '__main__':
    x = input('Введите число: ')
    while not x.isnumeric(): x = input('Введите число: ')
    print('Простое' if [i for i in range(2, (int(x) // 2) + 1) if int(x) % i == 0] == [] else 'Составное')
