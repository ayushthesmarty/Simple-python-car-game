help_ = """
The are the commands of the game
help - show the commands
start - start the car
stop - stop the car
exit - exit the game
"""

print(help_)

running = True
car_run = False

while running:
    command = input("Your command: ").lower()

    if command == "help":
        print(help_)

    elif command == "start":
        if not car_run:
            car_run = True

            print("Starting car!!\n")

            print("The car is started!!")

        else:
            print("Starting car!!\n")

            print("The car is already started!!")

    elif command == "stop":
        if car_run:
            car_run = False

            print("Stopping car!!\n")

            print("The car is stopped!!")

        else:
            print("Stopping car!!\n")

            print("The car is already stopped!!")

    elif command == "exit":

        exit_run = True
        while exit_run:
            input_ = input("Do you want to exit the game? (y or n) ").lower()
            if input_ == "y":
                print("Bye, Bye!")

                exit()

            elif input_ == "n":
                break

            else:
                print("I don't recognize this command!!!")


    else:
        print("I don't recognize this command!!!")
        