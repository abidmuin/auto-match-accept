import os
import threading
import requests
import time
import keyboard
import pyautogui


class AutoMatchAccept:
    IMAGE_URL = "https://github.com/abidmuin/auto-match-accept/blob/master/LoL/accept_button.png"
    LOCAL_IMAGE_PATH = "accept_button.png"
    CHECK_INTERVAL = 1
    CONFIDENCE_LEVEL = 0.55

    @staticmethod
    def download_image():
        if not os.path.exists(AutoMatchAccept.LOCAL_IMAGE_PATH):
            try:
                response = requests.get(AutoMatchAccept.IMAGE_URL)
                response.raise_for_status()

                with open(AutoMatchAccept.LOCAL_IMAGE_PATH, "wb") as image_file:
                    image_file.write(response.content)

                print("Image downloaded successfully!")

            except requests.exceptions.RequestException as e:
                print(f"Failed to download image: {e}")
                return False

        return True

    @staticmethod
    def accept_match():
        button_position = pyautogui.locateOnScreen(
            AutoMatchAccept.LOCAL_IMAGE_PATH, AutoMatchAccept.CONFIDENCE_LEVEL
        )

        if button_position:
            button_center = pyautogui.center(button_position)
            pyautogui.click(button_center)

            print("Match found and accepted.")
            print("GLHF on the Rift!")

            return True

        print("In Queue...!")

        return False

    @staticmethod
    def key_listener():
        print("Press 'q' to stop the script.")
        keyboard.wait("q")
        print("Script stopped!")


if __name__ == "__main__":
    auto_match_accept = AutoMatchAccept()

    if auto_match_accept.download_image():
        queue_thread = threading.Thread(target=auto_match_accept.accept_match)
        key_thread = threading.Thread(target=auto_match_accept.key_listener)

        queue_thread.start()
        key_thread.start()

        queue_thread.join()
        key_thread.join()
