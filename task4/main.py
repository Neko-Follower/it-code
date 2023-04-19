if __name__ == '__main__':
    products = ['Хлеб', 'Молоко']
    count = len(products)
    print(f'У тебя {count} продуктов, где {count} - значение переменной count.')
    print(''.join([product + '\n' for product in products]))
