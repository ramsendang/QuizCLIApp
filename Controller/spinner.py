import time
import sys

def spinner(duration):

    spinnerframes = ["-", "/", "|", "\\"]
    delay = 0.05
    startTime = time.time()
    # Starts the spinner by printing the character in Spinnerframes variable
    while time.time() - startTime< duration:
        for frame in spinnerframes:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(delay)
    # stops the spinner 
    sys.stdout.write("\r" + " " * len(spinnerframes[0]))
    sys.stdout.flush()