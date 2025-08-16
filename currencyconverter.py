def convert_currency(amount, from_currency, to_currency):
    """Converts an amount from one currency to another using fixed rates."""
    exchange_rates = {
        'USD': {'EUR': 0.85, 'JPY': 110.00, 'GBP': 0.73},
        'EUR': {'USD': 1.18, 'JPY': 129.41, 'GBP': 0.86},
        'JPY': {'USD': 0.0091, 'EUR': 0.0077, 'GBP': 0.0066}
    }
    
    from_currency = from_currency.upper()
    to_currency = to_currency.upper()

    if from_currency not in exchange_rates or to_currency not in exchange_rates[from_currency]:
        return "Error: Unsupported currency or conversion."
    
    rate = exchange_rates[from_currency][to_currency]
    converted_amount = amount * rate
    return converted_amount

if __name__ == "__main__":
    try:
        amount = float(input("Enter the amount: "))
        from_curr = input("Enter the original currency (e.g., USD, EUR, JPY): ")
        to_curr = input("Enter the target currency: ")
        
        converted = convert_currency(amount, from_curr, to_curr)
        if isinstance(converted, str):
            print(converted)
        else:
            print(f"{amount} {from_curr.upper()} is equal to {converted:.2f} {to_curr.upper()}")
    except ValueError:
        print("Invalid amount entered.")