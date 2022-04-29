from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import keyboard
import os

# path setting
path = 'E:\WPS_Sync_Files\py_mouse_click'
files = os.listdir(path)
num_png = len(files)-2

# Dataset of picture
Screen_Img = []
for i in range(1,num_png):
    temp = Image.open(str(i)+'.jpeg')
    Screen_Img.append(temp)
print('Successfully save, the numeber of picture is', len(Screen_Img))

# run code and if you want to stop, just press 's' on keyboard
while True:
    if keyboard.is_pressed('s'):
        break
    for m in range(0,num_png-1):
        Img_judge = pyautogui.locateOnScreen(Screen_Img[m],grayscale=True,confidence=.9)
        if Img_judge == None:
            print("can't find the same Img")
        else:
            x,y,width,height = Img_judge
            print ("The location of the Img is:X={},Y={}".format(x,y))
            # click the Img on the screen
            x+=10
            y+=10
            pyautogui.click(x,y,button='left')
