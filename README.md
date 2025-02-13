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
