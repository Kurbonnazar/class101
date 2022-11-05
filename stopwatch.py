import time
seconds=input("enter the time in seconds: ")
def countdown(seconds):
    while seconds>0:
        mins=int(seconds/60)
        sec=int(seconds%60)
        timer=f"{mins}:{sec}"
        print(timer, end="\r")
        time.sleep(1)
        seconds=seconds-1
    print("time's up")

countdown(int(seconds))