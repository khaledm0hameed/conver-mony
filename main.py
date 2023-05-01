import requests

currencies = ["USD", "EUR", "GBP"]  # list of supported currencies

money = input("Enter the money amount with currency symbol (e.g. $100): ")
currency = money[0]  # extract the currency symbol
amount = float(money[1:])  # extract the amount

print(f"Converting {money}...")

for target_currency in currencies:
    if target_currency != currency:
        url = f"https://api.exchangerate-api.com/v4/latest/{currency}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()
            rate = data["rates"][target_currency]
            converted_amount = amount * rate
            print(f"{target_currency}{converted_amount:.2f}")
        else:
            print("Error: Unable to retrieve exchange rate")
