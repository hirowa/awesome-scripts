## PDF Batch Cropper
### Script Overview
This Python script processes all PDF files in the current working directory by cropping each page according to specified margins. It allows for different cropping parameters for the first page and the rest of the pages. The final processed PDFs are saved with a "_processed" suffix, and the script uses QPDF to optimize the output by removing hidden content and linearizing the PDF for faster web viewing.

### Detailed Use/Features
1. **Directory-Based PDF Processing**: The script automatically detects all PDF files in the current directory and processes each one without needing manual input for each file.
2. **Customizable Cropping Parameters**: You can define separate cropping values for the first page and the remaining pages in terms of top, right, and bottom margins.
   - **First Page Crops**: Crops applied to the top, right, and bottom margins of the first page.
   - **Other Pages Crops**: Crops applied to the top, right, and bottom margins of all other pages.
3. **QPDF Integration**: After cropping, the script invokes QPDF to clean up hidden content and optimize the final output PDF.
4. **Temporary File Management**: The script uses a temporary file to store intermediate cropped results, which is deleted after final processing to save space.

### Installation
#### Requirements
- **Python 3.7 or higher**
- **pypdf**: A Python library for PDF manipulation.
- **QPDF**: A command-line program used for optimizing PDF files.

#### Installation Steps
1. **Clone or Download the Script**: Clone the repository or download the script to your local machine.
2. **Install Python Packages**:
   - Install Python dependencies by running:
     ```bash
     pip install pypdf
     ```
3. **Install QPDF**:
   - QPDF must be installed separately. For Linux/Mac, use a package manager like `apt` or `brew`:
     ```bash
     sudo apt install qpdf  # On Debian/Ubuntu
     brew install qpdf      # On macOS
     ```
   - On Windows, download the QPDF installer from the official [QPDF GitHub releases page](https://github.com/qpdf/qpdf/releases) and follow the installation instructions.

#### Usage
1. **Prepare the Directory**: Place the script in the directory containing the PDF files you want to crop.
2. **Run the Script**:
   - Simply run the script with Python:
     ```bash
     python your_script_name.py
     ```
   - The script will process each PDF in the directory, crop the pages based on predefined values, and save the output with a "_processed.pdf" suffix.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.