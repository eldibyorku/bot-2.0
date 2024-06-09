def read_currency_data(filepath):
    currency_data = {}
    try:
        with open(filepath, 'r') as file:
            for line in file:
                key, value = line.strip().split(': ')
                currency_data[key] = int(value)
    except FileNotFoundError:
        print("File not found. Starting with an empty dictionary.")
    return currency_data

def update_currency_data(filepath, updates):
    # Read current data from file
    currency_data = read_currency_data(filepath)
    
    # Update the data with new values
    for key, added_value in updates.items():
        if key in currency_data:
            currency_data[key] += added_value
        else:
            currency_data[key] = added_value
    
    # Write updated data back to the file
    with open(filepath, 'w') as file:
        for key, value in currency_data.items():
            file.write(f"{key}: {value}\n")