# WebScreenShotTool
A Python script that uses Selenium to take screenshots of basic enum pages like robots.txt. The script sets the zoom level, waits for the page to load, gets the response code, saves the screenshot, and adds text overlays. The main function takes a website URL as input and saves the screenshots in a timestamped folder.

**Usage:**
```bash
python script.py https://www.google.com/
```

**Example Output**
![screenshot___git](https://github.com/akash0x01/WebScreenShotTool/assets/145096386/45534a21-05b5-4fb4-822e-996e500568a5)
![screenshot__robots_txt](https://github.com/akash0x01/WebScreenShotTool/assets/145096386/0a7cd2c7-1e2f-48bc-abc9-903aa4de28e6)

## ChatGPT Prompt
I used ChatGPT prompts to make this tool. Below is chatgpt prompt I used.
```markdown
Generate a Selenium-based program to take annotated screenshots of multiple sub-locations under a given URL. Following is the requirement specification.

# Overall Objective
The program takes a URL as an argument and navigates to different sub-locations under that URL to take screenshots. It annotates each screenshot with the URL and the HTTP response code. The screenshots are saved in a folder named by the current timestamp. The program is intended to work in headless mode so as not to interrupt the current user's workflow.

# Code Structure
1. **Import Statements**: Importing all required libraries and modules like `webdriver` from Selenium, `Image` from PIL, and `requests`.

2. **Utility Functions**:
	- `sanitize_filename(filename)`: Replaces any character that is not alphanumeric or underscore with an underscore.
	- `take_screenshot(driver, url, sub_url, file_name, folder_name)`: Responsible for navigation, taking screenshots, annotation, and saving the screenshot in a folder.
3. **Main Function** (**`main(url)`**):
	- Cleans up the URL by removing the trailing /.
	- Initializes Selenium WebDriver with Chrome options for headless mode.
	- Iterates through a list of sub-locations, calling **`take_screenshot()`** for each.

# Key Features
**1. Headless Mode**: The program runs without opening a GUI window to prevent interruption.
**2. Full HD Resolution**: The window size is set to 1920x1080 pixels.
**3. Timestamp Folder**: Screenshots are saved in a new folder labeled with the current timestamp.
**4. URL Sanitization**: Any special characters in the filename are replaced by underscores.
**5. Annotations**: The URL and HTTP response code are annotated in red text on each screenshot.
**6. Zoom Level**: The program sets the zoom level of the webpage to 110%.
**7. Console Output**: The program prints a message to the console each time a screenshot is successfully saved.

# Usage
Execute the program from the terminal by passing the URL as an argument:

`
python script.py http://example.com
`

# Limitations and Considerations
- Error handling is basic; for instance, the program will only wait for 10 seconds for the webpage to load.
- The program assumes that the website is reachable and does not require login/authentication.

# Future Improvements
- The script could be modified to handle login pages, pop-ups, or other interactive elements.
- You could use threading or multiprocessing to take screenshots faster if dealing with a large number of sub-locations.
```
