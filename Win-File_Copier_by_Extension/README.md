## File Copier by Extension

### Script Overview
This script automates the process of copying all files with a specific extension from a given input directory (and its subdirectories) to a specified output directory. It is particularly useful for users who need to organize or back up files of a certain type, such as text documents, images, or any other file format.

### Detailed Use/Features
1. **Extension-Based Filtering**: The script takes a file extension as input and only copies files that match this extension.
2. **Directory Traversal**: It recursively traverses through all subdirectories of the input folder, searching for files that match the specified extension.
3. **Output Directory Management**: If the specified output directory does not exist, the script automatically creates it to ensure that files can be copied without issues.
4. **File Copying and Logging**: For each file found with the matching extension, the script copies the file to the output directory and logs the operation in the console.
5. **Path Sanitization**: The script removes any leading or trailing quotation marks from the paths entered by the user to ensure paths are properly formatted.

### Installation

#### Requirements
- Python 3.6 or higher
- No additional libraries are required beyond Python's standard library (`os` and `shutil`).

#### Installation Steps
1. Download the script file to your local machine.
2. Ensure Python is installed on your system (version 3.6 or higher).
3. No additional installations or dependencies are required as the necessary modules are part of Python's standard library.

#### Usage
1. Save the script to a convenient location on your machine.
2. Open a terminal or command prompt.
3. Run the script using Python:
   ```bash
   python your_script_name.py
   ```
4. Enter the required information when prompted:
   - **File Extension**: The file extension to filter by (e.g., `.txt`).
   - **Input Folder Path**: The path to the folder containing files you want to copy.
   - **Output Folder Path**: The path to the folder where the copied files will be stored.
5. The script will copy all matching files and display a message indicating the number of files copied.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.