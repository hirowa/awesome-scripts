function saveAutomationSheetAsCSV() {
  // Define the target sheet and folder path
  var sheetName = "sheetName";
  var folderPath = ["folderName1", "folderName2", "folderName3"];

  // Get the active spreadsheet and the specific sheet
  var spreadsheet = SpreadsheetApp.getActiveSpreadsheet();
  var sheet = spreadsheet.getSheetByName(sheetName);
  
  if (!sheet) {
    SpreadsheetApp.getUi().alert('Sheet named "' + sheetName + '" not found.');
    return;
  }

  // Get the original file name and today's date
  var originalFileName = spreadsheet.getName();
  var today = new Date();
  
  // Format the date as YYYY-MM-DD
  var dateString = today.getFullYear() + "-" +
                   ("0" + (today.getMonth() + 1)).slice(-2) + "-" +
                   ("0" + today.getDate()).slice(-2);
  
  // Create a new file name with today's date + original file name
  var newFileName = dateString + "_" + originalFileName + "_" + sheetName + ".csv";

  // Get the data from the "Automation" sheet
  var lastRow = sheet.getRange("A:A").getValues().filter(String).length; // Find last non-empty row in column A
  var dataRange = sheet.getRange(1, 1, lastRow, sheet.getLastColumn()); // Get the range from A1 to the last non-empty row

  // Get the values from the sheet and convert them to CSV format
  var csvContent = convertRangeToCsv(dataRange.getValues());

  // Find or create the target folder in Google Drive
  var folder = getOrCreateFolder(folderPath);
  
  // Create a CSV file in the target folder
  var file = folder.createFile(newFileName, csvContent, MimeType.CSV);
  
  // Notify the user with dynamic folder and sheet names
  var folderPathString = folderPath.join(" > ");
  SpreadsheetApp.getUi().alert('Sheet "' + sheetName + '" saved to Google Drive under "' + folderPathString + '" as: ' + newFileName);
}

function convertRangeToCsv(data) {
  return data.map(function(row) {
    return row.map(function(cell) {
      return typeof cell === "string" ? '"' + cell.replace(/"/g, '""') + '"' : cell;
    }).join(",");
  }).join("\n");
}

function getOrCreateFolder(pathArray) {
  var folder = DriveApp.getRootFolder(); // Start from "My Drive"
  for (var i = 0; i < pathArray.length; i++) {
    var folders = folder.getFoldersByName(pathArray[i]);
    if (folders.hasNext()) {
      folder = folders.next();
    } else {
      folder = folder.createFolder(pathArray[i]); // Create folder if it doesn't exist
    }
  }
  return folder;
}
