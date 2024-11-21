import requests
import json

# Define the base URL for the API
BASE_URL = "https://data.brreg.no"

def download_organization_data():
    # Endpoint for downloading all organization data in JSON format
    endpoint = "/enhetsregisteret/api/enheter/lastned"
    url = f"{BASE_URL}{endpoint}"

    try:
        # Make the GET request to the API
        response = requests.get(url, headers={"Accept": "application/vnd.brreg.enhetsregisteret.enhet.v2+json"})
        response.raise_for_status()  # Raise an error for bad responses
        
        # Save the downloaded data to a local file
        with open("organization_data.json", "w", encoding='utf-8') as file:
            json.dump(response.json(), file, indent=4, ensure_ascii=False)
        
        print("Organization data downloaded successfully!")
    
    except requests.exceptions.RequestException as e:
        print(f"Error downloading data: {e}")

if __name__ == "__main__":
    download_organization_data()
