from bs4 import BeautifulSoup
import requests

def get_business_list():
    url = "http://realbusinessmen.com/page/%s"

    page = 1

    while True:

        response = requests.get(url % page)
        if not response.ok:
            break

        soup = BeautifulSoup(response.text)
        articles = soup.find_all("article")
        images = [article.img.get("src")
                for article in articles
                if article.img is not None]

        with open("business.txt", "a") as business:
            [business.write(image + "\n") for image in images]

        next_page = soup.find(id="pageNavOlder")

        if next_page is None:
            break
        else:
            page += 1

def get_business():

    with open("business.txt", "r") as business:
        urls = [url[:-1] for url in business]

    number_of_business = 1

    for url in urls:
        response = requests.get(url, stream=True)
        if response.ok:
            with open("business/business%d.jpg"%number_of_business, "wb") as image:
                [image.write(chunk) for chunk in response.iter_content()]
                number_of_business += 1
                print(number_of_business)


if __name__ == '__main__':
    #get_business_list()
    get_business()
