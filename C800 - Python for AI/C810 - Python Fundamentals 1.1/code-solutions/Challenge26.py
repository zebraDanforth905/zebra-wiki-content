import random

money = int(input("How much money do you have? "))
action = random.randint(1, 5)

match action:
    case 1:
        money = money + 10
        print("You found $10! You now have $" + str(money))
    case 2:
        money = money - 5
        print("You lost $5! You now have $" + str(money))
    case 3:
        money = money * 2
        print("You doubled your money! You now have $" + str(money))
    case 4:
        money = 0
        print("You lost it all! You now have $" + str(money))
    case 5:
        print("Nothing happened. You still have $" + str(money))
