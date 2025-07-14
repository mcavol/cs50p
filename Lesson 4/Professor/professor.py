import random

def main():
    level = get_level()
    score = 0
    for i in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        tries = 3
        while tries > 0:
            try:
                answer = int(input(f"{x} + {y} = "))
                if answer == (x+y):
                    score += 1
                    break
                else:
                    tries -=1
                    print("EEE")
                    continue
            except ValueError:
                tries -=1
                print("EEE")
                pass
        if tries ==0:
            print(f"{x} + {y} = {x+y}")

    print(f"Score: {score}")


def get_level():
    while True:
        try:
            n = eval(input("Level: "))
            if n == 1 or n==2 or n==3:
                break
            else:
                continue
        except NameError:
            pass
    return n


def generate_integer(level):
    if level==1:
        a = 0
        b = 9

    elif level==2:
        a = 10
        b = 99

    elif level==3:
        a = 100
        b = 999

    int_number = random.randint(a, b)
    return int_number


if __name__ == "__main__":
    main()
