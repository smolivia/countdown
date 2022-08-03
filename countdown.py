import time

def countdown(t):
    print("\n----------------------Countdown----------------------")
    while(t > 0):
        mins = int(t / 60)
        secs = int(t % 60)
        print("{min:02d}:{sec:02d}".format(min = mins, sec = secs), end='\r')
        time.sleep(1)
        t -= 1
    print("00:00")
    print("Countdown completed.")
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

    if user == 'y':
        t = input("\nEnter the length of your countdown in seconds: ")
        countdown(int(t))
    elif user == 'n':
        mins = int(input("\nEnter the length of minutes of your countdown: "))
        secs = int(input("Enter the length of seconds of your countdown: "))
        t = mins * 60 + secs
        countdown(int(t))
    else:
        print("""
------------------------ERROR------------------------
That was not a valid answer. Please try again.
------------------------ERROR------------------------""")
        getUserInput()

getUserInput()

