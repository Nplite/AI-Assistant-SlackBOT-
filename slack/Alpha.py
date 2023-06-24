import requests
def get_daily_motivation_quote(text):
    response = requests.get("https://api.quotable.io/random")
    if response.status_code == 200:
        data = response.json()
        quote = data["content"]
        author = data["author"]
        return f"{quote} - {author}"
    else:
        return "Failed to fetch daily motivation quote."
if __name__ == "__main__":
    motivation_quote = get_daily_motivation_quote()
    print(motivation_quote)

    


    