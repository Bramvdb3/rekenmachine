import urllib.request
import json

def main():
    url = input("Enter URL: ").strip()
    print(f"Retrieving JSON data from: {url}")
    
    # Fetch JSON data from the URL
    try:
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        
        # Parse JSON
        json_data = json.loads(data)
        
        # Extract comment counts
        comment_counts = [int(item['count']) for item in json_data['comments']]
        
        # Compute sum of comment counts
        total_comments = sum(comment_counts)
        
        print(f"Sum of comment counts: {total_comments}")
        
    except Exception as e:
        print(f"Error fetching or parsing data: {e}")

if __name__ == "__main__":
    main()