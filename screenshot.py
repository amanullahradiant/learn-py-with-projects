import time
import pyautogui

def screenshot():
  # Generate a unique name based on the current timestamp
  name = int(round(time.time() * 1000))
  filename = f"F:/Aman/python/projects/screenshots/{name}.png"

  print("Prepare for the screenshot! 5 seconds...")
  time.sleep(3)  # Give time to arrange the screen for the screenshot

  # Take the screenshot and save it
  image = pyautogui.screenshot()
  image.save(filename)  # Save with the generated name
  print(f"Screenshot saved as {filename}")

  # Display the screenshot (optional)
  image.show()


  """
  save_path = "F:\\Aman\\screenshots\\"  # Update with your desired path
  name = f"F:/Aman/python/projects/screenshots/{name}.png"
  filename = save_path + filename
  image.save(filename)
  """

screenshot()