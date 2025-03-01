
# Vortex Mod Manager Collection Auto-Downloader

This script automates the process of downloading collections from the Vortex Mod Manager using the `pyautogui` library to interact with the graphical interface. It locates download buttons on the screen and clicks them automatically, as defined in the provided image list.

## Requirements

You can install the required dependencies by running:

```bash
pip install -r requirements.txt
```

## How to Use

1. **Prepare the button images**: The script requires images of download buttons to interact with the Vortex interface. Place the images in PNG format in the project folder (e.g., `first_download_button.png` and `second_download_button.png`).
   
2. **Configure the script**: Add the paths to the button images in the `file_list` section of the script. You can also adjust the `timeout` parameter to set how long the script can remain idle.

3. **Run the script**: 

```bash
python download_mods.py
```

The script will search for the download buttons on the screen and click them automatically. The script checks for the buttons every 2 seconds and resets the runtime each time a button is clicked. If the runtime exceeds the defined `timeout`, the script will stop.

## Disabling the File Rating Reminder in Vortex

To prevent the Vortex Mod Manager from showing the "file ratings" reminder, follow these steps:

1. **Open the Nexus Mods website.**
2. **Click on your profile and go to "Site preferences".**
3. **Change the value of the label "Remind me about file ratings" to "Never".**

![Disable file rating reminder](https://i.imgur.com/IlbO4Gu.png)

This script works best when the endorsement reminder is disabled, as it prevents interruptions during the automation process.

## Notes

- Ensure that the Vortex Mod Manager window is visible and in a fixed position on the screen for the script to work correctly.
- The image location confidence can be adjusted in the function `locate_image(image, confidence=0.9)` if needed.
