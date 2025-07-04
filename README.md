# Flight_Ticket_Booking
Every flight has:
    Flight Number (unique)
    Source & Destination
    Date & Time (must be in future)
    Base Price per seat
    Flights of previous date should not been displayed for the user entered date.


Seat Booking Rules
    Don’t allow the same user to book the same flight twice
    Price increases as seats get filled (ex: +10% every 20 seats)
    Seat classes (optional)	Economy, Business, First Class (different price levels)

Pricing & Discounts
    User age >= 60	Apply 10% discount
    Student Apply 5% discount

Suggested Rules/Validations to Include
    Cannot book more than 6 seats per user
    Cannot book past-date flights
    Show confirmation before payment
    Decrease available seats after successful booking
    Stop booking if flight is full




# Advanced option 
Admin Functionality (Optional)
    Admin can:
    Add new flights
    Update existing flights
    Cancel flights
    View total bookings
    View available seats for any flight



Add things to a database 
    Python handles:
        User inputs
        Booking logic
        Validation
        Business rules (max seats, price, etc.)
    SQL is Your Database
        SQL stores:
        Users
        Flights

Bookings
    Seat availability
    Prices


Sort flights by price
Sort flights by date