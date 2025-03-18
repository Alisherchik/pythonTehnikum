# all_product = {'Склад': {}, 'Корзина': {}}
#
# def add_product['Склад': [product_name], ('К'
sklad = 'Склад'
all_product = {sklad: {}, 'Корзина': {}}

while True:
    print('''1. Добавить продукт в склад
2. Изменить кол-во продукта
3. Добавить в корзину''')
    n = input('')
    if n == '1':
        add_product()
    elif n == '2':
        info = input("Какой продукт хотите изменить: ")
        if info in all_product[sklad]:
            quantity = int(input("Какой кол-во продуктов будет: "))
            all_product[sklad][info] = quantity
            print(all_product)
        else:
            print("Такого продукта нет")
    elif n == '3':
        product_to_cart = input("Какой продукт хотите добавить в корзину")
        if product_to_cart in all_product[sklad]:
            product_to_cart_quantity = int(input('Какое кол-во'))
            quantity = all_product[sklad][product_to_cart]
            all_product[sklad][product_to_cart] = quantity - product_to_cart_quantity
            all_product['Корзина'][product_to_cart] = product_to_cart_quantity
            print(all_product)
        else:
            print("Такого продукта в складе нет")
            # Корзина': [product_count]]