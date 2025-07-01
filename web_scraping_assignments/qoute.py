import requests
from bs4 import BeautifulSoup
from collections import Counter


url = "http://quotes.toscrape.com/"

try:
    res = requests.get(url)
except requests.RequestException as e:
    print(f"Somthing went wrong: {e}")
else:
    if res.status_code == 200:
        soup = BeautifulSoup(res.content, "html.parser")
        quotes = [quote.text for quote in soup.select("span.text")]
        authors = [author.text for author in soup.select("div.quote small.author")]
        tags = [tag.text for tag in soup.select("div.quote a.tag")]
        
        print(f"1. Total number of quote: {len(quotes)}")
        print(f"2. The number of unique authors: {len(set(authors))}")
        
        author_with_most_qoute = ""
        occure = 1
        for author, occurance in dict(Counter(authors)).items():
            if occurance > occure:
                occure = occurance
                author_with_most_qoute = author
        
        print(f"3. The author with the most quotes: {author_with_most_qoute}")
        
        Count_quotes_is = 0
        for qoute in quotes:
            if "is" in qoute.lower():
                Count_quotes_is += 1
                
        print(f"4.Number of quotes contain the word 'is': {Count_quotes_is}")
        print("5.")
        for tag, occurance in dict(Counter(tags)).items():
            print(f"'{tag}' appear '{occurance}' times")
    else:
        print(f"Error code: {res.status_code}")
        