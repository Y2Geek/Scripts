number = 0

# Ask the user for their name
name = input("Please enter your name: ")

message = f"All work and no play makes {name} a dull boy\n"

# Save message to file 1000 times
with open('dull_boy.doc', 'w') as f:
    while number <= 1000:
        f.write(message)
        number += 1
