class Star_Cinema:
    hall_list = []

    def entry_hall(self, hall_data):
        Star_Cinema.hall_list.append(hall_data)


class Hall(Star_Cinema):
    def __init__(self, Hall_name, Hall_location, hall_no, rows, cols):
        self.seats = {}
        self.Hall_name = Hall_name,
        self.location = Hall_location
        self.show_list = []
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no

        self.entry_hall(self)

    def entry_show(self, show_id, movie_name, time):
        show_details = (show_id, movie_name, time)
        self.show_list.append(show_details)

        # seat_allocation = [['F' for _ in range(self.cols)] for _ in range(self.rows)]
        # self.seats[show_id] = seat_allocation

        seat_allocation = [["F" for _ in range(self.cols)] for _ in range(self.rows)]
        self.seats[show_id] = seat_allocation

    def display_hall_info(self):
        print(f"Hall No: {self.hall_no}, Rows: {self.rows}, Columns: {self.cols}")
        print(f"Seats Information: {self.seats}")
        print(f"Show List: {self.show_list}")

    def display_seats(self,show_id):
        for row in self.seats[show_id]:
            print(" ".join(row))


Cinema = Star_Cinema()
Hall1 = Hall("Purovi Hall", "Gazipur", 1, 10, 10)
Hall2 = Hall("Shurovi Hall", "Savar", 2, 20, 30)

Hall1.entry_show("ASE-123","Avengers","12.00 Am")

Cinema.entry_hall(Hall1)
Cinema.entry_hall(Hall2)

for hall in Star_Cinema.hall_list:
    hall.display_hall_info()
