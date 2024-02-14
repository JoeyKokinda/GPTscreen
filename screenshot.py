import win32clipboard
from io import BytesIO
from PIL import Image, ImageGrab
import tkinter as tk

def take_screenshot():
    # Captures the screen
    screenshot = ImageGrab.grab()
    # Convert the screenshot to a format that can be copied to clipboard
    output = screenshot.convert("RGB")
    with BytesIO() as output:
        screenshot.save(output, "BMP")
        data = output.getvalue()[14:]
    # Open the clipboard
    win32clipboard.OpenClipboard()
    # Empty the clipboard
    win32clipboard.EmptyClipboard()
    # Set the clipboard data
    win32clipboard.SetClipboardData(win32clipboard.CF_DIB, data)
    # Close the clipboard
    win32clipboard.CloseClipboard()
    print("Screenshot taken and copied to clipboard")

# Create the main window
root = tk.Tk()
root.title("Screenshot Tool")

# Create a button and attach the screenshot function
button = tk.Button(root, text="Take Screenshot", command=take_screenshot)
button.pack(pady=20)

# Run the application
root.mainloop()