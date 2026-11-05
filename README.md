# Python Practice

My Python practice projects, written and run on my phone using Termux and Neovim.

## Projects

| Project | Description |
|---------|-------------|
| [train-ticket](train-ticket) | Command-line train ticket booking system |

---

## Train Ticket Booking System

A simple command-line program to book, view and cancel train tickets for multiple passengers. It uses only plain Python: dictionaries, lists, loops and functions. No libraries are needed.

### Features

- Book one ticket for many passengers
- Each ticket gets a unique Ticket ID, starting from 10000
- Every passenger gets their own seat number
- Total fare is calculated automatically (Rs. 500 per passenger)
- Set a password when booking
- View a ticket only with the correct Ticket ID and password
- Cancel a ticket only with the correct Ticket ID and password

### How to run

```
cd train-ticket
python ticket.py
```

### Menu

```
1. Book train ticket
2. View ticket
3. Cancel ticket
4. Exit
```

### How the data is stored

All bookings are kept in one dictionary called `tickets`. The key is the Ticket ID, and the value holds the password and the list of passengers.

```
tickets = {
    10000: {
        "password": "abc",
        "passengers": [
            {"name": "Ravi", "age": 30, "seat": 1},
            {"name": "Anita", "age": 28, "seat": 2},
        ],
    }
}
```

Data is stored in memory only, so all tickets are erased when the program exits.

### What I learned

- Dictionaries and lists (a list inside a dictionary)
- Functions and the `global` keyword
- Loops, `if / else` and counters
- Checking a password before showing or deleting data

### Future ideas

- Cancel only specific passengers
- Handle wrong input, such as letters instead of numbers
- Save tickets to a file so they are not lost
- Add train names and travel dates

---

Made by Yuvaraj Maurya
