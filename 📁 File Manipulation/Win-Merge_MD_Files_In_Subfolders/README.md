## Merge MD Files In Subfolders
### Script Overview
This script automates the process of merging all markdown (`.md`) files found within subdirectories into a single markdown file. The resulting file is created in the root directory with the name of the subfolder as its filename. Each file's content is prefixed with its filename as a header for clarity.

### Detailed Use/Features
1. **Subdirectory Traversal**: The script traverses all subdirectories in the current working directory.
2. **Markdown File Detection**: Only files with the `.md` extension are selected for merging.
3. **Content Organization**: 
   - Each file's name is added as a level-1 header (`# filename.md`) to separate content.
   - The file's content is appended below the header with an extra newline for spacing.
4. **Output File**: 
   - A merged markdown file is created in the root directory.
   - The file is named after the subdirectory (e.g., `subfolder_name.md`).
5. **Logging**: A success message prints the location of the merged markdown file.

### Installation
#### Requirements
- Python 3.6 or higher  
- No additional libraries are required as the script uses Python's built-in modules.

#### Installation Steps
1. **Download/Clone**: Download or clone the script to your local machine.
2. **Ensure Python**: Verify that Python 3.6 or higher is installed:
   ```bash
   python --version
   ```
3. Place the script in the root directory where subfolders containing markdown files exist.

#### Usage
1. Open a terminal or command prompt.
2. Navigate to the root directory containing subfolders with `.md` files.
3. Run the script using Python:
   ```bash
   python merge_markdown_files.py
   ```
4. After execution:
   - The merged markdown file will appear in the root directory.
   - Its filename corresponds to the subfolder's name (e.g., `subfolder_name.md`).

Example Directory Structure:
```
root/
│
├── folder1/
│   ├── file1.md
│   ├── file2.md
│
├── folder2/
│   ├── file3.md
│
└── merge_markdown_files.py
```

After running the script:
```
root/
│
├── folder1.md      # Merged content from folder1
├── folder2.md      # Merged content from folder2
├── folder1/
│   ├── file1.md
│   ├── file2.md
│
├── folder2/
│   ├── file3.md
│
└── merge_markdown_files.py
```

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.