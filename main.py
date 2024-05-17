import requests

# Function to fetch data from API
def fetch_data(api_url):
    response = requests.get(api_url)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# Function to identify citations for each response
def identify_citations(data):
    citations = []
    for item in data:
        response_text = item['Response']
        sources = item['Source']
        for source in sources:
            if source['context'] in response_text:
                citations.append({"id": source['id'], "link": source.get('link', '')})
                break
    return citations

# Main function to process data
def main():
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data(api_url)

    if data:
        print("Fetched data from API successfully!")
        
        citations = identify_citations(data)

        if citations:
            print("\nCitations:")
            for citation in citations:
                print("ID:", citation['id'])
                print("Link:", citation['link'])
        else:
            print("No citations found.")

    else:
        print("Failed to fetch data from API. Please try again later.")

if __name__ == "__main__":
    main()
