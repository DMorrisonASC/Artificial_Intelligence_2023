# Author: Daeshaun Morrison, Muhlenberg College class of 2024(daeshaunkmorrison@gmail.com)
# Date: 11/25/2023
# Instructor: Professor Silveyra
# Description: Write a Python program that crawls the muhlenberg.edu site and stores the contents of 100 pages crawled in a separate .txt file. In each file, you will store:
# URL of the link
# Number of relative links in this file
# Number of absolute links in this file
# Contents of the HTML file
# You should only visit links that are HTML pages. However, you will count all other links for your totals (png, pdf, etc.)

# The output of the program will be the different files and a message that tells the user that the crawling has finished. It should list the number of pages retrieved and the number of relative, absolute, and total URLs found.
# Errors: Sometimes programs keeps retrying to get url that it has already visited

import os
import re
import requests
from urllib.parse import urljoin, urlparse

def get_links(html_content, base_url):
    """Extract the absolute and relative links from HTML content."""
    absolute_links = re.findall(r'href=["\'](https?://.*?)["\']', html_content)
    relative_links = re.findall(r'href=["\'](.*?)["\']', html_content)
    relative_links = [urljoin(base_url, link) for link in relative_links]
    return absolute_links, relative_links

def is_same_domain(url, domain):
    """Checks if the URL belongs to the specified domain."""
    parsed_url = urlparse(url)
    return parsed_url.netloc == domain

def save_page_contents(url, absolute_links, relative_links, html_content, output_dir):
    """Save the contents of a page into a .txt file."""
    file_name = os.path.join(output_dir, f"{hash(url)}.txt")
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"URL: {url}\n")
        file.write(f"Number of Absolute Links: {len(absolute_links)}\n")
        file.write(f"Number of Relative Links: {len(relative_links)}\n")
        file.write("HTML Content:\n")
        file.write(html_content)

def crawl(url, output_dir, domain, max_pages=100):
    """Crawls the given URL and stores the contents of pages in separate .txt files."""
    crawled_pages = 0
    absolute_urls = set()
    relative_urls = set()
    visited_urls = set()

    while crawled_pages < max_pages:
        try:
            response = requests.get(url)
            if response.status_code == 200 and 'text/html' in response.headers['Content-Type']:
                html_content = response.text
                absolute_links, relative_links = get_links(html_content, url)
                absolute_urls.update(absolute_links)
                relative_urls.update(relative_links)

                save_page_contents(url, absolute_links, relative_links, html_content, output_dir)

                visited_urls.add(url)
                crawled_pages += 1

                # Extract new URLs for crawling within the same domain
                new_urls = {u for u in absolute_links + relative_links if is_same_domain(u, domain)} - visited_urls
                if not new_urls:
                    break
                url = new_urls.pop()
            else:
                # Skip non-HTML pages
                visited_urls.add(url)
                url = next((u for u in absolute_urls.union(relative_urls) if u not in visited_urls and is_same_domain(u, domain)), None)
                if url is None:
                    break
        except Exception as e:
            print(f"Error crawling {url}: {e}")
            # next() function returns the next item of an iterator
            url = next((u for u in absolute_urls.union(relative_urls) if u not in visited_urls and is_same_domain(u, domain)), None)
            if url is None:
                break

    print(f"Crawling finished. Retrieved {crawled_pages} pages.")
    print(f"Number of Absolute URLs: {len(absolute_urls)}")
    print(f"Number of Relative URLs: {len(relative_urls)}")
    print(f"Total URLs found: {len(absolute_urls) + len(relative_urls)}")

if __name__ == "__main__":
    start_url = "https://www.muhlenberg.edu/"
    output_directory = "output"
    muhlenberg_domain = "www.muhlenberg.edu"
    os.makedirs(output_directory, exist_ok=True)
    crawl(start_url, output_directory, muhlenberg_domain)
