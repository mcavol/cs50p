def main():
    camel = input("camelCase: ").strip()
    snake = make_snake(camel)
    print(f"snake_case: {snake}")

def make_snake(camelName):
    snake_name = ""
    for l in camelName:
        if l.isupper():
            snake_name = snake_name + "_" + l.lower()
        else:
            snake_name = snake_name + l

    #check if string starts with _ and then remove a first letter from string
    if snake_name.startswith("_"):
        snake_name = snake_name[1:]
    return snake_name
main()


