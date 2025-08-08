def convert_units(value, from_unit, to_unit):
    conversions = {
        'miles_to_km': 1.60934,
        'km_to_miles': 0.621371,
        'celsius_to_fahrenheit': lambda c: (c * 9/5) + 32,
        'fahrenheit_to_celsius': lambda f: (f - 32) * 5/9,
    }
    
    key = f"{from_unit}_to_{to_unit}"
    if key in conversions:
        if callable(conversions[key]):
            return conversions[key](value)
        else:
            return value * conversions[key]
    else:
        return "Conversion not supported."

miles = 10
kilometers = convert_units(miles, 'miles', 'km')
print(f"{miles} miles is equal to {kilometers:.2f} kilometers.")

celsius = 25
fahrenheit = convert_units(celsius, 'celsius', 'fahrenheit')
print(f"{celsius}°C is equal to {fahrenheit:.2f}°F.")