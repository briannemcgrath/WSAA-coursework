import requests
url = "https://andrewbeatty1.pythonanywhere.com/books"
response = requests.get(url)

def readbooks():
    response = requests.get(url)
    return response.json()
if __name__ == "__main__":
    print(readbooks())

def readbook(id):
    geturl = url + '/' + str(id)
    response = requests.get(geturl)
    return response.json()

def createbook(book): 
    response = requests.post(url, json=book)
    return response.json()

def deletebook(id):
    deleteurl = url + '/' + str(id)
    response = requests.delete(deleteurl)
    return response.json()