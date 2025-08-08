import os
import shutil

def organize_files(directory):
    if not os.path.isdir(directory):
        print(f"Directory '{directory}' does not exist.")
        return

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            file_extension = filename.split('.')[-1].lower()
            
            # Create a new directory for the file type if it doesn't exist
            new_folder_path = os.path.join(directory, file_extension.upper())
            if not os.path.exists(new_folder_path):
                os.makedirs(new_folder_path)
            
            # Move the file to the new directory
            shutil.move(file_path, os.path.join(new_folder_path, filename))
            print(f"Moved '{filename}' to '{file_extension.upper()}' folder.")

# Use os.path.expanduser('~/Downloads') to get the correct path automatically
target_directory = os.path.expanduser('~/Downloads')
organize_files(target_directory)