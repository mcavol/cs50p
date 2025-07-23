def main():
    total_amount = 0
   
    while True:
        while True:
            coins = 0
            coins = eval(input(f"Amount Due: {50-total_amount}\nInsert coin: "))
            if coins == 5 or coins == 10 or coins == 25:
                break

        total_amount += coins
        if total_amount >= 50:
            print(f"Change Owed: {total_amount-50}")
            break

main()

