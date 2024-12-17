import os


def merge_markdown_files():
    # Get the current working directory
    base_dir = os.getcwd()

    # Walk through all subdirectories
    for root, _, files in os.walk(base_dir):
        # Skip the root folder to avoid reprocessing merged files
        if root == base_dir:
            continue

        # Collect markdown files in the current subdirectory
        markdown_files = [file for file in files if file.endswith('.md')]

        if markdown_files:
            merged_content = []

            for file in markdown_files:
                file_path = os.path.join(root, file)

                # Add the filename as a title separator
                merged_content.append(f"# {file}\n")

                # Read the file content
                with open(file_path, 'r', encoding='utf-8') as f:
                    merged_content.append(f.read())

                # Add a newline to separate content between files
                merged_content.append('\n')

            # Merge all the collected content into a single string
            merged_text = '\n'.join(merged_content)

            # Get the name of the subfolder
            folder_name = os.path.basename(root)

            # Define the output file path in the base directory with the folder name
            output_file_path = os.path.join(base_dir, f"{folder_name}.md")

            # Write the merged content to the output file
            with open(output_file_path, 'w', encoding='utf-8') as f:
                f.write(merged_text)

            print(f"Merged markdown file created at: {output_file_path}")

if __name__ == "__main__":
    merge_markdown_files()
