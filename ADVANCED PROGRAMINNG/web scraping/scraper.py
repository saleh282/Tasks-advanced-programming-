import requests
from bs4 import BeautifulSoup
import pandas as pd

all_books = []

for page in range(1, 51):  
    url = f"http://books.toscrape.com/catalogue/page-{page}.html"
    soup = BeautifulSoup(requests.get(url).text, "html.parser")
    
    for book in soup.find_all("article", class_="product_pod"):
        all_books.append({
            "Title": book.h3.a["title"],            
            "Price": book.find("p", class_="price_color").text,  
            "Rating": book.p["class"][1]             
        })

pd.DataFrame(all_books).to_excel("books_50pages.xlsx", index=False)

print("All 50 pages saved to books_50pages.xlsx")
