import requests
from bs4 import BeautifulSoup
from datetime import datetime

# Website URL
url = "https://www.bbc.com/news/technology"

# Send request to website
headers = {
    "User-Agent": "Mozilla/5.0"
}

try:
    response = requests.get(url, headers=headers, timeout=15)

    # Check if website is accessible
    response.raise_for_status()

    # Parse webpage
    soup = BeautifulSoup(response.text, "html.parser")

    # Extract headlines
    headlines = soup.select("h2")

    # Store headlines
    data = []

    for headline in headlines:
        text = headline.get_text(strip=True)

        if text:
            data.append(text)

    # Remove duplicates
    data = list(dict.fromkeys(data))

    # Display headlines
    print("\n===== TECH HEADLINES =====\n")

    for i, headline in enumerate(data, start=1):
        print(f"{i}. {headline}")

    # Save to file
    with open("headlines.txt", "w", encoding="utf-8") as file:
        file.write("TECH HEADLINES REPORT\n")
        file.write(f"Date: {datetime.now()}\n\n")

        for i, headline in enumerate(data, start=1):
            file.write(f"{i}. {headline}\n")

    print("\nHeadlines saved successfully to headlines.txt")

except requests.exceptions.RequestException as e:
    print("Error fetching webpage:", e)

except Exception as e:
    print("An error occurred:", e)