if __name__ == '__main__':
    products = ['Хлеб', 'Чай', 'Молоко']
    count = len(products)
    print(f'У тебя {count} продуктов, где {count} - значение переменной count.')
    print(''.join([product + '\n' if len(product) % 2 == 0 else '' for product in products]))
