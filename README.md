Postcode Info Finder
A command-line Python program that looks up UK postcodes using the postcodes.io API and displays location details.

Concepts Used
requests Library — queries the postcodes.io REST API with a cleaned postcode.

Exception Handling — catches RequestException for network failures and checks the API's status field for bad lookups.

Dictionary Access with .get() — safely reads fields like country, region, and latitude with 'N/A' fallbacks.

Features
Postcode Lookup — spaces are stripped and input uppercased before the API call.

Detailed Results — displays postcode, country, region, latitude, and longitude.

Retry Loop — re-prompts for a postcode until a valid one is found.

Improvements
Replace Recursion with a Loop — main() calls itself for "search again", which stacks frames and duplicates the intro; wrap the whole flow in one while loop.

Validate Postcode Format — nothing checks the input looks like a UK postcode; obvious typos waste API calls.

Clean Exit Handling — the else branch just return again, which does nothing; use break/continue and drop the hard exit() call from a helper.
