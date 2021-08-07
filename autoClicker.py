import pyautogui
from pynput.keyboard import *
import random

#  ======== settings ========
delay = random.randint(1, 2)  # in seconds
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
    print("\t delay = " + str(delay) + ' sec' + '\n')
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

    display_controls()
    while running:
        delay = random.randint(1, 2)  # in seconds
        if not pause and i < noOfClicks:

            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
            
            i += 1
    
    lis.stop()


if __name__ == "__main__":
    main()