if __name__ == '__main__':
    x = input('Введите число: ')
    while not x.isnumeric(): x = input('Введите число: ')
    print((lambda i, x=[0,1]: [(x.append(x[y+1]+x[y]), x[y+1]+x[y])[1] for y in range(i)])(int(x))[int(x)-1])
