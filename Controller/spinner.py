import time
import sys

def spinner(duration):
    frames = ["-", "/", "|", "\\"]
    delay = 0.1
    startTime = time.time()

    while time.time() - startTime< duration:
        for frame in frames:
            sys.stdout.write("\r" + frame)
            sys.stdout.flush()
            time.sleep(delay)
    # stops the spinner 
    sys.stdout.write("\r" + " " * len(frames[0]))
    sys.stdout.flush()