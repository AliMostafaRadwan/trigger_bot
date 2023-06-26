import torch
import cv2
import numpy as np
from mss import mss
import time
import mouse
import math
import win32api, win32con, win32gui
import keyboard
import pyautogui
import pydirectinput

def start():
    

    model = torch.hub.load(r'D:\programming\Val_AIM\yolov5-master', 'custom', path=r'sources\best2.pt', source='local')
    
    with mss() as sct:
        monitor = {"top": 220, "left": 640, "width": 640, "height":640}
    
        while(True):
            Start_time =time.time()
            screenshot = np.array(sct.grab(monitor))
            results = model(screenshot, size=640)
            df= results.pandas().xyxy[0]
            try:
                xmin = int(df.iloc[0,0])
                ymin = int(df.iloc[0,1])
                xmax = int(df.iloc[0,2])
                ymax = int(df.iloc[0,3])
                
                
        
                cv2.rectangle(screenshot, (xmin, ymin), (xmax, ymax), (255,0,0), 2)
            except:
                print("",end="")
            
            model.conf = 0.4
 
            # READING OUTPUT FROM MODEL AND DETERMINING DISTANCES TO ENEMIES FROM CENTER OF THE WINDOW
            # Get number of enemies / num of the rows of .xyxy[0] array
            #print("Enemy Number: ", enemyNum)
            
            rl = results.xyxy[0].tolist()
            print(rl)

            # if any results are found, do something
            if len(rl) > 0:
                #if confidence is high enough
                if rl[0][4] > 0.25:
                    if rl[0][1] >= 0:
                        #get xmax and ymax
                        x = int(rl[0][2])
                        y = int(rl[0][3])
                        #get distance from center of the window
                        # def getDistance(x, y):
                        #     return math.sqrt(((x - (monitor['width'] / 2)) ** 2) + ((y - (monitor['height'] / 2)) ** 2))
                        
                        width = int(rl[0][2]) - int(rl[0][0])
                        print('width: ',width)
                        height = int(rl[0][3]) - int(rl[0][1])
                        print('height: ',height)
                        xpos = int(.20 * ((x - (width/2)) - pyautogui.position()[0]))
                        ypos = int(.27 * ((y - (height/2)) - pyautogui.position()[1]))
                        pydirectinput.moveRel(xpos, ypos)
                        #pyautogui.click(.20,,.27)
                        pydirectinput.moveRel(-xpos, -ypos)

                    


            cv2.imshow("frame", screenshot)
            if(cv2.waitKey(1) == ord('q')):
                cv2.destroyAllWindows()
                break
           #print("FPS: ", 1.0 / (time.time() - Start_time))
if __name__ == '__main__':
    
    start()