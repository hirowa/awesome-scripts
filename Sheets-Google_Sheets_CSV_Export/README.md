## Google Sheets CSV Export Script
### Script Overview
This Google Apps Script automates the process of exporting data from a specified sheet in a Google Spreadsheet to a CSV file. The CSV file is saved in a specific folder hierarchy in Google Drive. The script supports dynamic folder creation, and allows you to easily save the sheet's contents with a timestamped filename in CSV format.

### Detailed Use/Features
1. **Sheet Selection**: The script targets a specific sheet (customizable by changing the `sheetName` variable) in the active Google Spreadsheet.
2. **Folder Hierarchy**: It defines a folder path where the CSV file will be saved. If any folder in the hierarchy doesn't exist, the script will create it.
3. **Filename Creation**: The script generates a new filename with the current date (in `YYYY-MM-DD` format), combined with the original Google Spreadsheet's name and the sheet's name.
4. **CSV Conversion**: The selected sheet's data is converted to CSV format, handling cases like embedded commas or double quotes in cells.
5. **Google Drive Integration**: After converting the data to CSV, the script saves the file in the specified Google Drive folder.
6. **User Notification**: Once the file is saved, a message is displayed to the user showing the full folder path and the name of the saved file.

### Installation
#### Requirements
- Google Apps Script environment (via Google Sheets)
- Active Google Sheet with a sheet that matches the specified `sheetName`
- Google Drive access

#### Installation Steps
1. Open your Google Spreadsheet.
2. Navigate to **Extensions > Apps Script**.
3. Copy and paste the provided script into the editor.
4. Modify the `sheetName` and `folderPath` variables as needed:
   - `sheetName`: The name of the sheet to be exported.
   - `folderPath`: An array specifying the folder hierarchy in Google Drive where the CSV will be saved.
5. Save the script and close the editor.
6. Run the `saveAutomationSheetAsCSV` function from the script editor, or bind it to a button within the Google Spreadsheet UI for ease of use.

#### Usage
1. Ensure that the Google Sheet has the correct `sheetName` and that the target folders (if they already exist) are named as defined in the `folderPath`.
2. Run the script either manually from the Apps Script editor or via a custom menu or button you can create in your Google Sheet.
3. After running, the script will create a CSV file in the designated Google Drive folder, with the format `YYYY-MM-DD_<SpreadsheetName>_<SheetName>.csv`.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the code presented here has been generated with the assistance of AI and may contain errors or require adjustments for specific use cases. Users are advised to review and test the script with their data and ensure that the intended folders and files are appropriately backed up before running.