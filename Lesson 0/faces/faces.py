def convert(text):
    text = text.replace(":)", "🙂").replace(":(", "🙁")
    return text

def main():
    inp_text = input()
    conv_text = convert(inp_text)
    print(conv_text)

if __name__ == "__main__":
    main()



