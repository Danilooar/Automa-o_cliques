import pyautogui
from time import sleep

print("Iniciando o monitoramento do mouse...")


"""while True: 
    currentMouseX, currentMouseY = pyautogui.position() 
    print(currentMouseX, currentMouseY)
    sleep(3)"""
    
pyautogui.click(x=1255, y=16)
sleep(3)

while True:

  pyautogui.click(x=177,y=633)
  sleep(3)

  pyautogui.click(x=842,y=653)
  sleep(3)

  pyautogui.click(x=850,y=153)
  sleep(3)
  
  