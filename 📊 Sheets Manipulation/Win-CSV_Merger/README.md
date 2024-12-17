## CSV Merger Script
### Script Overview
This Python script is designed to automate the process of merging multiple CSV files located in a single directory. It reads all the CSV files present in the current working directory, concatenates them into a single DataFrame, and saves the result as a new CSV file (`merged_output.csv`). This is especially useful for combining datasets or logs from multiple CSV files into one unified file.

### Detailed Use/Features
1. **Directory Scanning**: The script scans the current working directory for files with a `.csv` extension.
2. **CSV File Reading**: Each CSV file is read into a Pandas DataFrame.
3. **DataFrame Concatenation**: All CSV files are combined (concatenated) into a single DataFrame.
4. **Merged CSV Output**: The resulting merged DataFrame is saved as a new file called `merged_output.csv` in the same directory.
5. **Log Output**: The script provides feedback by printing the filenames of the CSV files it adds to the merge and confirms when the merge is complete.

### Installation
#### Requirements
- **Python 3.6** or higher
- **Pandas library** (Python Data Analysis Library)

#### Installation Steps
1. Ensure Python 3.6 or higher is installed on your system. You can download Python [here](https://www.python.org/downloads/).
2. Install the Pandas library if you haven't already:
   ```bash
   pip install pandas
   ```
3. Save the provided script into a Python file, e.g., `csv_merger.py`.

#### Usage
1. Place the script (`csv_merger.py`) in the directory where your CSV files are located.
2. Ensure that all the CSV files you want to merge are in this directory.
3. Run the script using Python:
   ```bash
   python csv_merger.py
   ```
4. After execution, a new file called `merged_output.csv` will be created in the same directory, containing the merged content of all the CSV files.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.