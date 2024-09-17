## EPUB Chapter Extractor
### Script Overview
This Python script extracts the chapters and subchapters from the Table of Contents (TOC) of EPUB files, saves them as individual `.txt` files, and generates a CSV file containing information about each chapter, including hierarchical numbering and word count. The script is designed to process multiple EPUB files within a directory, organizing each file's content into its own folder.

### Detailed Use/Features
1. **EPUB File Processing**: The script processes EPUB files in the current directory, creating a folder for each file to store its extracted chapters and metadata.
2. **Chapter Extraction**: Using the Table of Contents (TOC), the script extracts text for each chapter, organizes it by chapter level (e.g., 1, 1.1, 1.1.1), and writes each chapter to a separate `.txt` file.
3. **Sanitized Filenames**: Filenames are sanitized to remove any invalid characters and truncated to a safe length (100 characters) if necessary.
4. **Hierarchical Numbering**: Chapters are numbered hierarchically based on their level (e.g., Chapter 1, Subchapter 1.1, Sub-subchapter 1.1.1).
5. **Word Count**: The script counts the number of words in each chapter and includes this information in a CSV file.
6. **Error Handling**: Suppresses CSS warnings and handles potential errors when reading files or pages from the EPUB.
7. **CSV Output**: Each EPUB's chapter information is saved in a CSV file, with fields such as chapter number, title, page number, and word count.

### Installation
#### Requirements
- Python 3.6 or higher
- Required Python packages:
  - `PyMuPDF` (install via `pip install pymupdf`)
  - `shutil`, `os`, `sys`, `re`, and `csv` are part of Python's standard library.

#### Installation Steps
1. Clone or download the script file.
2. Install the required dependencies:
   ```bash
   pip install pymupdf
   ```
3. Place the script in a directory containing your EPUB files.

#### Usage
1. Ensure the script is located in a directory with the EPUB files to process.
2. Run the script with Python:
   ```bash
   python epub_chapter_extractor.py
   ```
3. The script will automatically:
   - Create a folder for each EPUB file.
   - Extract the chapters into separate `.txt` files.
   - Generate a CSV file containing chapter metadata for each EPUB.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.