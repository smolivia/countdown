import time

def countdown(t):
    print("\n----------------------Countdown----------------------")
    while(t > 0):
        # calculate minutes and seconds from total time remaining in seconds
        mins = int(t / 60)
        secs = int(t % 60)
        # print minutes and seconds remaining, overwriting the previous line each time
        # time is formatted to have two spaces, only show ints, and show 0 if there is no value
        print("{min:02d}:{sec:02d}".format(min = mins, sec = secs), end='\r')
        # pause the timer for one second before updating the total time remaining in seconds
        time.sleep(1)
        t -= 1
    print("00:00")
    # show user that countdown has completed
    print("Countdown completed.")
    # ask to start another countdown and run get user input if yes
    user = input("Start another countdown? type 'y' for yes and anything else to exit: ")
    if user == 'y':
        getUserInput()


def getUserInput():
    user = input("""
-------------------Set a Countdown-------------------
Would you like to enter your countdown time in seconds only?
type 'y' to enter your countdown only in seconds
type 'n' to enter seconds and minutes separately
""")
    # display two different methods based on the way the user would like to enter their countdown value
    # after the user enters their preferred method and countdown value, run the main countdown function
    if user == 'y':
        t = input("\nEnter the length of your countdown in seconds: ")
        countdown(int(t))
    elif user == 'n':
        mins = int(input("\nEnter the length of minutes of your countdown: "))
        secs = int(input("Enter the length of seconds of your countdown: "))
        t = mins * 60 + secs
        countdown(int(t))
    else: # the value is not valid. ask the user to input the method they would like to enter their countdown again
        print("""
------------------------ERROR------------------------
That was not a valid answer. Please try again.
------------------------ERROR------------------------""")
        getUserInput()

# start the countdown program by asking for the user's input
getUserInput()

