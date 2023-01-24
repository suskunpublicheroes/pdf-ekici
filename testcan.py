import requests
from bs4 import BeautifulSoup

site = input("Lütfen taramak istediğiniz web sitesinin adresini girin: ")
response = requests.get(site)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, 'html.parser')
    pdf_tags = soup.find_all('a', href=lambda x: x and x.endswith('.pdf'))
    pdf_links = [link['href'] for link in pdf_tags]
    for link in pdf_links:
        print(link)
else:
    print("Web site geçersiz.")
