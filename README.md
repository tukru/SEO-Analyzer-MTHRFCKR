![SEO Analyzer](https://img.shields.io/badge/SEO-Analyzer-blue)
![Author](https://img.shields.io/badge/Author-TUKRU-green)

# SEO Analyzer

This is a Python script for analyzing the SEO of a webpage. It fetches a webpage, analyzes the HTML tags that are relevant to SEO, counts the frequency of each word in the text of the webpage, and analyzes the links on the webpage.

## Features

- **Fetching and Analyzing HTML Tags**: The tool fetches a webpage and analyzes the HTML tags that are relevant to SEO, such as the title tag, meta tags, heading tags (h1, h2, etc.), anchor tags (a), and image tags (img).
- **Keyword Analysis**: If a keyword is provided, the tool counts the number of times the keyword appears in the text of the webpage.
- **Link Analysis**: The tool analyzes the links on the webpage, counting the number of internal links (links to the same domain), external links (links to other domains), and broken links (links that return a non-200 HTTP status code).
- **Word Frequency Analysis**: The tool counts the frequency of each word in the text of the webpage, which can help identify the main topics of the webpage.
- **Saving Reports**: The tool saves a report of the analysis to a text file in a "reports" directory.

## Usage

You can run the script from the command line with the following command:

python3 seo_analyzer.py

css


When you run the script, it will prompt you for a URL to analyze. You can also optionally enter a keyword to analyze.

The script will then fetch and analyze the webpage, and print out the results. It will also save a report of the analysis to a text file in a "reports" directory.

## Dependencies

This script requires the following Python libraries:

- requests
- BeautifulSoup
- re
- collections
- os
- datetime

You can install these libraries using pip:

pip install -r requirements.txt

vbnet


(Note: The re, collections, os, and datetime libraries are part of the Python standard library and should be included with your Python installation, so you don't need to install them separately.)

## Author

This tool was created by [TUKRU](https://github.com/TUKRU).

