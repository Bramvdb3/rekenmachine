import urllib.request
import urllib.parse
import json

def main():
    # Prompt for a location
    location = input("Enter location: ")
    
    # Construct the URL with properly encoded parameters
    base_url = 'http://py4e-data.dr-chuck.net/opengeo?'
    url = base_url + urllib.parse.urlencode({'q': location})
    
    try:
        # Attempt to fetch JSON data from the URL
        print(f"Retrieving {url}")
        response = urllib.request.urlopen(url)
        data = response.read().decode()
        
        # Parse JSON data
        json_data = json.loads(data)
        
        # Check if there are results and extract the first plus_code
        if 'results' in json_data and json_data['results']:
            first_result = json_data['results'][0]
            if 'plus_code' in first_result:
                plus_code = first_result['plus_code']
                print(f"Retrieved {len(data)} characters")
                print(f"Plus code: {plus_code}")
            else:
                print("No 'plus_code' found in the results.")
        else:
            # If no results found for the full location, split the location into parts and retry
            parts = location.split(' and ')
            for part in parts:
                url = base_url + urllib.parse.urlencode({'q': part})
                print(f"Retrieving {url}")
                response = urllib.request.urlopen(url)
                data = response.read().decode()
                json_data = json.loads(data)
                
                if 'results' in json_data and json_data['results']:
                    first_result = json_data['results'][0]
                    if 'plus_code' in first_result:
                        plus_code = first_result['plus_code']
                        print(f"Retrieved {len(data)} characters")
                        print(f"Plus code: {plus_code}")
                        return  # Exit function if successful
                    else:
                        print("No 'plus_code' found in the results.")
                        return
                else:
                    print(f"No results found for '{part}'")
                    print("Full JSON response:")
                    print(data)
            
            print("No results found for any part of the location.")
            
    except Exception as e:
        print(f"Error fetching or parsing data: {e}")

if __name__ == "__main__":
    main()