from ast import Or
from itertools import count
import cv2
import numpy as np
from mss import mss
import time
import pydirectinput
import numpy as np
from regex import F
from sqlalchemy import false
import win32api
from ctypes import windll


def main():
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


            
                def point_visualizer():
                    
                    global mask
                    mask = cv2.circle(mask, (320, 320), 2, (255, 255, 255), -1)
                    mask = cv2.circle(mask, (315, 320), 2, (255, 255, 255), -1)
                    mask = cv2.circle(mask, (325, 320), 2, (255, 255, 255), -1)
                    mask = cv2.circle(mask, (315, 315), 2, (255, 255, 255), -1)
                    mask = cv2.circle(mask, (325, 325), 2, (255, 255, 255), -1)
                    mask = cv2.circle(mask, (325, 315), 2, (255, 255, 255), -1)
                    mask = cv2.circle(mask, (315, 325), 2, (255, 255, 255), -1)
                    cv2.imshow('ai mask - press q to quit', mask)
                    return mask
                        
                point_visualizer()

                if cv2.waitKey(1) == ord('q'):
                    cv2.destroyAllWindows()
                    break
                

    
if __name__ == '__main__':

    main()
