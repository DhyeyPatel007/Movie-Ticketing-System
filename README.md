🎬 Movie Ticketing System

A Python-based command-line application that simulates a movie theatre booking system. This project demonstrates Object-Oriented Programming (OOP) principles to manage movie schedules, seat availability, and ticket transactions.

🚀 Features

View Showings: Display a list of current movies with showtimes and real-time seat availability.

Book Tickets: Search for movies by title (case-insensitive) and book specific numbers of seats.

Cancel Tickets: Cancel existing bookings and automatically release seats back to the pool.

Validation: Robust error handling for invalid inputs (e.g., negative numbers, non-integer inputs).

Dynamic Updates: Seat counts update instantly after every booking or cancellation.

🛠️ Tech Stack

Language: Python 3.x

Concepts Used: Classes, Objects, Encapsulation, Exception Handling, Lists.

📂 Project Structure

The project is built around two main classes:

class Show: Represents a single movie screening.

Attributes: title, time, total_seats, booked_seats.

Methods: book_seats(), cancel_seats(), available_seats().

class Theatre: Manages the collection of shows.

Attributes: list_of_shows.

Methods: add_show(), display_shows(), book_tickets(), cancel_tickets().

📥 How to Run

Clone the repository:

git clone [https://github.com/yourusername/movie-ticketing-system.git](https://github.com/yourusername/movie-ticketing-system.git)


Navigate to the directory:

cd movie-ticketing-system


Run the application:

python main.py


🎮 Usage Guide

When you run the program, you will see the following interactive menu:

1 --> View shows
2 --> Book tickets
3 --> Cancel tickets
4 --> Quit


1. Viewing Shows

Select option 1 to see the current movie listings.

Output: 'Sholay' at 3 hrs 48 mins - 160 seat(s) available

2. Booking Tickets

Select option 2.

Enter the movie name (e.g., "sholay" or "Sholay").

Enter the number of seats you want to book.

If seats are available, the booking is confirmed.

3. Cancelling Tickets

Select option 3.

Enter the movie name.

Enter the number of seats to cancel.

The system will update the inventory accordingly.

🔮 Future Enhancements

[ ] Data Persistence: Save booking records to a CSV or SQL database so data isn't lost on exit.

[ ] Pricing Module: Calculate total ticket cost based on the number of seats booked.

[ ] Seat Selection: Allow users to pick specific seat numbers (e.g., A1, A2).

🤝 Contributing

Contributions are welcome! Feel free to open an issue or submit a pull request.

Fork the Project

Create your Feature Branch (git checkout -b feature/AmazingFeature)

Commit your Changes (git commit -m 'Add some AmazingFeature')

Push to the Branch (git push origin feature/AmazingFeature)

Open a Pull Request

📄 License

Distributed under the MIT License. See LICENSE for more information.
