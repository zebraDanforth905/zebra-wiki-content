message = input("Enter your message: ")

print("Your message is " + str(len(message)) + " characters long.")

message = message.replace(" ", "")
print("Without spaces: " + message)

if "urgent" in message.lower():
    print("This is an urgent message!")
else:
    print("This is not an urgent message.")
