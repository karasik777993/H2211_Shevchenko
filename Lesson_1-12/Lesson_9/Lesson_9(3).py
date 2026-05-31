from bs4 import BeautifulSoup
import requests

resource = requests.get("https://coinmarketcap.com/")
if resource.status_code == 200:
    soup = BeautifulSoup(resource.text, features="html.parser")
    soup_list = soup.find_all("div",{"class": "sc-631098c-0 ilZTOW"})
    soup_list_1 = soup.find_all("div",{"class": "sc-c1554bc0-0 eWrlhi"})



#    for elem in soup_list:
#        print(elem)

    res = soup_list[0]. find("span")
    res_1 = soup_list_1[0].get_text()

    print(res.text)
    print(res_1)