import pyautogui
from pynput.keyboard import *
import random
import time

from datetime import datetime

#  ======== settings ========
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc

#  ==========================

pause = True
running = True


def on_press(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// - Settings: ")
    print("// - Controls:")
    print("\t F1 = Resume")
    print("\t F2 = Pause")
    print("\t F3 = Exit")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    i = 0
    noOfClicks = 2000
    delay = random.randint(180, 300)  # in seconds

    display_controls()
    while running:
        if not pause and i < noOfClicks:
            keyToPress = random.randint(1, 2)
            amountToPress = random.randint(25, 50)
            x = 0

            if keyToPress == 1:
                print('Pressing left')
                for i in range(random.randint(1, 5)):
                    pyautogui.press('left', presses = amountToPress)
                print('Finished pressing left')

            elif keyToPress == 2:
                print('Pressing right')
                for i in range(random.randint(1, 5)):
                    pyautogui.press('right', presses = amountToPress)
                print('Finished pressing right, pressed it')     
            i += 1        
        
        pyautogui.PAUSE = delay

        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")

        if current_time == datetime.strptime("02:00:00", "%H:%M:%S"):
            break


    lis.stop()


if __name__ == "__main__":
    main()