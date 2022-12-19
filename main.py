from config import BASE_LINK
from crawler import LinkCrawler


if __name__ == "__main__":

    c = LinkCrawler()
    print(c.start(BASE_LINK))


