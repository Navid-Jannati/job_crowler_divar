import requests
from bs4 import BeautifulSoup


class LinkCrawler:
    def __init__(self):
        pass

    def get_page(self, url):
        """
        here we use from (requests) for get target page with url
        :param url: Target page url for crawl
        :return: output is a response for request to url
        """

        try:
            response = requests.get(url)
        except requests.HTTPError:
            return None
        return response

    def find_links(self, html_doc):
        """
        here we use from (bs4) for able work with html_doc (response) from get_page
        :param html_doc: This is the same response we received from the get_page method
        :return:output is a list of links
        """
        adv_links = list()
        soup = BeautifulSoup(html_doc, 'html.parser')
        return soup.find_all('a', attrs={'class': 'hdrlnk'},)

    def store(self, links):
        for li in links:


    def start(self, url):
        page_number = 0
        crawl = True
        links = list()
        while crawl:
            response = self.get_page(url + str(page_number))
            if response is None:
                crawl = False
                continue
            new_links = self.find_links(response.text)
            links.extend(new_links)
            page_number += 120
            crawl = bool(len(new_links))
        return links

