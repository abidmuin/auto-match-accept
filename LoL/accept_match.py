import os
import threading
import requests
import time
import keyboard
import pyautogui

print("====================================")
print("Auto Match Accept Script Started!")


image_url = (
    "https://github.com/abidmuin/auto-match-accept/blob/master/LoL/accept_button.png"
)


local_image_path = "accept_button.png"

if not os.path.exists(local_image_path):
    try:
        response = requests.get(image_url)
        response.raise_for_status()

        with open(local_image_path, "wb") as image_file:
            image_file.write(response.content)

        print("Image downloaded successfully!")

    except requests.exceptions.RequestException as e:
        print(f"Failed to download image: {e}")

else:
    print("Looks like you are running the script first time.")
    print("Script will now download the image of accept button.")


check_interval = 1
confidence_level = 0.55

print("Waiting for Matchmaking..........")


def in_queue():
    while True:
        button_position = pyautogui.locateOnScreen(accept_button, confidence_level)

        if button_position:
            button_center = pyautogui.center(button_position)
            pyautogui.click(button_center)

            print("Match Found and Accepted.")
            print("GLHF on the Rift!")

            break
        else:
            print("In Queue...!")

        time.sleep(check_interval)


def key_listener():
    print("Press 'q' to stop the script.")
    keyboard.wait("q")
    print("Script stopped!")


if __name__ == "__main__":
    queue_thread = threading.Thread(target=in_queue)
    key_thread = threading.Thread(target=key_listener)

    queue_thread.start()
    key_thread.start()

    queue_thread.join()
    key_thread.join()


# pyinstaller --onefile --add-data "accept_button.png;dist/accept_button.png". accept_match.py
