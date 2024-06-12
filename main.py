from PIL import ImageGrab
import datetime
import time
import os

def grabScreenFunc():
    screenGrab = ImageGrab.grab(None, True, True)

    fileName = datetime.datetime.now().strftime("./captures/%Y-%m-%dT%H-%M-%S.png")

    screenGrab.save(fileName, 'PNG')

if not os.path.exists("./captures"):
    os.makedirs("./captures")

while(True):
    grabScreenFunc()
    # Capturing Screen every 30 seconds
    time.sleep(30)