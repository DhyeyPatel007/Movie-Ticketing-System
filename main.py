class Show:
    def __init__(self, title, time, total_seats):
        self.title = title
        self.time = time
        self.total_seats = total_seats
        self.bookes_seat = 0

    def book_seats(self, n):
        if n <= 0:
            print("Please enter a positive number of seats to book.")



            return False
        if self.bookes_seat + n <= self.total_seats:
            self.bookes_seat += n
            print(f"{n} seat(s) booked for '{self.title}'.")
            return True
        else:
            available = self.total_seats - self.bookes_seat
            print(f"Unable to book {n} seat(s). Only {available} seat(s) available for '{self.title}'.")
            return False

    def cancel_seats(self, n):
        if n <= 0:
            print("Please enter a positive number of seats to cancel.")
            return False
        if self.bookes_seat >= n:
            self.bookes_seat -= n
            print(f"{n} seat(s) cancelled for '{self.title}'.")
            return True
        else:
            print(f"Cannot cancel {n} seat(s). Only {self.bookes_seat} seat(s) are currently booked for '{self.title}'.")
            return False

    def available_seats(self):
        return self.total_seats - self.bookes_seat

    def __str__(self):
        return f"'{self.title}' at {self.time} - {self.available_seats()} seat(s) available"


class Theatre:
    def __init__(self):
        self.shows = []

    def add_show(self, show):
        self.shows.append(show)

    def display_shows(self):
        if not self.shows:
            print("No show available right now.")
        else:
            for show in self.shows:
                print(show)

    def book_tickets(self, title, count):
        for show in self.shows:
            if show.title.lower() == title.lower():
                return show.book_seats(count)
        print(f"Show '{title}' not found.")
        return False

    def cancel_tickets(self, title, count):
        for show in self.shows:
            if show.title.lower() == title.lower():
                return show.cancel_seats(count)
        print(f"Show '{title}' not found.")
        return False


def run_theatre():
    theatre = Theatre()

    theatre.add_show(Show("Sholay", "3 hrs 48 mins", 160))
    theatre.add_show(Show("Sooryavansham", "3 hrs 02 mins", 160))
    theatre.add_show(Show("Kuch Kuch Hota Hai", "2 hrs 48 mins", 160))
    theatre.add_show(Show("Pardes", "3 hrs 17 mins", 160))
    theatre.add_show(Show("Hum, Saath-Saath Hain", "3 hrs 17 mins", 160))
    theatre.add_show(Show("Dilwale Dulhania Le Jayenge", "3 hrs 26 mins", 160))
    theatre.add_show(Show("Pyaar Kiya to Darna Kya", "3 hrs 17 mins", 160))
    theatre.add_show(Show("Border", "2 hrs 17 mins", 160))
    theatre.add_show(Show("Andaz Apna Apna", "2 hrs 55 mins", 160))
    theatre.add_show(Show("Hum Aapke Hain Koun..!", "3 hrs 50 mins", 160))
    theatre.add_show(Show("Karan Arjun", "3 hrs 01 mins", 160))
    theatre.add_show(Show("Main Khiladi Tu Anari", "2 hrs 37 mins", 160))
    theatre.add_show(Show("Coolie", "3 hrs 40 mins", 160))

    while True:
        print("\n1 --> View shows")
        print("2 --> Book tickets")
        print("3 --> Cancel tickets")
        print("4 --> Quit")

        try:
            choice = int(input("Enter any number (1-4): "))
        except ValueError:
            print("Please enter a valid number (1-4).")
            continue

        if choice == 1:
            theatre.display_shows()
        elif choice == 2:
            t = input("Which show do you want to watch?: ").strip()
            try:
                n = int(input("Enter number of seats to be book: "))
            except ValueError:
                print("Please enter a valid number of seats.")
                continue
            success = theatre.book_tickets(t, n)
            if success:
                print("Booked successfully!")
        elif choice == 3:
            t = input("Show name: ").strip()
            try:
                n = int(input("Enter number of seats to cancel: "))
            except ValueError:
                print("Please enter number of seats.")
                continue
            success = theatre.cancel_tickets(t, n)
            if success:
                print("Cancelled successfully!")
        elif choice == 4:
            print("Thanks for visiting.")
            break
        else:
            print("Invalid choice.")


run_theatre()