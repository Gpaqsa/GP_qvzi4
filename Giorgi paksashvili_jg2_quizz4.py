import requests
from bs4 import BeautifulSoup
from time import sleep
from random import randint
import csv

file = open("FLASh.csv", "w", encoding="utf-8", newline='\n')
file.write("Title, price\n")

ind = 1
while ind <= 76:
    url = "https://alta.ge/usb-flash-drive-page-1" + str(ind) + ".html?"
    conn = requests.get(url)
    # print(conn.status_code)

    content = conn.text
    # print(content)

    soup = BeautifulSoup(content, "html.parser")

    all_flashMamoryBlock = soup.find('div', {'class': 'grid-list'})
    # print(all_flashMamoryBlock)
    all_flashmamory = all_flashMamoryBlock.find_all('div', class_="ty-column3")
    # print(all_flashmamory)

    for each in all_flashmamory:
        title = each.find("div", class_="ty-grid-list__item-name").text.strip()
        # print(title)
        price = each.find('span', class_="ty-price-num").text.strip()
        # print(price)
        print(title, price + "$")
    ind += 19
    file.write(title + ',' + price + '\n')
    sleep(randint(15, 20))
