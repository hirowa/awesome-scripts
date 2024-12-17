## Random File Renamer

### Script Overview
This script is designed to automatically rename all files within a specified directory to a unique random name while preserving the original file extensions. The primary purpose of this script is to anonymize or randomize file names in a batch, which can be useful for various organizational or security purposes.

### Detailed Use/Features
1. **Directory Validation**: The script checks if the specified directory exists and will terminate with a message if the directory is not found.
2. **File Processing**: It iterates through each file within the directory, skipping subdirectories, and generates a new random name for each file.
3. **Random Naming**: For each file, a unique random number between 100,000 and 999,999 is generated to create a new filename, while the original file extension is retained.
4. **Renaming Operation**: Each file is renamed to its new random name, and a log message is printed to indicate the old and new filenames.

### Installation

#### Requirements
- Python 3.6 or higher
- No additional libraries are required as the script uses only standard Python libraries (`os`, `random`, `sys`).

#### Installation Steps
1. Clone the repository or download the script file to your local machine.
2. Ensure Python is installed on your system (version 3.6 or higher).
3. No additional dependencies are needed beyond Python's standard library.

#### Usage
1. Place the script in any directory of your choice.
2. Open a terminal or command prompt.
3. Run the script using Python:
   ```bash
   python your_script_name.py
   ```
4. When prompted, enter the full path of the directory containing the files you want to rename.
5. The script will rename all files in the specified directory to random names and display a log of the renaming process.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.