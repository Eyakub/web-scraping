from bs4 import BeautifulSoup
import requests


url = "http://example.com/"

# getting the webpage,creating a response object
response = requests.get(url)
print('Response -> ', response)

# extracting the source code of the page
data = response.text
print('Data -> ', data)

# passing the soruce code to beautiful soup to create a beautifulsoup object
soup = BeautifulSoup(data, 'html.parser')
print('Soup -> ', soup)

# extracting all the <a> tagss into a list
tags = soup.find_all('a')

# extracting URL from the attribute href in the tag <a>
for tag in tags:
    print('Href from inside <a> tag ->', tag.get('href'))