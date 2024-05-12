import streamlit as st
import requests

# Function to fetch a random quote from an API
def fetch_quote():
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        return data["content"], data["author"]
    else:
        return "Couldn't fetch the quote", "Unknown"

# Streamlit app
def main():
    st.title("Random Quote Generator")
    st.subheader("Click the button below to get a random quote!")

    if st.button("Generate Quote"):
        quote, author = fetch_quote()
        st.write(f'"{quote}"')
        st.write(f"- {author}")

if __name__ == "__main__":
    main()
