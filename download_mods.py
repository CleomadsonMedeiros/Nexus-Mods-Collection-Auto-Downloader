import pyautogui
import time

file_list = [
        "first_download_button.png", 
        "second_download_button.png", 
]

def locate_image(image):
        try:
                coordinates = pyautogui.locateOnScreen(image, confidence=0.9) # Here you can adjust the confidence level
                if coordinates is not None:
                        pyautogui.moveTo(coordinates)
                        pyautogui.click()
                        return True
        except pyautogui.ImageNotFoundException:
                pass
        return False

# Adjust the timeout value to your needs
timeout = 3600

start_time = time.time()

print(f"Script Started. Timeout set to {timeout} seconds.")

while True:
        for image in file_list:
                if locate_image(image):
                        start_time = time.time()

        if time.time() - start_time > timeout:
                print("Timeout reached. Exiting script.")
                break
        time.sleep(2)