# Get the input
english = input("What grade did you get in English?")
maths = input("What grade did you get in Maths?")
computers = input("What grade did you get in Computers?")

# Change them all to integers
a = int(english)
b = int(maths)
c = int(computers)

print("Your average grade is " + str((int(a) + int(b) + int(c)) / 3))
