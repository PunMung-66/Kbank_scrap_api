import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://pantip.com/topic/36611712"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <h2> tag with the specified class
    h2_tag = soup.find('h2', {'class': 'display-post-title'})

    # Extract the text content inside the <h2> tag
    if h2_tag:
        result = h2_tag.text.strip()
        print("\n\nExtracted value:", result)
    else:
        print("h2 tag not found.")
else:
    print("\n\nFailed to retrieve the webpage. Status code:", response.status_code)
