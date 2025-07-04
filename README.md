# Flight_Ticket_Booking
Every flight has:<br>
    Flight Number (unique)<br>
    Source & Destination<br>
    Date & Time (must be in future)<br>
    Base Price per seat<br>
    Flights of previous date should not been displayed for the user entered date.<br>


Seat Booking Rules<br>
    Don’t allow the same user to book the same flight twice<br>
    Price increases as seats get filled (ex: +10% every 20 seats)<br>
    Seat classes (optional)	Economy, Business, First Class (different price levels)<br>

Pricing & Discounts<br>
    User age >= 60	Apply 10% discount<br>
    Student Apply 5% discount<br>

Suggested Rules/Validations to Include<br>
    Cannot book more than 6 seats per user<br>
    Cannot book past-date flights<br>
    Show confirmation before payment<br>
    Decrease available seats after successful booking<br>
    Stop booking if flight is full<br>

<br><br><br><br>


# Advanced option 
Admin Functionality (Optional)<br>
    Add new flights<br>
    Update existing flights<br>
    Cancel flights<br>
    View total bookings<br>
    View available seats for any flight<br>
<br><br>


Add things to a database<br> 
    Python handles:<br>
        User inputs<br>
        Booking logic<br>
        Validation<br>
        Business rules (max seats, price, etc.)<br>
    SQL is Your Database<br>
        SQL stores:<br>
        Users<br>
        Flights<br>

Bookings<br>
    Seat availability<br>
    Prices<br>


Sort flights by price<br>
Sort flights by date<br>