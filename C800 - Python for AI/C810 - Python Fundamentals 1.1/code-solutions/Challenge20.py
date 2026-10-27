story = input("Type your story: ")
story = story.lower()

startsRight = story.startswith("once upon a time") or story.startswith("long ago in a faraway land")
hasCreature = "dragon" in story or "unicorn" in story or "fairy" in story or "wizard" in story
endsRight = story.endswith("the end")

if startsRight and hasCreature and endsRight:
    print(True)
else:
    print(False)
    if not startsRight:
        print("It does not start the right way.")
    if not hasCreature:
        print("It is missing a magical creature.")
    if not endsRight:
        print("It does not end with THE END.")
