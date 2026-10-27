height = int(input("How tall are you in inches? "))

print("You are allowed on these rides:")

if height >= 40:
    print("Tree Top Adventure, Taxi Jam, Sugar Shack")
if height >= 48:
    print("Vortex, Lumber Jack, Flying Canoes")
if height >= 54:
    print("Flight Deck, Behemoth, Leviathan")

if height < 40:
    print("Sorry, you are too short for any of the rides.")
