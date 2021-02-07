width = int(input())  # The number is in meters
length = int(input())  # The number is in meters
height = int(input())  # The number is in meters

# The free space is in cubic meters!
free_space = height * length * width

there_is_free_space = True
command = input()
while not command == "Done":
    packages_count = int(command)  # One package is with measurements 1x1x1 = 1 cubic meter!
    free_space -= packages_count
    if free_space <= 0:
        there_is_free_space = False
        break

    command = input()

if there_is_free_space:
    print(f"{free_space} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(free_space)} Cubic meters more.")
