# Hidden Endpoint Finder

**Hidden Endpoint Finder** is a command-line tool designed to crawl websites or JavaScript files to find hidden endpoints. This tool can identify endpoint patterns that may be used for potential security vulnerabilities such as broken access control, security misconfigurations, or other issues in web applications.

It crawls JavaScript files for endpoint links, helping bug bounty hunters, penetration testers, and security researchers discover hidden API endpoints or endpoints that may not be linked directly on the front-end.

## Features

- **Crawl URLs**: Provide a URL to crawl for hidden endpoints.
- **JavaScript File Crawling**: Fetch and extract hidden endpoints from linked JavaScript files.
- **Multi-URL Support**: Provide a `.txt` file with multiple URLs, and the tool will crawl each URL and save the found endpoints separately.
- **Output to File**: Save all discovered endpoints into a file for easy analysis.
- **Playwright Integration**: Uses Playwright for dynamically loaded JavaScript files, allowing the tool to capture endpoints in single-page applications (SPAs).
- **Regex Filtering**: Uses regular expressions to find endpoints in JS files and pages.



## Installation

1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/hidden-finder.git
   cd hidden-endpoint-finder
   pip install -r requirements.txt (requests,playwright)

  Usages:
To use the Hidden Endpoint Finder, you can run the script with various options:
python3 crawl.py 

Options:
-h, --help
Shows the help message and exits.

-v, --version
Displays the version of the tool.

-js, --js-file <js_file>
Takes a path to a local .js file and finds hidden endpoints from it.

--multi_urls <txt_file>
Provides a .txt file containing a list of URLs (one URL per line). The tool will process each URL individually and save the results in separate files based on the target’s name.

-m, --multi
Allows you to give multiple URLs directly in the command line for endpoint discovery.

-o, --output <output_file>
Saves the output of the discovered endpoints into the specified file.

Examples:
1. Crawling a JavaScript file to find endpoints:
To find hidden endpoints from a specific JavaScript file, use the -js option:
python3 crawl.py -js path/to/your/file.js

2. Crawling a single URL to find hidden endpoints:
You can pass a URL directly in the command to find endpoints:
python3 crawl.py -m http://example.com

3. Crawling multiple URLs from a .txt file:
If you have a .txt file containing multiple URLs, one per line, you can use the --multi_urls flag:
python3 crawl.py --multi_urls urls.txt

This will process each URL and save the results in separate files named after the target URL.

4. Saving the results in a specific output file:
To save the discovered endpoints in a specific file, use the -o option:
python3 crawl.py -m http://example.com -o results.txt
This will save the endpoints into results.txt.

Example of a urls.txt file:
http://example.com
http://anotherexample.com
http://yetanotherexample.com

