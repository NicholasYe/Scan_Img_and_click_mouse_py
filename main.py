from time import sleep
import pyautogui
from PIL import ImageGrab, Image
import keyboard

# Screen short in advance and save it as template
Screen_Img= Image.open("screen.jpeg")
msg = pyautogui.locateOnScreen(Screen_Img, grayscale=True,confidence=.9)

# run code and if you want to stop, just press 's' on keyboard
while True:
    if keyboard.is_pressed('s'):
        break
    elif msg == None:
        print("can't find the same Img")
    else:
        x,y,width,height=msg
        print ("The location of the Img is:X={},Y={}".format(x,y))
        # click the Img on the screen
        x+=10
        y+=10
        pyautogui.click(x,y,button='left')
