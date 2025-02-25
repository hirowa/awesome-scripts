## PDF and Text File Merger  
### Script Overview  
This script allows users to merge multiple text-based files, including PDFs, `.txt`, and `.md` files, into a single output file. It extracts text content from each file, adds a header with the file name, and appends the content to the output file. This is useful for consolidating notes, reports, or documents into a single readable format.

### Detailed Use/Features  
1. **Supports Multiple File Types**:  
   - Extracts text from `.pdf`, `.txt`, and `.md` files.  
   - Skips unsupported file formats with a warning.  
2. **PDF Text Extraction**:  
   - Uses `PyPDF2` to extract text from each page of a PDF.  
3. **File Merging with Headers**:  
   - Adds a separator with the file name before merging content.  
   - Preserves readability by ensuring proper spacing between files.  
4. **Error Handling**:  
   - Checks for missing files and reports errors.  
   - Catches and displays exceptions related to file processing.  

### Installation  
#### Requirements  
- Python 3.6 or higher  
- Dependencies:  
  - `PyPDF2` (for PDF text extraction)  

#### Installation Steps  
1. Install Python (if not already installed).  
2. Install required dependencies using pip:  
   ```bash
   pip install PyPDF2
   ```
3. Download or clone the script file to your desired directory.  

#### Usage  
Run the script from the command line with the following format:  
```bash
python merge_files.py output.txt file1.pdf file2.txt file3.md ...
```
- `output.txt` → Name of the merged output file.  
- `file1.pdf`, `file2.txt`, `file3.md`, etc. → Input files to be merged.  
- The script processes each file, extracts text, and writes it into `output.txt` with headers.  

### Disclaimer  
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.