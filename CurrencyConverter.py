import tkinter as tk

# Open the file containing currency data
with open('CurrencyData.txt') as f:
    # Read all lines from the file
    lines = f.readlines()

# Create an empty dictionary to store currency data
CurrencyDict = {}

# Iterate over each line in the file
for line in lines:
    # Split the line by tab character to separate currency name and conversion rate
    parsed = line.split("\t")

    # Check if the line has at least two elements
    if len(parsed) >= 2:
        # Assign currency name as key and conversion rate as value to the dictionary
        CurrencyDict[parsed[0]] = parsed[1].strip()  # Remove any leading/trailing whitespace


# Function to handle currency conversion
def convert_currency():
    # Get the input amount and target currency
    amt = entry_amount.get()
    Currency = entry_currency.get()

    # Check if the entered currency exists in the dictionary
    if Currency in CurrencyDict:
        # Convert the amount to the target currency using the conversion rate
        converted_amount = float(amt) * float(CurrencyDict[Currency])

        # Display the result
        result_label.config(text=f"{amt} INR is equal to {converted_amount} {Currency}")
    else:
        # Display an error message if the entered currency is not found
        result_label.config(text="Error: Invalid currency selection. Please choose from the available options.")


# Function to reset the fields and result message
def reset_fields():
    entry_amount.delete(0, tk.END)
    entry_currency.delete(0, tk.END)
    result_label.config(text="")


# Create a Tkinter window
window = tk.Tk()
window.title("Currency Converter")

# Create labels and entry fields
label_amount = tk.Label(window, text="Enter the amount you want to convert from INR:")
label_amount.pack()
entry_amount = tk.Entry(window)
entry_amount.pack()

label_currency = tk.Label(window, text="Enter the currency you want to convert to:")
label_currency.pack()
entry_currency = tk.Entry(window)
entry_currency.pack()

# Display available currency options
available_currencies = "\n".join(CurrencyDict.keys())
label_available = tk.Label(window, text=f"Available options:\n{available_currencies}")
label_available.pack()

# Create buttons for conversion and reset
convert_button = tk.Button(window, text="Convert", command=convert_currency)
convert_button.pack()

reset_button = tk.Button(window, text="Reset", command=reset_fields)
reset_button.pack()

# Create a label for displaying the result or error message
result_label = tk.Label(window, text="")
result_label.pack()

# Start the Tkinter event loop
window.mainloop()
