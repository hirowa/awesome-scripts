## Obsidian-Batch_Replacer
### Script Overview
This script automates the process of cleaning and replacing specific tags in Markdown (`.md`) files within a folder and its subfolders. It replaces specified tags, removes numeric values, standalone numeric lines, and lines containing non-alphanumeric characters or hyphens. This is particularly useful for bulk-cleaning Markdown files, such as notes or documentation files, where old or unnecessary tags need to be removed.

### Detailed Use/Features
1. **Tag Replacement**: Replaces a specified old tag with a new tag across all `.md` files in a folder and its subfolders.  
2. **Numeric Value Removal**: Strips numeric values that appear after the specified tag.  
3. **Standalone Numeric Line Removal**: Deletes any lines that contain only numbers or whitespace.  
4. **Non-Alphanumeric Line Removal**: Removes lines with non-alphanumeric characters or hyphens that do not add meaningful content.  
5. **Recursive Folder Processing**: Traverses all subdirectories to ensure every `.md` file is updated.  
6. **User Input**: Allows users to specify the folder path containing the `.md` files to be cleaned.  

### Installation
#### Requirements
- **Python 3.6 or higher**  
- Standard Python libraries: `os` and `re` (no additional installation required).  

#### Installation Steps
1. Clone the repository or download the script file.  
2. Ensure Python is installed on your system (version 3.6 or higher).  
3. Save the script in your desired working directory.

#### Usage
1. Open a terminal or command prompt.  
2. Run the script using Python:  
   ```bash
   python your_script_name.py
   ```
3. When prompted, enter the path to the folder containing the Markdown files (e.g., `/path/to/markdown/files`).  
4. The script will search for `.md` files, replace the tags, and clean unnecessary lines.  
5. Changes will be made **in place**, and the script will output the names of the updated files.  

**Example Input/Output**:  
- Input:  
   Folder Path: `/my_notes/`  
- Action:  
   - Replace the tag `"Date: "` with `""` (empty string).  
   - Remove numeric values, standalone numeric lines, and invalid lines.  
- Output:  
   ```
   Updated tags in: /my_notes/note1.md
   Updated tags in: /my_notes/subfolder/note2.md
   ```

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.