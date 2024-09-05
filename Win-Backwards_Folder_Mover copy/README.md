## Audio-Video Merger Script

### Script Overview
This script merges an audio file with a video file using FFmpeg, a popular multimedia framework. The merged file will contain the original video stream combined with the new audio stream, saved as an output file in the same directory as the original video with '_merged' appended to its name. This tool is useful for situations where you need to replace or add an audio track to a video without re-encoding the video stream.

### Detailed Use/Features
1. **User Input for File Paths**: The script prompts the user to enter the paths for the video and audio files they wish to merge.
2. **Automatic Output Path Generation**: The output file is automatically named based on the input video file name, with '_merged' appended to it, and saved in the same directory.
3. **Merging Process**: The script uses FFmpeg to merge the specified audio file with the video file. The video stream is copied directly (`-c:v copy`), while the audio stream is encoded using AAC (`-c:a aac`).
4. **Continuous Operation Option**: After completing a merge, the script asks the user if they want to process another file, allowing for multiple merges in a single session.

### Installation

#### Requirements
- Python 3.6 or higher
- FFmpeg installed and added to the system's PATH
- Operating System: This script has been tested on Windows 11.

#### Installation Steps
1. **Download FFmpeg**: 
   - Visit the FFmpeg official website [FFmpeg.org](https://ffmpeg.org/download.html) and download the appropriate version for your operating system.
   - Follow the instructions on the FFmpeg website to install it and add the `ffmpeg` executable to your system's PATH.

2. **Clone the Repository or Download the Script**: 
   - Clone this repository or download the script file directly to your local machine.

3. **Ensure Python is Installed**:
   - Make sure Python 3.6 or higher is installed on your system. You can download it from [Python.org](https://www.python.org/downloads/).

#### Usage
1. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using Python:
     ```bash
     python merge_audio_video.py
     ```
2. **Follow the Prompts**:
   - Enter the full path to the video file when prompted.
   - Enter the full path to the audio file when prompted.
   - The script will merge the files and save the output in the same directory as the video file with '_merged' appended to its name.

3. **Repeat or Exit**:
   - After merging, the script will ask if you want to merge another file. Enter 'yes' to continue or 'no' to exit.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.