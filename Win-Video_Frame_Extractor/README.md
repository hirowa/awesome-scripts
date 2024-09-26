## Video Frame Extractor
### Script Overview
This Python script automates the process of organizing video files, extracting frames from each video using FFmpeg, and storing both the video and its frames in neatly organized directories. The script is designed to look for common video file formats within the current working directory, create a folder for each video, extract selected frames, and move the original video into its respective folder. It is particularly useful for those needing frame extraction for purposes such as video analysis, creating thumbnails, or animation study.

### Detailed Use/Features
1. **Video Detection**: The script scans the current working directory for video files with extensions such as `.mp4`, `.mov`, `.avi`, `.mkv`, `.flv`, and `.wmv`.
2. **Folder Creation**: For each detected video, it creates a folder named after the video file (excluding the extension). Inside that folder, it creates a `Frames` subfolder where the extracted frames will be stored.
3. **Frame Extraction**: Using FFmpeg, the script extracts frames from the video at intervals specified by the user, based on the maximum number of frames to be extracted.
4. **File Organization**: The script moves the original video into its respective folder to keep the working directory organized.
5. **User Input**: The user is prompted to enter a value representing the frequency of frame extraction, which determines how many frames are captured.
6. **Logging**: The script provides print statements that log its progress, including the processing of videos and extraction of frames.

### Installation
#### Requirements
- Python 3.6 or higher
- **FFmpeg**: The script uses FFmpeg, a popular open-source tool for handling video, audio, and other multimedia files.
- Python standard libraries: `os`, `shutil`, and `subprocess` (no external Python packages required).

#### Installation Steps
1. Install Python (version 3.6 or higher) if it’s not already installed.
   - [Download Python](https://www.python.org/downloads/)
2. Install FFmpeg and ensure it is accessible via the command line.
   - [Download FFmpeg](https://ffmpeg.org/download.html) and add it to your system's PATH.
3. Clone or download the script to your local machine.

#### Usage
1. Place the script in the directory containing the video files you want to process.
2. Open a terminal or command prompt in that directory.
3. Run the script using Python:
   ```bash
   python video_frame_extractor.py
   ```
4. When prompted, enter the maximum number of frames you wish to extract from each video.
5. The script will create a folder for each video file, extract the frames using FFmpeg, and move the video file into the folder.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.