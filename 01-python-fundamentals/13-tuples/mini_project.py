'''Flight Booking System

Each booking

(
Passenger Name,
Flight Number,
Seat Number
)

Functions

Book seat
Search booking
Cancel booking
Display bookings'''

bookings = []


def book_seat():
    name = input("Enter passenger name: ")
    flight = input("Enter flight number: ")
    seat = input("Enter seat number: ")

    # Check if seat is already booked
    for booking in bookings:
        if booking[2] == seat:
            print("Seat already booked!")
            return

    bookings.append((name, flight, seat))
    print("Booking successful.")


def search_booking():
    name = input("Enter passenger name: ")

    found = False

    for booking in bookings:
        if booking[0].lower() == name.lower():
            print("\nBooking Found")
            print("Passenger :", booking[0])
            print("Flight    :", booking[1])
            print("Seat       :", booking[2])
            found = True
            break

    if not found:
        print("Booking not found.")


def cancel_booking():
    name = input("Enter passenger name: ")

    for booking in bookings:
        if booking[0].lower() == name.lower():
            bookings.remove(booking)
            print("Booking cancelled.")
            return

    print("Booking not found.")


def display_bookings():

    if len(bookings) == 0:
        print("No bookings available.")
        return

    print("\n------ All Bookings ------")

    for booking in bookings:
        print(f"Passenger : {booking[0]}")
        print(f"Flight    : {booking[1]}")
        print(f"Seat       : {booking[2]}")
        print("--------------------------")


while True:

    print("""
========== Flight Booking System ==========
1. Book Seat
2. Search Booking
3. Cancel Booking
4. Display Bookings
5. Exit
""")

    choice = input("Enter your choice: ")

    if choice == "1":
        book_seat()

    elif choice == "2":
        search_booking()

    elif choice == "3":
        cancel_booking()

    elif choice == "4":
        display_bookings()

    elif choice == "5":
        print("Thank you!")
        break

    else:
        print("Invalid choice.")








