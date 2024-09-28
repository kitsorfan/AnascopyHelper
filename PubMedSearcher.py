import os
import re
import requests
from bs4 import BeautifulSoup


class PubMedSearcher:
    def __init__(self, term, output_file, size=200, filters=None):
        self.term = term
        self.output_file = output_file
        self.size = size
        self.filters = filters or []
        self.base_url = "https://pubmed.ncbi.nlm.nih.gov/"
        
        # Initialize the output file
        self.initialize_file()

    def initialize_file(self):
        """Clear existing content in the output file."""
        if os.path.exists(self.output_file):
            with open(self.output_file, 'w') as file:
                pass  # Clear the content

    def build_url(self, page):
        """Construct the URL for the search query."""
        params = {
            'term': self.term,
            'size': self.size,
            'page': page
        }
        
        # Combine filters into the URL
        url = f"{self.base_url}?{requests.compat.urlencode(params)}"
        for filter_param in self.filters:
            url += f"&filter={filter_param}"
        
        return url

    def search(self):
        """Perform the search and write titles to the output file."""
        all_titles = []
        page = 1
        # Build the URL for the current page
        page_url = self.build_url(page)
        response = requests.get(page_url)
        
        # Check if the request was successful
        if response.status_code == 200:
        # Extract the number of total results using a regular expression
            match = re.search(r'totalResults: parseInt\("(\d+)"', response.text)
            if match:
                totalResultsNumber = int(match.group(1))  # Convert the extracted number to an integer
            else:
                print("Total results number not found in the response.")
        else:
            print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")

        remainingTitles = totalResultsNumber # a large numbrer
        while remainingTitles>0:
            # Build the URL for the current page
            page_url = self.build_url(page)
            response = requests.get(page_url)
            
            # Check if the request was successful
            if response.status_code != 200:
                print(f"Failed to retrieve data. HTTP Status Code: {response.status_code}")
                        
            # Parse the HTML content with BeautifulSoup
            soup = BeautifulSoup(response.text, 'lxml')
            titles = soup.find_all(class_='docsum-title')

            remainingTitles-=len(titles)
            # If no titles are found, break the loop (end of results)
            if not titles:
                print(f"No more titles found on page {page}.")
                break

            # Open the output file to append titles
            with open(self.output_file, 'a') as file:
                for title in titles:
                    # Remove <b> tags and get the text
                    for bold_tag in title.find_all('b'):
                        bold_tag.unwrap()  # Remove <b> tags but keep the text
                    
                    title_text = title.get_text(strip=True)
                    title_text = " ".join(title_text.split()).replace('%20', ' ').strip()
                    file.write(title_text + "\n")
                    all_titles.append(title_text)

            # Increment the page number for the next request
            page += 1

        # Print the total number of titles collected
        return len(all_titles)

