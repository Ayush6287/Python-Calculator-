import time

def show_menu():
    """Display conversion options"""
    print("\n=== Unit Converter ===")
    print("1. Length (m ↔ cm ↔ km)")
    print("2. Weight (kg ↔ g ↔ lb)")
    print("3. Temperature (C ↔ F)")
    print("4. Exit")

def length_converter():
    """Length conversions"""
    value = float(input("Enter value: "))
    print("1. Meters to Centimeters")
    print("2. Centimeters to Meters") 
    print("3. Meters to Kilometers")
    print("4. Kilometers to Meters")
    
    choice = input("Choose (1-4): ")
    if choice == '1':
        result = value * 100
        print(f"{value} m = {result} cm")
    elif choice == '2':
        result = value / 100
        print(f"{value} cm = {result} m")
    elif choice == '3':
        result = value / 1000
        print(f"{value} m = {result} km")
    elif choice == '4':
        result = value * 1000
        print(f"{value} km = {result} m")
    else:
        print("Invalid choice!")

def weight_converter():
    """Weight conversions"""
    value = float(input("Enter value
