## Text File Organizer

### Script Overview
This script is designed to help users organize `.txt` files within a specified directory. It searches through the base directory (and all its subdirectories) for text files and moves them into a newly created folder within each directory where text files are found. The default name for the new folder is "Transcripts," but the user can specify a different name if desired.

### Detailed Use/Features
1. **Recursive Directory Search**: The script recursively searches through the specified base directory and all its subdirectories to find `.txt` files.
2. **Dynamic Folder Creation**: For each directory containing `.txt` files, the script creates a new folder named "Transcripts" (or a user-defined name).
3. **File Moving**: All `.txt` files found within a directory are moved into the newly created folder.
4. **User Input for Customization**: 
   - Users are prompted to enter the base directory to search.
   - Users can specify a custom name for the folder where `.txt` files will be moved. If left blank, the default "Transcripts" is used.
5. **Continuous Operation Option**: After processing a directory, the script prompts the user to either continue processing another directory or exit.

### Installation

#### Requirements
- Python 3.6 or higher
- Operating System: This script has been tested on Windows 11.

#### Installation Steps
1. **Download or Clone the Script**: 
   - Clone the repository or download the script file to your local machine.

2. **Ensure Python is Installed**:
   - Verify that Python 3.6 or higher is installed on your system. If not, download and install it from [Python.org](https://www.python.org/downloads/).

#### Usage
1. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using Python:
     ```bash
     python organize_txt_files.py
     ```
2. **Follow the Prompts**:
   - Enter the path to the base directory you want to organize when prompted.
   - Optionally, enter a custom name for the new folder to store `.txt` files. Leave blank to use the default name "Transcripts".
   - The script will move all `.txt` files into the specified folder within each directory that contains `.txt` files.

3. **Repeat or Exit**:
   - After organizing files, the script will ask if you want to process another folder. Enter 'yes' to continue or 'no' to exit.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.