import requests

def get_daily_productivity_quote(text):
    response = requests.get("https://api.quotable.io/random?tags=productivity")
    if response.status_code == 200:
        data = response.json()
        quote = data["content"]
        author = data["author"]
        return f"{quote} - {author}"
    else:
        return "Failed to fetch daily productivity quote."

if __name__ == "__main__":
    productivity_quote = get_daily_productivity_quote()
    print(productivity_quote)
