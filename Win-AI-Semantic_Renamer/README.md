## AI Semantic Renamer
### Script Overview
This script automates the process of renaming `.txt` files based on their content. It reads a portion of the file, sends the content to the OpenAI API to generate a descriptive name, and then renames the file accordingly. This is particularly useful for organizing and categorizing text files in a meaningful way without manually reviewing each file's content.

### Detailed Use
1. **Finding Text Files**: The script recursively searches the specified directory for all `.txt` files.
2. **Reading File Content**: It reads a specific number of characters (default is 500) from each text file to use as context for generating a new name.
3. **API Communication**: The extracted content is sent to the OpenAI API with a request to generate a short, descriptive file name based on the content.
4. **Renaming Files**: The script uses the generated name to rename the file. It ensures the new name is valid for Windows file systems and checks for existing files to prevent overwriting.
5. **Error Handling and Logging**: If renaming fails after multiple attempts, the script logs the file path to a `failed_logs.txt` file for further review.

### Installation
#### Requirements
- Python 3.7 or higher
- **requests** library for handling HTTP requests

#### Installation Steps
1. Clone the repository or download the script.
2. Install the required Python library:
   ```bash
   pip install requests
   ```
3. **Set Up Your OpenAI API Key**:
   - Replace `<put_your_api_key_here>` in the script with your actual OpenAI API key.

#### Usage
- Place the `.txt` files to be renamed in a directory.
- Run the script using Python:
  ```bash
  python your_script_name.py
  ```
- The script will process all `.txt` files in the specified directory and rename them based on the generated descriptive names.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are responsible for securing their OpenAI API key and for any costs incurred from API usage.