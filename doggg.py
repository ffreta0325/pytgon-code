def ticket3(age):
    ticketType = "children" if age < 15 else "adults" if age < 65 else "seniors"
    print(ticketType)

def test():
    ticket3(10)
    ticket3(20)
    ticket3(70)
test()