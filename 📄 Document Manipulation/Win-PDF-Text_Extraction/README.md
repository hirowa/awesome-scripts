## PDF Text Extraction and API Processing Script
### Script Overview
This Python script automates the extraction of text from a PDF file and sends the extracted content to an API (OpenAI's GPT model) for further processing. The script then parses the response, cleans it up, and saves the processed data in JSON format. This is particularly useful for converting PDF content into structured data through a language model, enabling tasks such as content summarization, transformation, or extraction of meaningful information.

### Detailed Use/Features
1. **PDF Text Extraction**: The script can extract text from either a single page or a range of pages from a PDF file using the PyMuPDF library (`fitz`). Users are prompted to enter a specific page or page range.
2. **API Interaction**: The extracted content is sent to an API endpoint (e.g., OpenAI's GPT API). The model processes the content, returning a response that the script attempts to clean and parse as JSON data.
3. **Error Handling**: The script handles potential errors during text extraction, API communication, and JSON parsing. It provides informative messages for debugging when issues arise.
4. **Output**: The final processed data is saved as a JSON file with a filename based on the original PDF's name.
5. **Batch Processing**: The script scans the current working directory for all PDF files and processes them in sequence.

### Installation
#### Requirements
- Python 3.7 or higher
- **PyMuPDF (fitz)** for PDF text extraction
- **Requests** for making API calls

#### Installation Steps
1. Clone the repository or download the script file.
2. Install the required dependencies:
   ```bash
   pip install pymupdf requests
   ```
3. Ensure you have an API key from OpenAI or another compatible service.
4. Replace the placeholder `API_KEY` in the script with your actual API key.

#### Usage
1. Place the script in a directory containing the PDF files you want to process.
2. Run the script:
   ```bash
   python script_name.py
   ```
3. Follow the on-screen instructions to enter the page number or range of pages for each PDF.
4. The script will extract text, send it to the API, and save the parsed JSON response as a file in the same directory.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.