import os
import pyautogui
import keyboard
from time import sleep
from PIL import ImageGrab, Image

# path setting
path = 'E:/WPS_Sync_Files/py_mouse_click/IMG/'
files = os.listdir(path)
num_png = len(files)

# Dataset of picture
Screen_Img = []
for i in range(1,num_png+1):
    temp = Image.open(path+str(i)+'.jpeg')
    Screen_Img.append(temp)
print('Successfully save, the numeber of picture is', len(Screen_Img))

# core function and if you want to stop just press 's' on keyboard
def func():
    for m in range(0,num_png):
        Img_judge = pyautogui.locateOnScreen(Screen_Img[m],grayscale=True,confidence=.9)
        if keyboard.is_pressed('s'):
            exit()
        elif Img_judge == None:
            print("can't find the same Img")
        else:
            x,y,width,height = Img_judge
            print ("The location of the Img is:X={},Y={}".format(x,y))
            # click the Img on the screen
            x+=10
            y+=10
            pyautogui.click(x,y,button='left')

if __name__ == "__main__":
    while True:
        func()