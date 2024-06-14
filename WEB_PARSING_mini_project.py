import requests
from bs4 import BeautifulSoup
import csv
import time
from random import randint

file = open("item.csv", "w", encoding="utf-8_sig",newline="\n")
write_obj = csv.writer(file)
write_obj.writerow(["Name", "Catrgory", "Price", "Link"])


page = 1
while page <=5:
    url = f"https://www.shop.ge/online-shop/index{page}.html"
    response = requests.get(url)
    # print(response)

    html = response.text
    # print(html)
    soup = BeautifulSoup(html, "html.parser")
    item_section = soup.find("section", class_="list row")
    all_items = item_section.find_all("article")

    for item in all_items:
        img_add = item.img.attrs.get("src")
        info = item.find("div", class_="main-column clearfix")
        name = info.li.a.text.strip()
        category = info.ul.span.text
        price_find = item.find("li",class_= "system")
        price = price_find.span.text.strip()
        write_obj.writerow([name, category ,price, img_add])

    page += 1
    time.sleep(randint(15,20))