## Image to Alt-Text Generator

### Script Overview
This script is designed to automate the process of generating alt text for images using OpenAI's GPT-4 Vision model. The script processes all images in a specified folder, sends them to the OpenAI API for alt text generation, and saves the resulting descriptions to text files in the same folder. The script supports a variety of image formats including PNG, JPEG, GIF, and BMP.

### Detailed Use/Features
1. **Base64 Encoding of Images**: The script reads each image file and encodes it to a Base64 format suitable for sending to the OpenAI API.
2. **Integration with OpenAI GPT-4 Vision API**: It uses the GPT-4 Vision model to generate descriptive alt text for each image.
3. **Automated Alt Text File Generation**: For each processed image, the script creates a corresponding `.txt` file containing the generated alt text. The text file is saved in the same directory as the image with the same base filename.
4. **API Key Management**: The script retrieves the OpenAI API key from a local `api_key.txt` file if it exists. If the file is not found, it prompts the user to enter their API key.
5. **User Interaction**: 
   - Prompts the user to enter the folder path containing images.
   - Continuously informs the user about the processing status of each image.

### Installation

#### Requirements
- Python 3.6 or higher
- An OpenAI API key with access to the GPT-4 Vision model
- Internet connection (for API requests)
- Operating System: This script has been tested on Windows 11.

#### Installation Steps
1. **Obtain an OpenAI API Key**:
   - Sign up for an OpenAI account and obtain an API key that has access to the GPT-4 Vision model.
   
2. **Save the API Key**:
   - Create a text file named `api_key.txt` in the same directory as the script.
   - Paste your API key into `api_key.txt` and save the file.

3. **Clone the Repository or Download the Script**:
   - Clone this repository or download the script file directly to your local machine.

4. **Ensure Python is Installed**:
   - Verify that Python 3.6 or higher is installed on your system. If not, download and install it from [Python.org](https://www.python.org/downloads/).

5. **Install Required Libraries**:
   - Install the `requests` library if it is not already installed:
     ```bash
     pip install requests
     ```

#### Usage
1. **Run the Script**:
   - Open a terminal or command prompt.
   - Navigate to the directory where the script is located.
   - Run the script using Python:
     ```bash
     python image_to_alt_text.py
     ```

2. **Follow the Prompts**:
   - Enter the path to the folder containing images when prompted.
   - If you haven't saved your API key in `api_key.txt`, you will be prompted to enter it manually.

3. **View the Results**:
   - The script will process all images in the specified folder, generate alt text using OpenAI's API, and save the alt text to `.txt` files in the same folder.

4. **Repeat or Exit**:
   - The script will complete after processing all images in the folder. You can rerun it for another folder if needed.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to ensure the security of their OpenAI API keys and handle image data responsibly to protect privacy and comply with relevant regulations.