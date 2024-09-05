## YouTube Transcript Downloader

### Script Overview
This script, **YouTube Transcript Downloader**, is designed to automate the process of downloading transcripts from YouTube videos, shorts, and streams from a specific YouTube channel. It retrieves transcripts directly from YouTube's API and organizes them into text files on your local machine. The script also includes functionality to merge these transcript files into a single document, enhancing organization and accessibility.

### Detailed Use/Features
1. **Fetch YouTube Channel ID and Name**: The script extracts the YouTube channel ID and name from the provided YouTube channel URL using web scraping techniques with BeautifulSoup.
2. **Download Transcripts**: It allows the user to select the type of content (videos, shorts, streams, or all) to download transcripts for, by retrieving the transcripts using the YouTube Transcript API.
3. **File Handling**: The script saves each transcript as a text file named after the video title in a user-specified directory. It also sanitizes the filenames to remove any invalid characters.
4. **Merge Transcripts**: After downloading, the script merges all transcript files in each folder into a single file for easier review.
5. **User Interactivity**: The script is interactive, prompting the user for inputs such as the YouTube channel URL, output directory, content type to download, and sleep duration between requests to avoid rate-limiting.
6. **Error Handling and Logging**: The script is equipped with error handling mechanisms to manage issues like missing channel IDs or failed transcript retrievals, and it logs these errors in a user-friendly format.

### Installation
#### Requirements
- Python 3.6 or higher
- Required Python libraries:
  - `beautifulsoup4`
  - `requests`
  - `re` (part of Python's standard library)
  - `scrapetube`
  - `youtube_transcript_api`
  - `os` (part of Python's standard library)

#### Installation Steps
1. **Install Python**: Ensure Python 3.6 or higher is installed on your system. You can download Python from [python.org](https://www.python.org/downloads/).
2. **Clone the Repository**: Clone the repository or download the script file.
3. **Install Required Libraries**: Install the required Python libraries using pip:
   ```bash
   pip install beautifulsoup4 requests scrapetube youtube-transcript-api
   ```
4. **Prepare Environment**: Ensure you have a stable internet connection as the script interacts with online APIs and websites.

#### Usage
1. **Run the Script**: Navigate to the directory containing the script and run it using Python:
   ```bash
   python youtube_transcript_downloader.py
   ```
2. **Follow the Prompts**:
   - Enter the YouTube channel URL.
   - Specify the output folder where transcripts will be saved.
   - Select the type of content to download transcripts for (videos, shorts, streams, or all).
   - Set the sleep duration between API requests to avoid rate-limiting.
3. **View Output**: The transcripts will be saved in the specified directory, organized by content type. Merged transcript files will also be available.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.