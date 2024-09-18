## Image Filename Suggestion and Renaming Script
### Script Overview
This Python script processes images in a specified directory, sends them to the OpenAI API for filename suggestions, and renames the images based on the API's response. The script encodes each image in base64 format, sends it along with a prompt to the API, retrieves the suggested name, and then renames the image file accordingly. It includes error handling and rate-limiting to manage API requests.

### Detailed Use/Features
1. **Image Encoding**: Each image file is opened, read in binary format, and encoded as a base64 string.
2. **API Request**: The encoded image is sent to the OpenAI API with a custom prompt asking for a suitable filename.
3. **Response Handling**: The API returns a suggested name, which is sanitized (invalid characters are removed) and used to rename the file.
4. **Supported Image Types**: The script handles common image formats such as `.png`, `.jpg`, `.jpeg`, and `.gif`.
5. **Rate Limiting**: A delay of 1 second is introduced between API requests to avoid hitting rate limits.
6. **Error Handling**: If the image cannot be processed or the API call fails, the script will log the error and continue with the next image.

### Installation
#### Requirements
- Python 3.6 or higher
- **requests** library for sending HTTP requests to the API.
- An OpenAI API key.

#### Installation Steps
1. Install Python if not already installed (version 3.6+).
2. Install the required library by running the following command:
   ```bash
   pip install requests
   ```
3. Replace `<your_api_key_here>` in the script with your OpenAI API key.
4. Place the script in the directory where you want to process the images, or specify the directory in the script.

#### Usage
1. **Prepare the Image Files**: Ensure the images you want to rename are located in the same directory as the script or modify the script to point to a different directory.
2. **Run the Script**: Execute the script using Python:
   ```bash
   python image_renamer.py
   ```
3. **File Renaming**: The script will process each image, send it to the OpenAI API for a filename suggestion, sanitize the result, and rename the file.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.