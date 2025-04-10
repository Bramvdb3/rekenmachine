from urllib.request import urlopen
from bs4 import BeautifulSoup

# URL of the HTML page containing the data
url = "http://py4e-data.dr-chuck.net/comments_2031143.html"

# Function to fetch HTML content from the URL and parse it
def parse_html_and_extract_sum(url):
    # Fetching the HTML content from the URL
    html = urlopen(url).read()
    
    # Parsing the HTML using BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')
    
    # Extracting all <span> tags that contain numbers
    span_tags = soup('span')
    
    # Initializing sum variable
    total_sum = 0
    
    # Looping through each <span> tag, extracting numbers and computing sum
    for tag in span_tags:
        # Extracting the text content of the <span> tag
        content = tag.contents[0]
        
        # Converting the extracted content to an integer and adding to sum
        total_sum += int(content)
    
    return total_sum

# Calling the function to fetch HTML, extract numbers, and compute sum
total_sum = parse_html_and_extract_sum(url)

# Printing the computed sum
print(f"The sum of the numbers in the HTML file is: {total_sum}")