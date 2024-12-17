import os
import re

def replace_tags_in_md_files(folder_path, old_tag, new_tag):
    """
    Replace a specific tag in all .md files within a folder and its subfolders.

    :param folder_path: Path to the folder containing .md files
    :param old_tag: The tag to be replaced
    :param new_tag: The new tag to replace the old one
    """
    # Walk through the folder and its subfolders
    for root, _, files in os.walk(folder_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)

            # Check if the file is an .md file
            if file_name.endswith('.md'):
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()

                # Replace the old tag with the new tag and remove numeric values
                updated_content = re.sub(rf"{re.escape(old_tag)}\s*\d*", new_tag, content)

                # Remove standalone numeric lines
                updated_content = re.sub(r"(?m)^\s*\d+\s*$", "", updated_content)

                # Remove lines with non-alphanumeric characters or standalone hyphens
                updated_content = re.sub(r"(?m)^\s*[-\w]*[-\d]*\s*$", "", updated_content)

                # Write the updated content back to the file
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(updated_content)

                print(f"Updated tags in: {file_path}")

if __name__ == "__main__":
    # Get user input for folder path
    folder_path = input("Enter the path to the folder containing .md files: ").strip().strip('"').strip("'")
    old_tag = "Date: "
    new_tag = ""

    # Run the function
    replace_tags_in_md_files(folder_path, old_tag, new_tag)
