## Postcode Finder
A command-line postcode lookup tool written in Python. It uses the requests module to query the postcodes.io API and displays information about any UK postcode.

## Features
Postcode Input — Prompts for a UK postcode, automatically uppercased and stripped.

Input Cleaning — Removes spaces from the postcode before sending it to the API.

Live Lookup — Fetches data from https://api.postcodes.io/postcodes/{postcode}.

Info Display — Prints the postcode, country, region, latitude, and longitude, falling back to N/A for missing fields.

Retry on Failure — Re-prompts for a postcode if the lookup fails or the postcode isn't found.

Error Handling — Catches network errors with requests.exceptions.RequestException and checks the API's status field.

Search Again — Restarts the lookup if the user answers y.

## Technologies Used
text
| Technology | Purpose |
|---|---|
| Python | Application logic |
| `requests` | Sends HTTP requests to the postcodes.io API |
| postcodes.io | Provides UK postcode data |
| f-strings | Builds the API URL and output messages |
| `try / except` | Handles network errors |
| `raise_for_status()` | Detects HTTP error responses |
| `dict.get()` | Safely reads fields with fallbacks |
| `input()` / `print()` | Console interaction |
<!-- -->
## How to Use It
Install Python 3.6 or newer from python.org and make sure it's added to your PATH.

Install the requests library by running pip install requests.

Save the code as postcode_finder.py.

Open a terminal in the folder containing the file.

Run python postcode_finder.py.

Enter a UK postcode (e.g. SW1A 1AA), view the results, then answer y or n when asked to search again.

## Improvements
Use a loop instead of recursion — main() calls itself when the user searches again, which stacks frames and will eventually hit Python's recursion limit; a while True loop is safer.

Validate the postcode format — the code sends whatever the user types straight to the API; a regex check for a valid UK postcode shape would catch typos before making the request.
