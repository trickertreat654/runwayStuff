import pyautogui
import time

# Coordinates of the section you want to click on (replace with actual coordinates)
x, y = 1067, 1050

# Infinite loop to click every minute
while True:
    # Move the mouse to the specified coordinates and click
    pyautogui.click(x, y)
    print(f"Clicked at ({x}, {y})")

    # Wait for 60 seconds before the next click
    time.sleep(45)
