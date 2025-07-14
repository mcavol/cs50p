import random
def main():
    level = set_level()
    numb = random.randint(1, level)
    guess_int(numb)

def set_level():
    while True:
        try:
            n = eval(input("Level: "))
            if n >= 1:
                break
            else:
                continue
        except NameError:
            pass
    return n

def guess_int(n):
    while True:
        try:
            guess = eval(input("Guess: "))
            if guess >= 1:
                if guess > n:
                    print("Too large!")
                elif guess < n:
                    print("Too small!")
                else:
                    print("Just right!")
                    break
            else:
                continue
        except NameError:
            pass

if __name__=="__main__":
    main()
