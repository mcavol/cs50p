import requests
import sys
import json

def main():
    response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    dict = response.json()
    usd_rate = float(dict['bpi']['USD']['rate'].replace(",",""))
    amount = get_amount()
    price = usd_rate * amount
    print(f"${price:,.4f}")



def get_amount():
    try:
        n = float(sys.argv[1])

    except ValueError:
        sys.exit("need amount in float")
    return n

if __name__ == "__main__":
    main()
