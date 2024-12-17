## Image Grid Creator using ImageMagick
### Script Overview
This guide describes how to create an image grid using ImageMagick, a powerful open-source software suite for image manipulation. The provided script (`GridCreator.bat`) uses ImageMagick's `montage` command to create a grid layout of images in a folder. Additionally, resizing options are provided to optimize the grid's size if needed.

### Detailed Use/Features
1. **Grid Creation**: 
   - The script generates a tiled grid from all image files (`*.png`) in the current directory.
   - The resulting grid layout arranges the images into rows and columns according to the specified tile format (e.g., 3 images per row).
2. **Thumbnail Arrangement**:
   - Images are resized and positioned into a compact, tiled layout using the `montage` command.
   - The layout's geometry (spacing, size, and arrangement) is customizable via the `-geometry` and `-tile` options.
3. **Grid Optimization**:
   - The script includes a resizing command using `convert` to adjust the grid's dimensions if the final output is too large or heavy.
4. **Customizable Settings**:
   - Control the resolution using the `-density` flag.
   - Adjust thumbnail size and spacing using `-geometry`.

### Installation
#### Requirements
- **ImageMagick**: Ensure that ImageMagick is installed on your system. You can download it from the [official website](https://imagemagick.org).
- A system with command-line access (e.g., Command Prompt or Terminal).
- Supported file format: The script processes `.png` files by default but can be modified for other formats.

#### Installation Steps
1. Download and install ImageMagick by following the instructions on the [official website](https://imagemagick.org/script/download.php).
2. Save the provided batch script (`GridCreator.bat`) in the folder containing the images you want to process.
3. Confirm that the ImageMagick executables (`magick`, `montage`, and `convert`) are accessible from your command-line interface. Add ImageMagick to your system's PATH variable if necessary.

#### Usage
1. **Run the Batch Script**:
   - Place the `GridCreator.bat` script in the folder containing your images.
   - Double-click the batch file or run it via the command line:
     ```bash
     GridCreator.bat
     ```
   - This will execute the following command to create a grid layout:
     ```bash
     magick montage -density 300 -geometry +0+0 -tile 3x0 *.png Grid.png
     ```
     - `-density 300`: Sets the resolution to 300 DPI.
     - `-geometry +0+0`: Ensures no additional spacing between images.
     - `-tile 3x0`: Arranges the images into a grid with 3 images per row.
2. **Resizing the Grid (if needed)**:
   - Use the following command to resize the grid output:
     ```bash
     magick convert Grid.png -resize 100x100 ResizedGrid.png
     ```
   - Replace `100x100` with the desired dimensions to scale the output grid.

### Disclaimer
THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE, AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES, OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF, OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

Additionally, the provided script and instructions have been tested on a Windows 11 environment with ImageMagick. Compatibility with other operating systems is not guaranteed. Please ensure all data is backed up before executing the script, as it modifies image files and generates new outputs. Consult the [ImageMagick Command-line Options](https://legacy.imagemagick.org/script/command-line-options.php) for additional customization.