import sys
from pyfiglet import Figlet
import random
font = ""
figlet = Figlet()

if len(sys.argv) == 1:
    figlet.setFont(font=random.choice(figlet.getFonts()))
elif (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in figlet.getFonts():
    figlet.setFont(font=sys.argv[2])
else:
    sys.exit("type font")

inp = input("Input: ")
print(f"Output:\n{figlet.renderText(inp)}")
