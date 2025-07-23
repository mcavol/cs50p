def main():
    inp = input("Input: ").strip()
    outp = make_twttr(inp)
    print(f"Output: {outp}")

def make_twttr(inp_string):
    outp_string = inp_string.replace("A", "").replace("a", "").replace("E", "").replace("e", "").replace("I", "").replace("i", "").replace("O", "").replace("o", "").replace("U", "").replace("u", "")
    return outp_string
main()
