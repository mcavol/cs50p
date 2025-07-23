def main():
    frac = get_fraction()
    tank = percent(frac)
    if tank <= 1:
        print("E")
    elif tank >= 99:
        print("F")
    else:
        print(f"{tank}%")

def get_fraction():
    while True:
        inp = input("Fraction: ")
        try:
            x, y = inp.split("/")
            fraction = int(x)/int(y)
            if 0 <= fraction <= 1:
                break
            else:
                continue
        except (ValueError, ZeroDivisionError, NameError):
            pass
    return fraction

def percent(xy):
    perc = round(xy*100)
    return perc

main()
