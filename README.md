📮 Python Postcode Info Finder
A simple command-line tool built with Python that looks up information about any UK postcode. It uses the free postcodes.io API to fetch details like country, region, latitude, and longitude. It's a great beginner-to-intermediate project for learning about APIs, HTTP requests, JSON parsing, and error handling in Python.

📖 Python Postcode Info Finder
The Python Postcode Info Finder is a console-based application that lets users look up information about any UK postcode. The user enters a postcode (with or without spaces), and the program queries the free postcodes.io API to retrieve details about it.

The program displays:

Postcode – The normalized version returned by the API.

Country – e.g., England, Scotland, Wales, Northern Ireland.

Region – e.g., Greater London, South East.

Latitude – The geographic latitude.

Longitude – The geographic longitude.

If the postcode is invalid or not found, the user is re-prompted until a valid one is entered. After a successful lookup, the user can choose to search for more postcodes.

All inputs are cleaned automatically — spaces are stripped out and letters are converted to uppercase — so formats like sw1a 1aa, SW1A1AA, and sw1a1aa all work.

This project is ideal for anyone learning how to work with web APIs, JSON responses, and clean function-based design in Python.

✨ Features
UK postcode lookup – Works with any valid UK postcode.

Free API, no key required – Uses postcodes.io.

Automatic input cleaning – Uppercases letters and removes spaces before sending to the API.

Detailed results – Displays postcode, country, region, latitude, and longitude.

Safe field access – Uses .get() with "N/A" fallback for missing data.

Input validation – Keeps prompting until a valid postcode is entered.

API error handling – Catches network errors, timeouts, and HTTP failures.

Status code check – Verifies the API returned a 200 status before displaying data.

Repeat option – Look up more postcodes without restarting the program.

Entry-point guard – Uses if __name__ == "__main__": for clean script execution.

Modular design – Clear, single-purpose functions.

🛠️ What It Uses
Language & Library
Python 3

requests – A popular third-party library for making HTTP requests.

Install with: pip install requests

External API
postcodes.io — https://api.postcodes.io/postcodes/{postcode}

Free, no API key required.

Returns a JSON object containing detailed information about the postcode.

Key Functions
Function	Purpose
get_postcode()	Prompts the user for a UK postcode, uppercases it, and strips whitespace.
postcode_data(postcode)	Sends the cleaned postcode to the API and returns the result data. Handles network and status errors.
display_result(result)	Prints the postcode, country, region, latitude, and longitude in a clean layout.
main()	Runs the full program flow and handles the repeat prompt.
Key Variables
Variable	Purpose
postcode	The user's entered postcode.
clean	The postcode with spaces removed, ready for the API URL.
data	The full JSON response from the API.
result	The "result" field from the API response, containing postcode details.
Python Concepts Demonstrated
The requests library – Making HTTP GET requests.

JSON parsing – Using response.json() to get structured data.

Exception handling – try/except blocks for requests.exceptions.RequestException.

HTTP status checking – Using response.raise_for_status().

String methods – .upper(), .strip(), and .replace() for input cleaning.

F-strings – Formatting the API URL and output messages.

Dictionary access – Using .get() with default values for safety.

Functions – Modular, single-purpose function design.

Recursion – main() calls itself when the user chooses to search again.

if __name__ == "__main__": – Standard Python entry-point pattern.

while True loop – Retries on invalid postcodes.

Built-in Functions Used
input() – Reads user input from the console.

print() – Displays results and messages.

exit() – Terminates the program when the user chooses to quit.

📥 Download
You can download the source file from this repository and save it as a .py file:

text
postcode_finder.py
Then install the required library:

bash
pip install requests
▶️ How to Run
Make sure you have Python 3 installed (python.org).

Install the requests library:

bash
pip install requests
Save the code as postcode_finder.py.

Open a terminal or command prompt in the folder containing the file.

Run:

bash
python postcode_finder.py
Enter any UK postcode — with or without spaces — and the program will display information about it.

🐍 Made with Python
This project is written in Python 3 and uses the requests library to communicate with the free postcodes.io API. It's a clean, practical example of how to integrate a public web service into a small command-line application.

Whether you're a beginner learning about APIs or someone who needs a quick UK postcode lookup tool, this project is a great starting point.

💡 Possible Future Improvements
Fix the recursion flow – main() calls itself repeatedly, which can eventually hit Python's recursion limit. Consider using a while True loop instead.

Fix the "Try again" branch – Returning again from main() doesn't do anything because the return value is discarded. Should re-prompt or restart main().

Add more fields – e.g., parliamentary constituency, admin district, ward, or NHS region.

Save results to a file – Log lookups to a CSV or text file.

Bulk lookup – Support multiple postcodes at once using the API's bulk endpoint.

Reverse lookup – Given latitude and longitude, find the nearest postcode.

Format the output with color – Use colorama or ANSI codes for a nicer look.

Add distance calculation – Compute distance between two postcodes using their coordinates.

Build a Tkinter GUI version for a graphical interface.

📄 License
This project is free to use, modify, and distribute for personal or educational purposes.
