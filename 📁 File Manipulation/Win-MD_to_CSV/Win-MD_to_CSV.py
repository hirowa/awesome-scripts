import os
import csv

def convert_md_to_csv():
    # Ask user for folder path
    folder_path = input("Enter the path to the folder containing .md files: ").strip().strip('"').strip("'")

    # Check if path is valid
    if not os.path.isdir(folder_path):
        print("Invalid folder path.")
        return

    # Prepare output CSV path
    output_csv = os.path.join(folder_path, "markdown_files.csv")

    # Find all .md files in the directory
    md_files = [f for f in os.listdir(folder_path) if f.endswith(".md")]

    if not md_files:
        print("No .md files found in the specified folder.")
        return

    # Write to CSV
    with open(output_csv, "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["Filename", "Content"])  # Header

        for filename in md_files:
            file_path = os.path.join(folder_path, filename)
            with open(file_path, "r", encoding="utf-8") as md_file:
                content = md_file.read().replace("\n", " ")  # Convert newlines to spaces
                writer.writerow([os.path.splitext(filename)[0], content])

    print(f"CSV created successfully: {output_csv}")

# Run the script
if __name__ == "__main__":
    convert_md_to_csv()
