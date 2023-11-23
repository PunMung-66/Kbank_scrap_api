import requests
from bs4 import BeautifulSoup

# URL of the webpage you want to scrape
url = "https://kbiz.kasikornbank.com/menu/account/account-summary"

# Send an HTTP request to the URL
response = requests.get(url)

# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Parse the HTML content of the page
    soup = BeautifulSoup(response.text, 'html.parser')

    # Find the <span> tag with the specified class
    span_tag = soup.find('span', {'class': 'green'})

    # Extract the text content inside the <span> tag
    if span_tag:
        result = span_tag.text.strip()
        print("\n\nExtracted value:", result)
    else:
        print("Span tag not found.")
else:
    print("Failed to retrieve the webpage. Status code:", response.status_code)
