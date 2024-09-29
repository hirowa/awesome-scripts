## PDF Cropping
### Script Overview
This Python script automates the process of cropping PDF files by identifying a specific label within the PDF's text and removing content below the label on the identified page. It is particularly useful for trimming sections of documents where only a portion is required, such as removing pages or sections after a specific keyword or phrase (e.g., "Total de Movimientos"). The script processes all PDF files in a specified directory (or the current directory by default) and saves cropped versions of each PDF.

### Detailed Use/Features
1. **PDF Parsing**: The script uses the `PyMuPDF` library (via `fitz`) to read the content of each PDF.
2. **Label Detection**: It searches for a specific text label (default: "Total de Movimientos") within each PDF, starting from the last page and moving backwards.
3. **Cropping**: Once the label is found, the script crops the page by removing content at and below the Y-coordinate of the label.
4. **Batch Processing**: It iterates over all PDF files in the specified directory, applying the cropping process to each one.
5. **Output**: The cropped version of each PDF is saved as a new file, appending "_cropped" to the original file name.
6. **Fallback Behavior**: If the label is not found in a given PDF, the script will not modify the file and will notify the user.

### Installation
#### Requirements
- Python 3.6 or higher
- [PyMuPDF](https://pypi.org/project/PyMuPDF/) (also known as `fitz`)
- OS module (comes as part of Python's standard library)

#### Installation Steps
1. **Clone the repository or download the script**:
   Download the Python script to your local machine or clone the repository.
   
2. **Install Python**:
   Ensure that Python 3.6 or higher is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

3. **Install dependencies**:
   Use `pip` to install the required package (`PyMuPDF`):
   ```bash
   pip install pymupdf
   ```

#### Usage
1. Place the script in the directory containing the PDFs you want to crop, or specify the directory in the function call.
   
2. **Run the script**:
   You can run the script directly from the command line as follows:
   ```bash
   python your_script_name.py
   ```

3. The script will automatically detect all `.pdf` files in the specified directory (default is the current working directory), search for the label (default is "Total de Movimientos"), and crop the relevant pages.

4. If the label is found, a new cropped version of the PDF will be saved with `_cropped` appended to the file name (e.g., `document_cropped.pdf`). If the label is not found, the script will notify you and no changes will be made.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.