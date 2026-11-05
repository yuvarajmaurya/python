
nextTicket = 10000;
nextSeat = 1;
tickets = {}
fare = 500


def bookTicket() :
    global nextTicket, nextSeat ;
    print("\n ----- BOOK TRAIN TICKET -----\n");
    while True :
        count = int(input(" How Many Passengers : "))
        if count <= 0 :
            print("\n --------- INVALID INPUT! ----------")
            print(" PASSENGER COUNT MUST BE ATLEAST ONE. \n")
        else :
            break
    passengers = [] # Empty List
    for i in range( 1, count + 1):
        print("\n Passenger : ",i)
        name = input(" Enter Name : ")
        age = int(input(" Enter Age  : "))
        passengers.append({"name" : name, "age" : age, "seat" : nextSeat})
        nextSeat += 1
    password = input("\n Set a Password : ")
    ticketId = nextTicket
    nextTicket += 1
    tickets[ticketId] = {"password" : password, "passengers" : passengers}
    print("\n Booked! \n Ticket ID  : ", ticketId)
    print(" Total Fare : ₹" + str(count * fare))


def viewTicket() :
 print("\n ----- VIEW TICKET ----- \n");
 ticketId = int(input(" Enter Ticket ID : "))
 password = input(" Enter Password  : ")
 if ticketId in tickets :
    ticket = tickets[ticketId]
    if ticket["password"] == password :
       print("\n ---- Ticket No :", ticketId, "----")
       n = 1
       for p in ticket["passengers"]:
        print("",str(n) + ")",p["name"], ", Age", p["age"], ", seat :", p["seat"])
        n += 1
       total = len(ticket["passengers"]) * fare
       print(" Total Fare : ₹", total)
    else :
        print("\n ----- Wrong Password -----")
 else :
     print(" Ticket ID Not Found !!!")

def cancelTicket() :
    print("\n ---- CANCEL TRAIN TICKET ---- \n");
    ticketId = int(input(" Enter Ticket ID : "))
    password = input(" Enter Password : ")
    if ticketId in tickets :
        ticket = tickets[ticketId]
        if ticket["password"] == password :
            del tickets[ticketId]
            print("\n --- Ticket", ticketId, "Cancelled --- ")
        else :
            print(" Wrong Password!!!")
    else :
        print(" Ticket ID Not Found !!!")


while True :
    print("\n _________________________________\n")
    print("\n ----- TICKET BOOKING SYSTEM -----\n");
    print(" 1. Book train ticket.");
    print(" 2. view   ticket.");
    print(" 3. cancel ticket.");
    print(" 4. Exit.\n");

    op = int(input(" Enter option : "));
    if   (op == 1) :
       bookTicket();
    elif (op == 2) :
       viewTicket();
    elif (op == 3) :
       cancelTicket();
    elif (op == 4) :
       break;
    else :
      print("\n  Invalid Option !!!");
      print("  ---- Try Again ----")









