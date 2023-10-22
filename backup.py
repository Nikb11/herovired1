import shutil
import os
from datetime import datetime
import sys


def backup_files(source_folder, dest_folder):
    if not os.path.exists(source_folder) or not os.path.exists(dest_folder):
        print("Folder not present.")
        return

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_path = os.path.join(root, file)
            dest_path = os.path.join(dest_folder, file)

            if os.path.exists(dest_path):
                timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
                filename, file_extension = os.path.splitext(file)
                new_filename = f"{filename}_{timestamp}{file_extension}"
                dest_path = os.path.join(dest_folder, new_filename)

            shutil.copy2(source_path, dest_path)
            print(f"File backup done: {file} to {dest_path}")

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Usage: python backup.py <source_directory> <destination_directory>")
    else:
        source_directory = sys.argv[1]
        destination_directory = sys.argv[2]
        backup_files(source_directory, destination_directory)
