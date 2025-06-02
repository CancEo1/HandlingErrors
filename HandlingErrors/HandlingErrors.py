# Simple calculator program to handle errors in Python
def get_price():
    while True:
        try:
            price = float(input("Enter the price: "))
            return price
        except ValueError:
            print("Please enter a decimal number.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter the quantity: "))
            return quantity
        except ValueError:
            print("Invalid Integer. Please Try again.")

def main():
    print("Welcome to the Total Price Calculator")

    # Get the price and quantity
    price = get_price()
    quantity = get_quantity()

    # Calculate the total price
    total = price * quantity

    # Display the results
    print()
    print("Price: ", price)
    print("Quantity: ", quantity)
    print("Total: ", total)

if __name__ == "__main__":
    main()
    print("Thank you for using the Total Price Calculator!")
