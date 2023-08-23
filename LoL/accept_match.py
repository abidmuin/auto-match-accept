import pyautogui
import time

print("====================================")
print("Auto Match Accept Script Started!")
print("Waiting for Matchmaking..........")

check_interval = 1

while True:
    button_position = pyautogui.locateOnScreen('accept_button.png', confidence=0.55)
    
    if button_position:
        button_center = pyautogui.center(button_position)
        pyautogui.click(button_center)
        
        print("Match Found and Accepted.")
        print("GLHF on the Rift!")
        
        break
    else:
        print("In Queue...!")
    
    time.sleep(check_interval)