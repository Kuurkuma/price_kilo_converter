from config import API_CURRENCY, CURRENCY_TO_FLAG
import freecurrencyapi

# Function to calculate price per kilogram
def price_per_kg (price, weight):
    """Calculate the price per kilogram.
    Args:
        total_price (float): The total price of the item
        weight_in_kg (float): The weight of the item in kilograms
    Returns:
        float: The price per kilogram
        """
    if weight <=0:
        raise ValueError("Weight must be greater than zero!")
    price = round((price / weight) * 1000, 2)
    return price

    print(f"The price per Kilo is {price}")

#print(price_per_kg(100,.5))

# Fetch exchange rate
def get_exchange_rate(from_currency, to_currency):
    """
    Get the current exchange rate using a free API.

    Args:
        from_currency (str): The source currency code (e.g., 'USD')
        to_currency (str): The target currency code (e.g., 'EUR')

    Returns:
        float: The exchange rate
    """
    import requests
    from requests.structures import CaseInsensitiveDict
    import freecurrencyapi


    try:
        api = API_CURRENCY
        client = freecurrencyapi.Client(api)
        #results = client.latest(base_currency=from_currency, to_currency)

        url_api = f"{api}/{from_currency.upper()}"
        response = requests.get(url_api)
        data = response.json()

        # Extract the exchange rate for the target currency
        rate = data["rates"][to_currency.upper()]
        return rate

    except KeyError:
        raise ValueError(f"Invalid currency code: '{to_currency}' not found in exchange rate data")

    except requests.exceptions.RequestException as e:
        raise ConnectionError(f"Failed to connect to exchange rate service: {e}")

    except Exception as e:
        raise Exception(f"Failed to get exchange rate: {e}")

#print(get_exchange_rate('EUR','MXN'))

def get_currency_with_flag(currency_code):
    """Returns a formatted string with currency code and flag emoji"""
    if currency_code in CURRENCY_TO_FLAG:
        return f"{CURRENCY_TO_FLAG[currency_code]} {currency_code}"
    return currency_code  # Return just the code if no emoji found

print(get_exchange_rate("MXN","EUR"))
