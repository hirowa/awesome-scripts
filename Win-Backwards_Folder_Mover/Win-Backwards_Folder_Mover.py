import os
import shutil

# Define the root directory
root_directory = os.getcwd()  # Use the current directory as the root

# Function to move files up one level and delete the folder
def move_files_up_and_delete(folder_path):
    # Get the parent directory of the current folder
    parent_directory = os.path.dirname(folder_path)
    
    # List all files and folders in the target directory
    for item in os.listdir(folder_path):
        item_path = os.path.join(folder_path, item)
        
        # Move the file or folder to the parent directory
        shutil.move(item_path, parent_directory)
        print(f'Moved: {item_path} to {parent_directory}')
    
    # Remove the empty folder after moving its contents
    os.rmdir(folder_path)
    print(f'Deleted folder: {folder_path}')

# Walk through the directory structure
for dirpath, dirnames, filenames in os.walk(root_directory, topdown=False):
    # Move files up one level for all subdirectories
    if dirpath != root_directory:  # Skip the root directory itself
        move_files_up_and_delete(dirpath)

print("Process completed!")
