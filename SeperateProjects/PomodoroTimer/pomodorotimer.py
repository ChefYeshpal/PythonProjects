'''
This is a pomodoro timer that will be linked to a html file to help it get published on the web
its requirements are:
    1. requires user input for work and break time
    2. shows the time expired


created: 2023-09-16 22:04:55

log:
2023-09-16 22:16:19 created this file and wrote the code


last modified:

2023-09-16 22:15:57 Created this file and made the code


'''



import time

def pomodoro_timer(totalcycles):
    for cycle in range(totalcycles):
        workduration = int(input(f"Cycle {cycle + 1} - Enter work duration (in minutes): ")) * 60
        breakduration = int(input("Enter break duration (in minutes): ")) * 60

        print(f"Cycle {cycle + 1} - Work")
        countdown(workduration)
        if cycle < totalcycles - 1:
            print("Take a break!")
            countdown(breakduration)
            print("Back to work!")

    print("Pomodoro timer completed!")

def countdown(seconds):
    while seconds:
        mins, secs = divmod(seconds, 60)
        timeformat = f"{mins:02d}:{secs:02d}"
        print(timeformat, end="\r")
        time.sleep(1)
        seconds -= 1
    print("00:00")

if __name__ == "__main__":
    totalcycles = int(input("Enter the number of Pomodoro cycles: "))
    pomodorotimer(totalcycles)
