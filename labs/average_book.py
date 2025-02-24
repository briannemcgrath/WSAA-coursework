import requests
url = "https://andrewbeatty1.pythonanywhere.com/books"

def readbooks():
    response = requests.get(url)
    return response.json()

def average_book_price():
    books = readbooks()
    prices = [book['price'] for book in books if 'price' in book and isinstance(book['price'], (int,float))]
    return sum(prices) / len(prices) if prices else 0 

if __name__ == '__main__':
    avg_price = average_book_price()
    print("Average Book Price:", avg_price)