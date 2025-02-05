## Coursera-dl Launcher  
### Script Overview  
This Windows batch script automates the process of downloading Coursera course content using the `coursera-dl` tool. It reads the authentication key (CAUTH) from a file, extracts and obfuscates part of the key for display, prompts the user for a course name, activates a virtual environment, and runs `coursera-dl` to download the course materials with English subtitles.  

### Detailed Use/Features  
1. **Extracts CAUTH Key**:  
   - Reads the CAUTH key from `cauth.txt`.  
   - Strips leading and trailing spaces.  
   - Obfuscates the key by displaying only the first 5 and last 5 characters for security.  

2. **Prompts for Course Name**:  
   - The user is asked to enter the Coursera course name.  

3. **Activates Virtual Environment**:  
   - Assumes a virtual environment (`coursera_venv`) is set up in the script's directory.  
   - Activates the virtual environment to ensure dependencies are correctly loaded.  

4. **Runs `coursera-dl`**:  
   - Uses the extracted CAUTH key to authenticate.  
   - Downloads course content with English subtitles.  

5. **Pauses Execution**:  
   - Keeps the command prompt open after execution for the user to review output messages.  

### Installation  

#### Requirements  
- Windows operating system  
- Python installed (3.6 or higher)  
- `coursera-dl` installed in a virtual environment  
- A properly configured `cauth.txt` file containing the CAUTH authentication token  
- A virtual environment located at `coursera_venv\Scripts\activate.bat`  

#### Installation Steps  
1. **Install Python** (if not already installed):  
   - Download and install Python from [python.org](https://www.python.org/downloads/).  
   - Ensure Python is added to the system PATH.  

2. **Set Up Virtual Environment**:  
   ```bash
   python -m venv coursera_venv
   coursera_venv\Scripts\activate
   ```

3. **Install `coursera-dl` in the Virtual Environment**:  
   ```bash
   pip install coursera-dl
   ```

4. **Create `cauth.txt`**:  
   - Obtain your CAUTH authentication token from Coursera (refer to `coursera-dl` documentation).  
   - Save it in a text file (`cauth.txt`) in the same directory as the script.  
   - Format: `CAUTH=<your_cauth_token>`  

5. **Run the Script**:  
   - Place `Win-Coursera-dl-Launcher.bat` in the same directory as `cauth.txt` and `coursera_venv`.  
   - Double-click the batch file or run it from the command prompt.  

#### Usage  
1. **Ensure all setup steps are completed.**  
2. **Run the script (`Win-Coursera-dl-Launcher.bat`).**  
3. **Enter the course name when prompted.**  
4. **Wait for the course content to be downloaded.**  
5. **Check the output folder for downloaded files.**  

### Disclaimer  
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.  

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.