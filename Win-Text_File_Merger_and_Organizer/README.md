## Text File Merger and Organizer

### Script Overview
This script is designed to recursively search through a specified directory and its subdirectories to find `.txt` files, merge them into a single file per folder, and organize these merged files into a centralized folder. Each merged file is named after its parent directory and contains the contents of all `.txt` files in that folder, separated by a customizable separator. Additionally, a copy of each merged file is placed in a root folder named "0. Transcripts" to facilitate easy access.

### Detailed Use/Features
1. **Recursive Directory Search**: The script searches through a specified directory and all its subdirectories to locate `.txt` files.
2. **Natural Sorting of Files**: `.txt` files are sorted in a natural order (e.g., `file1.txt, file2.txt, file10.txt` instead of `file1.txt, file10.txt, file2.txt`) before merging.
3. **Merging of Text Files**: Within each directory, all `.txt` files are merged into a single file. The contents are separated by a customizable separator (default is `---`).
4. **Output Organization**:
   - Merged files are saved in a subdirectory named "Merged" within their respective parent directories.
   - A copy of each merged file is also saved in a root-level directory called "0. Transcripts."
5. **Customizable and Automated Folder Structure**: If the "0. Transcripts" or "Merged" folders do not exist, the script automatically creates them.
6. **User Interaction**:
   - The user is prompted to enter the root directory path where `.txt` files are located.
   - After processing a directory, the user is asked if they want to process another, allowing for repeated use without restarting the script.

### Installation

#### Requirements
- Python 3.6 or higher
- Operating System: This script has been tested on Windows 11.

#### Installation Steps
1. **Download or Clone the Script**:
   - Clone the repository or download the script file directly to your local machine.

2. **Ensure Python is Installed**:
   - Verify that Python 3.6 or higher is installed on your system. You can download it from [Python.org](https://www.python.org/downloads/).

#### Usage
1. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using Python:
     ```bash
     python merge_txt_files.py
     ```
2. **Follow the Prompts**:
   - Enter the root directory path where the `.txt` files are located when prompted.
   - The script will search through the provided directory and its subdirectories to find and merge `.txt` files.

3. **View the Results**:
   - Merged files will be saved in a "Merged" folder within each directory where `.txt` files were found.
   - Copies of all merged files will also be saved in a "0. Transcripts" folder in the root directory.

4. **Repeat or Exit**:
   - After processing, the script will ask if you want to process another folder. Enter 'yes' to continue or 'no' to exit.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.