cake_width = int(input())
cake_length = int(input())
cake_pieces = cake_length * cake_width

command = input()
while not command == "STOP":
    pieces_ordered = int(command)
    cake_pieces -= pieces_ordered
    if cake_pieces <= 0:
        break

    command = input()

if cake_pieces > 0:
    print(f"{cake_pieces} pieces are left.")
else:
    print(f"No more cake left! You need {abs(cake_pieces)} pieces more.")
