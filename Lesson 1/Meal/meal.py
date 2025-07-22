def main():
    time = input("What time is it? ")
    newtime = convert(time)
    if 7 <= newtime <= 8:
        print("breakfast time")
    if 12 <= newtime <= 13:
        print("lunch time")
    if 18 <= newtime <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    conv_time = eval(hours) + eval(minutes)/60
    return conv_time


if __name__ == "__main__":
    main()
