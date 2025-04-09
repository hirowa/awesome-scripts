import json
import csv
import html2text

# Prompt the user for input file path and output file name
input_file_path = input("Enter the path to your JSON file: ").strip()
output_file_name = input("Enter the output CSV file name (e.g., articles.csv): ").strip()

# Load the JSON data from the user-provided file path
with open(input_file_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

# Extract the list of articles from the JSON (adjust key path as needed)
articles = data["category"]["articles"]

# Setup html2text converter for converting HTML to Markdown
converter = html2text.HTML2Text()
converter.ignore_links = False  # Keep links in the markdown output
converter.body_width = 0         # Prevent automatic word-wrapping

# Define the CSV column headers
fieldnames = [
    "id",
    "title",
    "slug",
    "text_markdown",  # Converted HTML content in markdown form
    "views",
    "rating_happy",
    "rating_neutral",
    "rating_sad",
    "keywords",
    "introtext",
    "updated_at",
    "full_url"
]

# Write the processed data to the output CSV file provided by the user
with open(output_file_name, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    # Process each article in the list
    for article in articles:
        # Convert the HTML content in the "text" field to Markdown
        markdown_text = converter.handle(article.get("text", "")).strip()

        # Create a dictionary representing the row data
        row = {
            "id": article.get("id", ""),
            "title": article.get("title", ""),
            "slug": article.get("slug", ""),
            "text_markdown": markdown_text,
            "views": article.get("views", 0),
            "rating_happy": article.get("rating_happy", 0),
            "rating_neutral": article.get("rating_neutral", 0),
            "rating_sad": article.get("rating_sad", 0),
            "keywords": article.get("keywords", ""),
            "introtext": article.get("introtext", ""),
            "updated_at": article.get("updated_at", ""),
            "full_url": article.get("full_url", "")
        }
        writer.writerow(row)

print(f"CSV has been created and saved as '{output_file_name}'.")
