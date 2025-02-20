import argparse
import requests
import os
import re
from urllib.parse import urljoin
import random
import time
import asyncio
from playwright.async_api import async_playwright
from bs4 import BeautifulSoup

# Banner with ASCII art for "Hidden Endpoint Finder"
BANNER = """
 _    _ _     _       _____ _           _____              _____       _       
| |  | (_)   | |     |  __ \\ |         |  __ \\            |  __ \\     | |      
| |__| |_  __| |_   _| |  | | ___ _ __ __ _| |  | |_ _ __ _| |  | |_ _| |_ ___ 
|  __  | |/ _` | | | | |  | |/ _ \\ '__/ _` | |  | | '__/ _` | |  | __| '__/ _ \\
| |  | | | (_| | |_| | |__| |  __/ | | (_| | |__| | | | (_| | |__| |_| | |  __/
|_|  |_|_|\\__,_|\\__, |_____/ \\___|_|  \\__,_|_____/|_|   \\__,_|_____\\__|_|  \\___|
               __/ |                                                        
              |___/                                                          
"""
print(BANNER)

# Regular expressions for JS files and hidden endpoints
ENDPOINT_REGEX = re.compile(r'["\'](\/[^"\']+)["\']')
JS_REGEX = re.compile(r'src=["\'](.*?\.js)["\']')
unwanted_chars = ['*', '#', '<', '>']

# Store unique endpoints and crawled JS files
found_endpoints = set()
crawled_js = set()

async def fetch_js_files_with_playwright(url):
    """Uses Playwright to extract all loaded JavaScript files dynamically."""
    js_files = set()
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, args=["--disable-blink-features=AutomationControlled"])
        context = await browser.new_context()
        page = await context.new_page()

        async def intercept_response(response):
            """Intercepts JS file responses."""
            if response.request.resource_type == "script":
                js_files.add(response.url)

        page.on("response", intercept_response)
        
        try:
            print(f"Navigating to {url}...")
            await page.goto(url, wait_until="load", timeout=30000)
        except Exception as e:
            print(f"Error: {e}")
        
        await browser.close()
    return js_files

def find_endpoints_in_js(js_file_url):
    """Finds hidden endpoints in a JS file."""
    try:
        print(f"Extracting endpoints from {js_file_url}...")
        response = requests.get(js_file_url)
        if response.status_code == 200:
            endpoints = ENDPOINT_REGEX.findall(response.text)
            for endpoint in endpoints:
                # remove bad item
                if not any(char in endpoint for char in unwanted_chars):
                    found_endpoints.add(endpoint)
        else:
            print(f"Failed to fetch {js_file_url} with status code {response.status_code}")
    except Exception as e:
        print(f"Error fetching JS file {js_file_url}: {e}")

def crawl_url(url):
    """Crawl a given URL for JS files and find hidden endpoints."""
    js_files = set()

    try:
        print(f"Fetching page: {url}")
        response = requests.get(url)
        if response.status_code == 200:
            # Find JS files in the page
            js_files.update(JS_REGEX.findall(response.text))

            for js_file in js_files:
                # Absolute URL for JS file
                js_file_url = urljoin(url, js_file)
                find_endpoints_in_js(js_file_url)
        else:
            print(f"Failed to fetch {url} with status code {response.status_code}")
    except Exception as e:
        print(f"Error fetching page {url}: {e}")

def parse_arguments():
    """Parses command-line arguments."""
    parser = argparse.ArgumentParser(description="Hidden Endpoint Finder")

    parser.add_argument("-u", "--url", type=str, help="URL to crawl for hidden endpoints")
    parser.add_argument("-js", "--js_file", type=str, help="Path or URL of JS file to find hidden endpoints")
    parser.add_argument("-m", "--multi_urls", type=str, help="Text file containing list of URLs to crawl")
    parser.add_argument("-o", "--output", type=str, default="output.txt", help="Output file to save found endpoints")
    
    return parser.parse_args()

def main():
    """Main function to handle the crawling process."""
    args = parse_arguments()

    if args.url:
        crawl_url(args.url)
    elif args.js_file:
        find_endpoints_in_js(args.js_file)
    elif args.multi_urls:
        with open(args.multi_urls, "r") as f:
            urls = f.readlines()
            for url in urls:
                crawl_url(url.strip())

    if found_endpoints:
        with open(args.output, "w") as f:
            for endpoint in found_endpoints:
                f.write(endpoint + "\n")
        print(f"Found endpoints saved to {args.output}")
    else:
        print("No endpoints found.")

if __name__ == "__main__":
    main()
