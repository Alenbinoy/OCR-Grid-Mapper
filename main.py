import requests
from bs4 import BeautifulSoup

def print_secret_message(url):
    """
    Fetches data from a published Google Doc, parses the coordinates,
    and prints the resulting secret message grid.
    """
    try:
        # 1. Fetch the content from the URL
        response = requests.get(url)
        response.raise_for_status()  # Ensure the request was successful
        
        # 2. Parse HTML to find the table
        soup = BeautifulSoup(response.text, 'html.parser')
        table = soup.find('table')
        if not table:
            print("Error: Could not find a table in the document.")
            return

        # 3. Extract data from table rows
        # We skip the first row as it contains headers
        data = []
        rows = table.find_all('tr')
        
        for row in rows[1:]:
            cells = row.find_all('td')
            if len(cells) >= 3:
                try:
                    # The format is usually: x-coord, char, y-coord
                    # Using .text.strip() to clean whitespace
                    x = int(cells[0].text.strip())
                    char = cells[1].text.strip()
                    y = int(cells[2].text.strip())
                    data.append((x, y, char))
                except ValueError:
                    # Skip rows that don't have valid integers for coordinates
                    continue

        if not data:
            print("Error: No valid data found in the table.")
            return

        # 4. Determine grid dimensions
        max_x = max(item[0] for item in data)
        max_y = max(item[1] for item in data)

        # 5. Create the grid filled with spaces
        # grid[y][x]
        grid = [[' ' for _ in range(max_x + 1)] for _ in range(max_y + 1)]

        # 6. Populate the grid
        for x, y, char in data:
            grid[y][x] = char

        # 7. Print the grid
        # IMPORTANT: The problem states (0,0) is the bottom corner.
        # In a standard terminal/text print, we start from the top.
        # Therefore, we iterate from max_y down to 0.
        for y in range(max_y, -1, -1):
            row_string = "".join(grid[y])
            print(row_string)

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

# Example usage:
url = "https://docs.google.com/document/d/e/2PACX-1vSvM5gDlNvt7npYHhp_XfsJvuntUhq184By5xO_pA4b_gCWeXb6dM6ZxwN8rE6S4ghUsCj2VKR21oEP/pub"
print_secret_message(url)
