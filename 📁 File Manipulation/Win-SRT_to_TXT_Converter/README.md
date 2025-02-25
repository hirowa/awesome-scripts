## SRT to TXT Converter  
### Script Overview  
This script processes `.srt` subtitle files, extracting only the subtitle text while removing sequence numbers and timestamps. The cleaned text is then saved as a `.txt` file in the same directory as the original subtitle file.  

### Detailed Use/Features  
1. **Recursive Directory Scanning**: The script scans the specified directory and its subdirectories for `.srt` files.  
2. **Subtitle Extraction**: It removes sequence numbers and timestamp lines from `.srt` files, keeping only the subtitle text.  
3. **Text Formatting**: Extracted subtitles are merged into a single line with spaces between them for better readability.  
4. **Automatic `.txt` File Creation**: The processed text is saved as a `.txt` file with the same name as the original `.srt` file.  
5. **Error Handling**: The script checks if the provided directory path exists before proceeding.  

### Installation  
#### Requirements  
- Python 3.6 or higher  
- No external dependencies (uses built-in Python modules: `os` and `re`)  

#### Installation Steps  
1. Download or clone the script file.  
2. Ensure Python 3.6+ is installed on your system.  
3. No additional libraries are needed since all required modules are part of Python’s standard library.  

#### Usage  
1. Run the script using Python:  
   ```bash
   python your_script_name.py
   ```  
2. Enter the directory path containing the `.srt` files when prompted.  
3. The script will process all `.srt` files in the directory and generate corresponding `.txt` files in the same location.  

### Disclaimer  
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.