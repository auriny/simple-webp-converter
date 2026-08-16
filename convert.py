import os
from PIL import Image

TARGET_WIDTH = 1920
QUALITY = 80
DIRECTORY = '.'

for filename in os.listdir(DIRECTORY):
    if not filename.lower().endswith('.png'):
        continue

    filepath = os.path.join(DIRECTORY, filename)
    with Image.open(filepath) as img:
        ratio = TARGET_WIDTH / img.width
        target_height = int(img.height * ratio)

        resized = img.resize((TARGET_WIDTH, target_height), Image.Resampling.LANCZOS)
        
        new_filename = f"{os.path.splitext(filename)[0]}.webp"
        resized.save(new_filename, 'webp', quality=QUALITY)
        print(f"Compressed: {filename} -> {new_filename}")
