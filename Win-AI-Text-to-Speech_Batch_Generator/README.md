## Text-to-Speech Batch Generator  
### Script Overview  
This script automates the process of converting multiple lines of text into audio files (MP3 format) using the OpenAI Text-to-Speech (TTS) API. It processes an input text file where each line represents a separate text input for the TTS API and generates corresponding MP3 files for each line. The script includes retry logic to handle rate-limiting errors gracefully.  

### Detailed Use/Features  
1. **Text Input Handling**:  
   - Reads all lines from a specified input file (e.g., `input.txt`).  
   - Each line is treated as an independent input for text-to-speech conversion.  

2. **Text-to-Speech Conversion**:  
   - Uses the OpenAI TTS API to convert text to speech.  
   - Allows selecting a voice parameter for generating audio.  

3. **Error Handling and Rate Limit Management**:  
   - Implements retry logic for rate-limiting errors (HTTP 429).  
   - Waits for 10 seconds before retrying the conversion to comply with API rate limits.  

4. **MP3 File Generation**:  
   - Saves each audio response as an MP3 file.  
   - Files are named sequentially (e.g., `1.mp3`, `2.mp3`, ...), corresponding to the line numbers in the input file.  

### Installation  

#### Requirements  
- Python 3.8 or higher  
- OpenAI Python library (`openai`)  

#### Installation Steps  
1. **Install Python**:  
   - Ensure Python 3.8 or higher is installed on your system.  
   - Verify installation using:  
     ```bash
     python --version
     ```  

2. **Install the OpenAI Library**:  
   - Install the required OpenAI Python library using pip:  
     ```bash
     pip install openai
     ```  

3. **Prepare API Key**:  
   - Save your OpenAI API key in a plain text file named `api_key.txt`.  
   - The script reads the API key from this file for authentication.  

4. **Prepare Input File**:  
   - Create a text file named `input.txt` containing the text to be converted to speech.  
   - Each line in the file will be processed as a separate input for the API.  

5. **Save the Script**:  
   - Save the provided script as `text_to_speech_batch.py`.  

#### Usage  
1. Ensure you have the following files ready:  
   - `api_key.txt` (contains your OpenAI API key)  
   - `input.txt` (contains the text inputs to be converted to speech)  

2. Run the script:  
   ```bash
   python text_to_speech_batch.py
   ```  

3. Upon successful execution:  
   - The script generates MP3 files (`1.mp3`, `2.mp3`, etc.) in the same directory.  
   - Each file corresponds to a line of text from the input file.  

### Disclaimer  
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.  