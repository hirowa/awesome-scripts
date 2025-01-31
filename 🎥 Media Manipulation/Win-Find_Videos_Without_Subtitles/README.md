## Find Videos Without Subtitles  

### Script Overview  
This Python script scans a specified directory and its subdirectories to identify video files that do not have corresponding subtitle files (`.srt`). It is useful for organizing media libraries, ensuring that all videos have subtitles, and identifying missing subtitle files.  

### Detailed Use/Features  
1. **File Scanning**: The script searches for common video file formats (`.mp4`, `.mkv`, `.avi`, `.mov`, `.wmv`, `.flv`).  
2. **Subtitle Matching**: It checks if each video file has a corresponding subtitle file (`.srt`) with the same name.  
3. **Recursive Search**: The script scans all subdirectories within the specified folder.  
4. **Missing Subtitle Detection**: It lists all video files that do not have a matching subtitle.  
5. **User Input**: The user provides the directory path via input.  
6. **Error Handling**: If the directory does not exist, the script alerts the user.  

### Installation  

#### Requirements  
- Python 3.6 or higher  
- Works on Windows (May also work on Linux/Mac, but not tested)  

#### Installation Steps  
1. Ensure Python is installed on your system (version 3.6 or later).  
2. Download or copy the script and save it as `Win-Find_Videos_Without_Subtitles.py`.  
3. Open a terminal or command prompt and navigate to the script's location.  

#### Usage  
1. Run the script using:  
   ```bash
   python Win-Find_Videos_Without_Subtitles.py
   ```  
2. Enter the directory path when prompted.  
3. The script will analyze the directory and display a list of video files missing subtitles.  

### Disclaimer  
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.