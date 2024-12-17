import os
import shutil

def copy_files_with_extension(extension, input_folder, output_folder):
    # Ensure the output folder exists
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files_copied = 0

    # Walk through all directories and subdirectories
    for root, dirs, files in os.walk(input_folder):
        for file in files:
            if file.endswith(extension):
                full_file_path = os.path.join(root, file)
                destination_path = os.path.join(output_folder, file)
                print(f"Copying {full_file_path} to {destination_path}")
                shutil.copy(full_file_path, destination_path)
                files_copied += 1

    return files_copied

def sanitize_path(path):
    # Remove leading and trailing quotation marks
    return path.strip("\"'")

if __name__ == "__main__":
    extension = input("Enter the file extension (e.g., '.txt'): ").strip()
    input_folder = sanitize_path(input("Enter the path of the input folder: "))
    output_folder = sanitize_path(input("Enter the path of the output folder: "))

    files_copied = copy_files_with_extension(extension, input_folder, output_folder)

    if files_copied == 0:
        print("No files were found with the given extension.")
    else:
        print(f"{files_copied} files with the extension {extension} have been copied from {input_folder} to {output_folder}.")