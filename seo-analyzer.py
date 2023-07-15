import requests
from bs4 import BeautifulSoup
import sys
import re
import collections
import os
from datetime import datetime

def fetch_and_analyze(url, keyword=None):
    # Fetch the webpage
    try:
        response = requests.get(url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"Error fetching webpage: {e}")
        return

    # Parse the HTML content of the webpage
    soup = BeautifulSoup(response.text, 'html.parser')

    # Define the HTML tags that are relevant to SEO
    seo_relevant_tags = ['title', 'meta', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'a', 'img']

    # Find and print out the SEO-relevant HTML tags and their attributes
    for tag in soup.find_all(seo_relevant_tags):
        print(f"Tag: {tag.name}")
        for attr, value in tag.attrs.items():
            print(f"  Attribute: {attr}, Value: {value}")
        print(f"  Content: {tag.text.strip()}")
        print()

    # If a keyword is provided, analyze its usage
    if keyword:
        keyword_count = len(re.findall(keyword, soup.text, re.IGNORECASE))
        print(f"Keyword '{keyword}' found {keyword_count} times")

    # Analyze the links on the webpage
    internal_links = 0
    external_links = 0
    broken_links = []
    for link in soup.find_all('a'):
        href = link.get('href')
        if href.startswith('/'):
            internal_links += 1
        elif href.startswith('http'):
            external_links += 1
            try:
                response = requests.head(href, allow_redirects=True, timeout=5)
                if response.status_code != 200:
                    broken_links.append(href)
            except requests.exceptions.RequestException:
                broken_links.append(href)
    print(f"Internal links: {internal_links}")
    print(f"External links: {external_links}")
    print(f"Broken links: {len(broken_links)}")

    # Count the frequency of each word in the text of the webpage
    text = soup.get_text()
    words = re.findall(r'\w+', text.lower())
    word_counts = collections.Counter(words)
    print("Word frequencies:")
    for word, count in word_counts.most_common():
        print(f"  {word}: {count}")

    return {
        'internal_links': internal_links,
        'external_links': external_links,
        'broken_links': broken_links,
        'word_frequencies': word_counts.most_common()
    }

def main():
    print("""
      _____ ______ ____                         _                    
     / ____|  ____/ __ \      /\               | |                   
    | (___ | |__ | |  | |    /  \   _ __   __ _| |_   _ _______ _ __ 
     \___ \|  __|| |  | |   / /\ \ | '_ \ / _` | | | | |_  / _ \ '__|
     ____) | |___| |__| |  / ____ \| | | | (_| | | |_| |/ /  __/ |   
    |_____/|______\____/  /_/    \_\_| |_ \__,_|_ \__, /___ \___|_|   
                                                   __/ |             
                                                  |___/              
    by TUKRU
    """)

    # Get the URL from the command line arguments or prompt the user for a URL
    if len(sys.argv) > 1:
        url = sys.argv[1]
    else:
        url = input("Enter a URL: ")

    # Get the keyword from the user
    keyword = input("Enter a keyword (optional): ")

    while True:
        print("\nOptions:")
        print("1. Analyze URL")
        print("2. Compare with another URL")
        print("3. Help")
        print("4. Exit")
        option = input("Choose an option: ")

        if option == '1':
            result = fetch_and_analyze(url, keyword)
            if result:
                save_report(url, result)
        elif option == '2':
            compare_url = input("Enter a URL to compare with: ")
            print(f"\nAnalysis for {url}:")
            result1 = fetch_and_analyze(url, keyword)
            print(f"\nAnalysis for {compare_url}:")
            result2 = fetch_and_analyze(compare_url, keyword)
            if result1:
                save_report(url, result1)
            if result2:
                save_report(compare_url, result2)
        elif option == '3':
            print("\nHelp:")
            print("Option 1: Analyze the current URL")
            print("Option 2: Compare the current URL with another URL")
            print("Option 3: Show this help message")
            print("Option 4: Exit the script")
        elif option == '4':
            break
        else:
            print("Invalid option. Please choose a number between 1 and 4.")

def save_report(url, result):
    # Create the reports directory if it doesn't exist
    if not os.path.exists('reports'):
        os.makedirs('reports')

    # Create a filename based on the current date and the domain of the URL
    date = datetime.now().strftime('%Y-%m-%d')
    domain = re.search(r'https?://([^/]+)/', url).group(1)
    filename = f'reports/{date}_{domain}.txt'

    # Write the report to the file
    with open(filename, 'w') as f:
        f.write(f"Report for {url} on {date}\n")
        f.write(f"Internal links: {result['internal_links']}\n")
        f.write(f"External links: {result['external_links']}\n")
        f.write(f"Broken links: {len(result['broken_links'])}\n")
        for link in result['broken_links']:
            f.write(f"  {link}\n")
        f.write("Word frequencies:\n")
        for word, count in result['word_frequencies']:
            f.write(f"  {word}: {count}\n")

    print(f"Report saved to {filename}")

if __name__ == "__main__":
    main()
