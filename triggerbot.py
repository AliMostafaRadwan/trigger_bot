# from ast import Or
# from itertools import count
import cv2
import numpy as np
from mss import mss
import time
# import pydirectinput
import numpy as np
# from regex import F
# from sqlalchemy import false
import win32api
# from ctypes import windll
# import sys

#windll.user32.MessageBoxW(0, "Press Q to quit", "Triggerbot", 1)

def main():


    # visualizeing true/false to see the ai vision !may effect on the hack performance
    visualize = True # will effect on the gui file

    # if capslock is pressed activate the trigger
    toggle_key = 0x14

    #prints the fps
    show_fps = False


    print('running...')



    while win32api.GetAsyncKeyState(ord('Q')) == 0:
        
        with mss() as sct:
            # Defining the area of the screen that the program will be looking at.
            monitor = {"top": 220, "left": 640, "width": 640, "height":640}



            while True:
                Start_time =time.time()
                # Taking a screenshot of the area defined in the monitor variable.
                screenshot = np.array(sct.grab(monitor))


                # Converting the screenshot from RGB to HSV.
                screenshot = cv2.cvtColor(screenshot, cv2.COLOR_RGB2HSV)

                # Defining the lower and the upper bound of the color range that the program will be looking for.
                lower_bound = np.array([135, 100, 100])
                upper_bound = np.array([164, 255, 255])

                # Creating a mask of the pixels that are within the range of the lower and upper bound.
                global mask
                mask = cv2.inRange(screenshot, lower_bound, upper_bound)


                # Getting the RGB values of the pixel at the coordinates (320,320)
                rgb_Mscreen = screenshot[320,320]
                rgb_Lscreen = screenshot[320,315]
                rgb_Rscreen = screenshot[320,325]
                rgb_URscreen = screenshot[325,325]
                rgb_ULscreen = screenshot[315,315]
                rgb_URDscreen = screenshot[315,325]
                rgb_ULDscreen = screenshot[320,315]


                # if capslock is pressed activate the code

                if win32api.GetKeyState(toggle_key) and (rgb_Mscreen[0] in np.arange(135, 164) and rgb_Mscreen[1] in np.arange(100, 225) and rgb_Mscreen[2] in np.arange(100, 255) or rgb_Rscreen[0] in np.arange(135, 164) and rgb_Rscreen[1] in np.arange(100, 225) and rgb_Rscreen[2] in np.arange(100, 255) or rgb_Lscreen[0] in np.arange(135, 164) and rgb_Lscreen[1] in np.arange(100, 225) and rgb_Lscreen[2] in np.arange(100, 255) or rgb_URscreen[0] in np.arange(135, 164) and rgb_URscreen[1] in np.arange(100, 225) and rgb_URscreen[2] in np.arange(100, 255) or rgb_ULscreen[0] in np.arange(135, 164) and rgb_ULscreen[1] in np.arange(100, 225) and rgb_ULscreen[2] in np.arange(100, 255) or rgb_URDscreen[0] in np.arange(135, 164) and rgb_URDscreen[1] in np.arange(100, 225) and rgb_URDscreen[2] in np.arange(100, 255) or rgb_ULDscreen[0] in np.arange(135, 164) and rgb_ULDscreen[1] in np.arange(100, 225) and rgb_ULDscreen[2] in np.arange(100, 255)):
                    # pydirectinput.click()
                    print("Detected")
                
                
                # cv2.imshow('Computer Vision', screenshot)
                def visualizer():
                    if visualize:
                        global mask
                        mask = cv2.circle(mask, (320, 320), 2, (255, 255, 255), -1)
                        mask = cv2.circle(mask, (315, 320), 2, (255, 255, 255), -1)
                        mask = cv2.circle(mask, (325, 320), 2, (255, 255, 255), -1)
                        mask = cv2.circle(mask, (315, 315), 2, (255, 255, 255), -1)
                        mask = cv2.circle(mask, (325, 325), 2, (255, 255, 255), -1)
                        mask = cv2.circle(mask, (325, 315), 2, (255, 255, 255), -1)
                        mask = cv2.circle(mask, (315, 325), 2, (255, 255, 255), -1)
                        cv2.imshow('ai mask', mask)
                    return mask
                        
                visualizer()

                if cv2.waitKey(1) == ord('q'):
                    cv2.destroyAllWindows()
                    break
                if show_fps:
                    print("FPS: ", 1.0 / (time.time() - Start_time))




if __name__ == '__main__':

    main()

