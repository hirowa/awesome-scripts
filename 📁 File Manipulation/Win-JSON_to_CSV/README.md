## JSON to CSV Article Converter
### Script Overview
This Python script converts a structured JSON file containing article data into a well-formatted CSV file. The script is designed for content managers, developers, or data analysts who need to extract and repurpose content from a JSON format (often generated from CMS exports or APIs) into a Markdown-compatible CSV format. It transforms HTML content within each article into Markdown using the `html2text` library and outputs multiple metadata fields for each article.

### Detailed Use/Features
- **Interactive Input**: Prompts the user to input the path to the source JSON file and specify the desired output CSV file name.
- **HTML to Markdown Conversion**: Converts rich-text HTML fields in each article (specifically the `text` field) to clean Markdown format for easier readability or future markdown-based processing.
- **Metadata Extraction**: Extracts essential fields including IDs, titles, views, ratings, keywords, and URLs.
- **CSV Output**: Writes the parsed and converted data to a CSV file with clear headers for each data attribute, making the output easy to open in Excel or import into other systems.

### Installation
#### Requirements
- Python 3.6 or higher
- `html2text` Python package

#### Installation Steps
1. Ensure Python 3.6+ is installed on your system.
2. Install the required dependency:
   ```bash
   pip install html2text
   ```
3. Save the script to a `.py` file, for example:
   ```bash
   article_json_to_csv.py
   ```

#### Usage
1. Place your JSON file in an accessible location on your system.
2. Run the script via terminal or command prompt:
   ```bash
   python article_json_to_csv.py
   ```
3. Enter the full path to your JSON file when prompted.
4. Provide the desired name for the output CSV file (e.g., `articles.csv`).
5. The script will process each article, convert HTML content to Markdown, and write the results into the specified CSV file.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.