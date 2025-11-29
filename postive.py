def positive_negative_checker():
    try:
        num = float(input("Enter a number: "))
        if num > 0:
            print("The number is Positive.")
        elif num < 0:
            print("The number is Negative.")
        else:
            print("The number is Zero.")
    except ValueError:
        print("Invalid input! Please enter a valid number.")

if __name__ == "__main__":
    positive_negative_checker()
