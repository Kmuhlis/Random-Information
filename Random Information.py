import requests
from bs4 import BeautifulSoup
import webbrowser

# Wikipedia special random özelliğini kullanarak rastgele aldığımız konu başlıklarını kullanıcıya sorarak açmamızı sağlayan bir proje.

while True:
    url = requests.get("https://en.wikipedia.org/wiki/Special:Random")
    # 1 - Önce requests get metodu ile wikipedia ya istek atıyoruz.
    soup = BeautifulSoup(url.content, "html.parser")
    # 2 - BeutifulSoup ile html kodlarını alıyoruz.
    title = soup.find(class_="firstHeading").text
    # 3 - Find metodu ile makale başlığını buluyoruz.
    print(f"{title} \nBu konuyla ilgilenmek istiyormusunuz? (E/H)")
    ans = input("").lower()
    if ans == "e":
        url = "https://en.wikipedia.org/wiki/%s" % title
        webbrowser.open(url)
        break
    elif ans == "h":
        print("Farklı bir konu aranıyor!")
        continue
    else:
        print("Doğru bir karakter girdiğinizden emin olun.!")
        break