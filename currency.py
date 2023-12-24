import requests


API_KEY = 'fca_live_wpr59HXkOPMzTbu6Huc7fsawD6HMSfaiE6QPVvzF'
BASE_URL = f"https://api.freecurrencyapi.com/v1/latest?apikey={API_KEY}"

CURRENCIES = ["USD", "PLN", "CAD", "EUR", "AUD", "JPY", "BGN", "CZK", "GBP", "NOK", "TRY", "NZD", "ZAR", "PHP"]

def convert_currency (base):
	currencies = ",".join(CURRENCIES)
	url = f"{BASE_URL}&base_currency={base}&currencies={currencies}"
	try:
		response = requests.get(url)
		data = response.json()
		return data["data"]

	except:
		print("Invalid currency")
		return None

while True:
	base = input("Enter the base currency (q for quit): ").upper()

	if base == "Q":
		break

	currency = input("\nEnter currency to be converted to: ").upper()
	amount = float(input("\nEnter amount to be converted: "))
	data = convert_currency(base)

	if not data:
		break

	value = float(data[currency]) * amount
	value = "{:.2f}".format(value)
	print(f"{amount} {base} is equal to: {value} {currency}")