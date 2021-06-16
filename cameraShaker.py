import pyautogui
from pynput.keyboard import *
import random
import time

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
    
    # delay = random.randint(5, 10)  # in seconds

    display_controls()
    while running:
        if not pause and i < noOfClicks:
            keyToPress = random.randint(1, 2)
            amountToPress = random.randint(1, 2)
            x = 0

            if keyToPress == 1:
                print('Pressing left')
                while x <= amountToPress:
                    pyautogui.keyDown('left')
                    pyautogui.keyUp('left')
                    x += 1
                print('Finished pressing left')

            elif keyToPress == 2:
                print('Pressing right')
                while x <= amountToPress:
                    pyautogui.keyDown('right')
                    pyautogui.keyUp('right')
                    x += 1
                print('Finished pressing right')
        
            i += 1        
        
        pyautogui.PAUSE = delay


    lis.stop()


if __name__ == "__main__":
    main()