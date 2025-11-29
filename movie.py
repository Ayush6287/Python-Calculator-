def show_seats(seats):
    print("\nSeats: (X = booked, O = available)")
    for i in range(len(seats)):
        row_display = ""
        for j in range(len(seats[i])):
            if seats[i][j] == 1:
                row_display += " X "
            else:
                row_display += " O "
        print(f"Row {i+1}: {row_display}")

def book_seat(seats):
    try:
        row = int(input("Enter row number to book (1-5): ")) - 1
        seat = int(input("Enter seat number in row to book (1-5): ")) - 1
        if seats[row][seat] == 0:
            seats[row][seat] = 1
            print(f"Seat {seat+1} in Row {row+1} successfully booked!")
        else:
            print("Sorry, seat already booked. Please try different seat.")
    except (IndexError, ValueError):
        print("Invalid input. Please enter valid seat numbers.")

def main():
    seats = [[0]*5 for _ in range(5)]  # 5x5 seats, all available (0)
    print("Welcome to Simple Movie Ticket Booking System.")

    while True:
        show_seats(seats)
        print("\nOptions:\n1. Book a Seat\n2. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            book_seat(seats)
        elif choice == "2":
            print("Thank you for using the booking system!")
            break
        else:
            print("Invalid choice, please select 1 or 2.")

if __name__ == "__main__":
    main()
