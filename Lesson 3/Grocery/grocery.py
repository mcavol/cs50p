def main():

    items_list = {}
    while True:
        try:
            item = input().strip().lower()
            if item in items_list:
                items_list[item] += 1
            if not item in items_list:
                items_list[item] = 1

        except EOFError:
            print()
            break

    items_list = dict(sorted(items_list.items()))
    for product in items_list:
        print(f"{items_list[product]} {product.upper()}")



main()
