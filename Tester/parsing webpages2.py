import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

def get_next_name(url, position):
    """
    Retrieve the name at a specific position from the given URL.
    """
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    
    # Find all anchor tags (<a>) in the parsed HTML
    tags = soup('a')
    
    # Ensure position is within bounds
    if position <= len(tags):
        next_link = tags[position - 1].get('href')
        return next_link, tags[position - 1].text
    else:
        return None, None

def follow_links(start_url, count, position):
    """
    Follow links from the starting URL for the specified number of repetitions.
    """
    current_url = start_url
    sequence_names = []
    
    for _ in range(count):
        next_link, next_name = get_next_name(current_url, position)
        
        if next_link:
            print(f"Retrieving: {current_url}")
            sequence_names.append(next_name)
            current_url = next_link
        else:
            print("Link at position not found or out of bounds.")
            break
    
    print(f"Last name in sequence: {sequence_names[-1]}")

# Example usage
if __name__ == "__main__":
    start_url = input("Enter URL: ").strip()
    count = int(input("Enter count: ").strip())
    position = int(input("Enter position: ").strip())
    
    follow_links(start_url, count, position)