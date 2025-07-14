from datetime import date
import re
import sys
import inflect


def main():
    mins = get_mins(input("Date of Birth: "))
    print(f"{mins} minutes")

def get_mins(s):
    p = inflect.engine()
    if matches := re.search(r"^([0-9][0-9][0-9][0-9])-([01][0-9])-([0123][0-9])$", s):
        year = int(matches.group(1))
        month = int(matches.group(2))
        day = int(matches.group(3))
        try:
            dif = (date.today() - date(year, month, day)).days * 1440
            if dif < 0:
                sys.exit("date from future")
            else:
                return p.number_to_words(dif, andword="").capitalize()
        except ValueError:
            sys.exit("not valid date")

    else:
        sys.exit("not valid date")


if __name__ == "__main__":
    main()
