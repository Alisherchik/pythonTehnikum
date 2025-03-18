all_product = 'Все товары'
korzina = 'Корзина'

sklad = {'Весь склад': {} }
print(sklad)
print(sklad['Весь склад'])

def a (pr_name, pr_count):

    if pr_name in sklad['Весь склад']:
        print('Такой уже есть')
    else:
        sklad['Весь склад'][pr_name] = pr_count
        print(sklad)
def c(pr_name, new_count):

    if pr_name in sklad['Весь склад']:
        sklad['Весь склад'][pr_name] += new_count
    else:

        print("Такого продукта нету")
def b(pr_name, n_count):
    if pr_name in sklad['Весь склад']:
        sklad['Весь склад'][pr_name] -= n_count
    else:

        print("Такого продукта нету")

a('banan', 12)
print(sklad)
c('banan', 10)
print(sklad)
a('banan', 12)
print(sklad)
b('banan', 5)
print(sklad)
