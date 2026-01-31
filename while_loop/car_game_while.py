# first_prompt = "help"
# start_car = "start"
# stop_car = "stop"
# quit_game = "quit"
#
# while first_prompt == "help":
#     input("start - to start the car")
#
# else:
#     print("I dont understand that ...")

command =""
started = False
stopped = False
while True:
    command = input("> ").lower()
    if command == "start":
        if started:
            print("The car is already started")
        else:
            started = True
            print("Car started... Ready to go")

    elif command== "stop":
        if not started:
            print("Car is already stopped")
        else:
            started =False
            print("Car stopped.")
    elif command == "help":
        print("""
            start- to start the car
            stop - to stop the car
            quit - to quit
        """)
    elif command == "quit":
        break
    else:
        print("Sorry, I dont understand this")