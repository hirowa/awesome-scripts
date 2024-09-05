## CSV File Processor and Descriptive Summarizer

### Script Overview
This Python script processes CSV files in the current working directory, organizes the data based on categories found within the CSV, and uses the OpenAI API to generate descriptive summaries for different sections of the CSV. The generated summaries are then saved as markdown files in organized folders, providing an easy-to-read overview of the content.

### Detailed Use/Features
1. **CSV File Processing**: The script identifies all CSV files in the current directory and processes them one by one.
2. **Directory Management**: For each CSV file, a dedicated directory is created, and the CSV file is moved into it for better organization.
3. **Data Cleaning**: The script cleans the 'Category' column of the CSV, filling NaN values and trimming whitespace.
4. **Sectioning**: The CSV content is divided into sections based on unique categories. Special handling is provided for 'Introduction' and 'Conclusion' sections, merging them appropriately with adjacent sections.
5. **API Integration**: For each section, the script sends a request to the OpenAI API to generate a descriptive summary. The API prompt is currently set as a placeholder (`<prompt_here>`), which should be customized to suit specific summary requirements.
6. **Summary Generation and Storage**: Summaries received from the API are saved as markdown (.md) files in the corresponding directory for easy access and readability.
7. **Sanitization**: Filenames are sanitized to remove invalid characters, ensuring compatibility across different file systems.
8. **Logging**: The script logs its actions, such as file moves, section findings, and API responses, providing transparency of operations.

### Installation
#### Requirements
- Python 3.7 or higher
- Required Python libraries: `pandas`, `requests`, `shutil`, and `re`.
- OpenAI API Key (must be acquired and set in the script).

#### Installation Steps
1. **Clone the Repository or Download the Script**: Save the provided script file to your local machine.
2. **Set Up Python Environment**: Ensure Python 3.7 or higher is installed on your system. Install required libraries if not already available:
   ```bash
   pip install pandas requests
   ```
3. **Acquire OpenAI API Key**: Obtain an API key from [OpenAI](https://platform.openai.com/) and replace the placeholder `<your_api_key_here>` in the script with your actual key.
4. **Customize API Prompt**: Replace `<prompt_here>` with an appropriate prompt to guide the AI in generating summaries tailored to your needs.

#### Usage
1. **Place the Script in Your Desired Directory**: Ensure that all CSV files you wish to process are in the same directory as the script.
2. **Run the Script**:
   ```bash
   python your_script_name.py
   ```
3. **Follow the Script Output**: The script will log its actions, such as identifying CSV files, processing them, creating directories, and generating summaries. All markdown summary files will be saved in their respective folders created by the script.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. This script has only been tested on Windows 11, and its compatibility with other operating systems is not guaranteed. Users are advised to back up their data before running the script to prevent any accidental loss of files.