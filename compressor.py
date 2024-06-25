import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
img = Image.open(file_path)
myHeight, myWidth = img.size

img = img.resize((myHeight, myWidth), Image.Resampling.LANCZOS)

# Convert image to RGB mode if it's in RGBA
if img.mode == 'RGBA':
    img = img.convert('RGB')

save_path = asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", ".jpg"), ("All files", ".*")])

# Save with compression
img.save(save_path + "_compressed.jpg", quality=20)  # Adjust quality as needed (lower value means more compression)
print("Image compressed successfully!")