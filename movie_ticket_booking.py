def manage_bookings(total_seats, booked_seats, book_seat, cancel_seat):
    if book_seat in booked_seats:
        print(f"Seat {book_seat} is already booked.")
    else:
        booked_seats.append(book_seat)
    
    if cancel_seat in booked_seats:
        booked_seats.remove(cancel_seat)
    else:
        print(f"Seat {cancel_seat} was not booked.")
    
    available_seats = [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]
    return available_seats

total_seats = 10
booked_seats = [2, 5, 7]
book_seat = 3
cancel_seat = 5
available_seats = manage_bookings(total_seats, booked_seats, book_seat, cancel_seat)
print(f"Available seats: {available_seats}")
