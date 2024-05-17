import requests
import streamlit as st

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

# Main function to display UI and process data
def main():
    st.title("Citations from API Responses")

    # Fetch data from API
    api_url = "https://devapi.beyondchats.com/api/get_message_with_sources"
    data = fetch_data(api_url)

    if data:
        st.write("Fetched data from API successfully!")
        
        # Identify citations for each response
        citations = identify_citations(data)

        if citations:
            st.subheader("Citations:")
            for citation in citations:
                st.write("ID:", citation['id'])
                st.write("Link:", citation['link'])
        else:
            st.write("No citations found.")

    else:
        st.write("Failed to fetch data from API. Please try again later.")

if __name__ == "__main__":
    main()
