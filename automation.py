# code to organize my downloads folder on my laptop

from pathlib import Path
import shutil

# Path to your Downloads folder
downloads = Path.home() / "Downloads"

# File categories
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp", ".webp"],
    "Documents": [".pdf", ".doc", ".docx", ".txt", ".ppt", ".pptx", ".xls", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".mov", ".avi", ".wmv"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Archives": [".zip", ".rar", ".7z", ".tar", ".gz"],
    "Programs": [".exe", ".msi"],
    "Python": [".py", ".ipynb"],
}

# Create category folders if they don't exist
for category in categories:
    (downloads / category).mkdir(exist_ok=True)

# Create an "Others" folder
(downloads / "Others").mkdir(exist_ok=True)

# Move files
for item in downloads.iterdir():

    # Ignore folders
    if item.is_dir():
        continue

    moved = False

    for category, extensions in categories.items():
        if item.suffix.lower() in extensions:
            shutil.move(str(item), str(downloads / category / item.name))
            moved = True
            break

    if not moved:
        shutil.move(str(item), str(downloads / "Others" / item.name))

print("Downloads folder organized successfully!")

