# OCR Grid Mapper

# 🧩 GridReveal: Coordinate Grid Renderer

**GridReveal** is a Python-based utility that transforms fragmented spatial data from a public Google Doc into a visual secret message. By parsing $(x, y)$ coordinates and their associated Unicode characters, the tool reconstructs a 2D grid to reveal hidden uppercase letters.

## 🚀 How it Works
The tool acts as a data visualizer. Instead of reading text linearly, it treats a Google Doc table as a map:
1. **Fetches** the HTML content of a published Google Doc.
2. **Parses** the table to extract x-coordinates, y-coordinates, and characters.
3. **Maps** these characters onto a 2D plane.
4. **Renders** the grid in a fixed-width format, ensuring the y-axis is correctly inverted so the message appears right-side up.

## ✨ Features
- **Web Scraping**: Uses `BeautifulSoup4` to handle HTML table parsing.
- **Dynamic Scaling**: Automatically detects the maximum X and Y coordinates to create a grid of any size.
- **Coordinate Correction**: Correctly handles the Cartesian-to-Terminal coordinate shift (rendering $y=0$ at the bottom).
- **Robust Parsing**: Includes error handling for invalid coordinates or empty tables.

## 🛠️ Installation

### Prerequisites
Ensure you have Python 3.x installed on your system.

### Dependencies
This project requires the `requests` and `beautifulsoup4` libraries. Install them using pip:

```bash
pip install requests beautifulsoup4

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------
📖 Usage
Clone this repository or save the main.py file.
Run the script and provide a URL to a published Google Doc containing the coordinate table.
from main import print_secret_message

# Example URL of a published Google Doc
url = "https://docs.google.com/document/d/e/YOUR_PUBLISHED_ID/pub"
print_secret_message(url)

📊 Example Output
If the input data contains coordinates for the letter 'F', the output will look like this:

█▀▀▀
█▀▀ 
█

⚙️ Technical Complexity
Time Complexity: $O(N + (W \cdot H))$, where $N$ is the number of characters in the table, $W$ is the maximum width, and $H$ is the maximum height.
Space Complexity: $O(W \cdot H)$ to store the 2D grid before printing.

📜 License
This project is open-source and available under the MIT License [blocked].


***

### 💡 Tips for your Project Folder:
To make your project look truly professional, your folder should look like this:
*   `main.py` (The Python code)
*   `README.md` (The file I just gave you)
*   `requirements.txt` (A file containing just these two lines: `requests` and `beautifulsoup4`)

**If you want to create the `requirements.txt` quickly, just run this in your terminal:**
```bash
pip freeze > requirements.txt

