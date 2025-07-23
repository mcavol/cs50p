def main():
    month_list = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    month_dict = make_dict(month_list)
    while True:
        date = input("Date: ")
        try:
            if "/" in date:
                month,day,year = date.split("/")
                month = int(month)
                day = int(day)
                year = int(year)
                if month <= 12 and day <= 31:
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    continue
            elif ", " in date:
                month,day,year = date.split(" ")
                day = int(day.replace(",",""))
                year = int(year)
                if month in month_dict and day <= 31:
                    month = month_dict[month]
                    print(f"{year}-{month:02}-{day:02}")
                    break
                else:
                    continue
        except ValueError:
            pass


def make_dict(some_list):
    some_dict = {}
    n = 0

    for month in some_list:
        n +=1
        some_dict[month] = n

    return some_dict

main()
