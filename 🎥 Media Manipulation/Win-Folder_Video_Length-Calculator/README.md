## Video Duration Summarizer (PowerShell)  

### Script Overview  
This PowerShell script scans a specified folder for video files and calculates their total duration. It extracts the duration metadata from each file and displays a summary, listing each video's name and duration, as well as the cumulative total duration of all detected videos.  

### Detailed Use/Features  
1. **File Filtering**: The script searches for video files with extensions `.mp4`, `.mkv`, `.avi`, `.mov`, and `.wmv`.  
2. **Metadata Extraction**: It retrieves the duration of each video using Windows Shell COM objects.  
3. **Time Parsing**: The extracted duration is processed and converted into a `TimeSpan` object for accurate summation.  
4. **Total Duration Calculation**: The script sums up the durations of all detected videos.  
5. **Formatted Output**: A table displaying each video's name and duration is generated, along with a total runtime summary.  

### Installation  

#### Requirements  
- Windows OS (PowerShell 5.1 or later)  
- Windows Explorer metadata indexing (required for duration extraction)  

#### Installation Steps  
1. Copy and paste the script into a `.ps1` file.  
2. Modify `$folderPath` to the target directory containing video files.  
3. Ensure that PowerShell script execution is allowed:  
   ```powershell
   Set-ExecutionPolicy RemoteSigned -Scope CurrentUser
   ```
4. Run the script in PowerShell:  
   ```powershell
   .\your_script.ps1
   ```

#### Usage  
1. Place the script in a folder containing video files or modify `$folderPath` to the correct directory.  
2. Execute the script in PowerShell.  
3. The output will display a list of video files with their respective durations, followed by the total duration of all videos.  

### Disclaimer  
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.