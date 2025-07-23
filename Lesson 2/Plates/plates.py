def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    if len(s) < 2 or len(s) > 6:
        return False

    if not s[0].isalpha() or not s[1].isalpha():
        return False

    numbers = ""
    for char in s:
        if char.isdigit():
            numbers += char
    if len(numbers) > 0:
        if numbers[0] == "0":
            return False
        if not s.endswith(numbers):
            return False

    if not s.isalnum():
        return False

    return True

main()
