from bs4 import BeautifulSoup
import requests
import os





# Parameters for the search query
params = {
    'term': '(oral health) AND (advanced cancer)',  # Your search query
    'size': 200,  # Number of results per page
    'page': 1  # Initial page number
}

# Filters as a list (if necessary)
filters = ['lang.english', 'lang.greekmodern', 'years.2003-2023', 'hum_ani.humans']




# Define the file name
file_name = 'titles.txt'

# Initialize the file (clear existing content if it exists)
if os.path.exists(file_name):
    with open(file_name, 'w') as file:  # Open in write mode to clear the file
        pass  # Just clear the content

# Base URL for PubMed search
base_url = "https://pubmed.ncbi.nlm.nih.gov/"


# Combine filters into the URL manually
url = f"{base_url}?{requests.compat.urlencode(params)}"
for filter_param in filters:
    url += f"&filter={filter_param}"

# List to store all titles
all_titles = []

# Loop through multiple pages
while True:
    # Update the page number in the params
    params['page'] = params['page']  # Increment the page number for each loop
    page_url = f"{url}&page={params['page']}"  # Construct the URL with the updated page number
    
    # Make the GET request to PubMed
    response = requests.get(page_url)
    
    # Check if the request was successful
    if response.status_code != 200:
        print(f"Failed to retrieve data on page {params['page']}. HTTP Status Code: {response.status_code}")
        break

    # Parse the HTML content with BeautifulSoup
    soup = BeautifulSoup(response.text, 'lxml')

    # Find all elements with class 'docsum-title'
    titles = soup.find_all(class_='docsum-title')
    
    # If no titles are found, break the loop (end of results)
    if not titles:
        print(f"No more titles found on page {params['page']}. Ending the loop.")
        break
    # Replace all <b> tags with a space and preserve the text inside
    for title in titles:
        for bold_tag in title.find_all('b'):
            # Replace <b> with space around the text inside
            bold_tag.insert_before("")
            bold_tag.insert_after(" ")
            bold_tag.unwrap()  # Remove <b> tags but keep the text

    # Open a file to write the titles
    with open('titles.txt', 'a') as file:
        # Iterate through all the titles found
        for index, title in enumerate(titles, start=1):
            # Get the text inside the 'docsum-title' class
            title_text = title.get_text()

            # Remove extra spaces, quotes, replace %20 with space, and remove leading/trailing spaces
            title_text = " ".join(title_text.split()).replace('%20', ' ').strip()
        
            file.write(title_text+"\n")

    # Extract and print titles, append to all_titles list
    for title in titles:
        title_text = title.get_text(strip=True)
        print(title_text)
        all_titles.append(title_text)


    # Increment page number for next request
    params['page'] += 1

# Print the total number of titles collected
print(f"Total titles collected: {len(all_titles)}")


