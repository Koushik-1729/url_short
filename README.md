# URL Shortener

This project provides both a URL Shortener GUI and a Flask API. The GUI allows you to enter a URL, select a shortening service, and generate a shortened URL. The Flask API handles the URL shortening and redirection.

### Features

- Enter a URL and generate a shortened URL using selected shortening service.
- Copy the shortened URL to the clipboard.
- Clear the input fields.

### Requirements

- Python 3.x
- pyperclip
- pyshorteners
- validators
- Tkinter (for the GUI)

### Usage

1. Run the following command to launch the URL Shortener GUI:

   ```shell
   python url_shortener_gui.py



## Installation

1. Clone the repository or download the script.

2. Install the required modules by running the following command:

   ```shell
   pip install pyperclip pyshorteners validators
Run the script using Python:
                   - python shorten.py

Usage:

-Enter the URL you want to shorten in the provided input field.

-Select a shortening service from the available options.

-Click the "Generate Short URL" button to generate the short URL.

-The generated short URL will appear in the second input field.

-Click the "Copy Short URL" button to copy the short URL to the clipboard.

-Click the "Clear Fields" button to reset the input fields.

# URL Shortener Flask API

### Features:
   - Insert URLs into the SQLite database with a randomly generated key.
   - Redirect shortened URLs to their corresponding original URLs.

### Requirements
   - Python 3.x
   - Flask
   - SQLite3
### Usage
 
   - Make a POST request to the /insert endpoint with the url parameter set to 
     the URL you want to shorten.

   - The API will return a response with the generated key for the shortened URL.

   - To access the original URL, make a GET request to 
     http://localhost:5000/{key}, where {key} is the generated key for the 
     shortened URL.

   - The API will redirect you to the original URL.
   
Contributing:
- Contributions are welcome! If you have any suggestions or improvements, please create a pull request or open an issue on the GitHub repository.

##Contact
- For any inquiries or additional information, please contact [koushik.yeruva02@gmail.com].
