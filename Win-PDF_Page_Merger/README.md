## PDF Page Merger
### Script Overview
This script processes PDF files in a specified directory and merges all the pages of each PDF into a single large page per PDF. For each original PDF, the script computes the combined height of all its pages, keeps the maximum width, and creates a new single-page PDF that stacks all pages vertically. The new merged PDF is saved with a "_merged" suffix in the filename.

### Detailed Use/Features
1. **PDF Detection**: The script iterates over all files in the current working directory, targeting files with a `.pdf` extension.
2. **PDF Merging**: For each PDF:
   - A new PDF file is created with one large page that accommodates the dimensions of all original pages stacked vertically.
   - The maximum width of the pages is used as the width of the new PDF page, and the heights of all pages are summed to form the new page's height.
3. **Page Insertion**: Each original page is sequentially placed on the new PDF page, maintaining the original content in its respective order.
4. **Output File**: The merged PDF is saved with the same base name as the original, followed by "_merged.pdf".
5. **Logging**: After processing all PDFs in the directory, a completion message is printed to the console.

### Installation
#### Requirements
- **Python 3.6+**
- **PyMuPDF** (also known as `fitz`) for PDF processing.

#### Installation Steps
1. **Install Python**: Ensure Python 3.6 or higher is installed. You can download Python [here](https://www.python.org/downloads/).
2. **Install PyMuPDF**:
   Run the following command to install the `fitz` package (PyMuPDF):
   ```bash
   pip install PyMuPDF
   ```
3. **Download the Script**: Save the script as a `.py` file in the directory where you want to process PDFs.

#### Usage
1. **Navigate to the Directory**: Use the terminal or command prompt to navigate to the folder containing your `.py` script and the PDFs you want to process.
   ```bash
   cd path_to_your_directory
   ```
2. **Run the Script**: Execute the script by running:
   ```bash
   python script_name.py
   ```
3. **Output**: The script will create a new PDF for each input PDF in the directory, with the merged content on a single page. The new PDF will have the same name as the original, followed by "_merged.pdf".

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.