import os
import time
from pathlib import Path
from PIL import Image
import pillow_heif

# Register HEIC support
pillow_heif.register_heif_opener()

WATCH_FOLDER = Path.home() / "Downloads"
CHECK_INTERVAL = 5  # seconds

def convert_image(file_path):
    try:
        img = Image.open(file_path)
        rgb_img = img.convert("RGB")
        new_path = file_path.with_suffix(".jpg")
        rgb_img.save(new_path, "JPEG")
        print(f"Converted: {file_path.name} → {new_path.name}")
        file_path.unlink()  # Optional: delete original
    except Exception as e:
        print(f"Failed to convert {file_path.name}: {e}")

def monitor_folder():
    print(f"Watching {WATCH_FOLDER} for HEIC/WebP files...")
    seen = set()
    while True:
        for file in WATCH_FOLDER.glob("*"):
            if file.suffix.lower() in [".heic", ".webp"] and file not in seen:
                convert_image(file)
                seen.add(file)
        time.sleep(CHECK_INTERVAL)

if __name__ == "__main__":
    monitor_folder()