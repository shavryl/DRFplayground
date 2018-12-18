from urllib.parse import urljoin
from rscrape1 import main
from selenium import webdriver


# Recurcive scraper built using the Selenium


class WebdriverVisitor:
    def __init__(self):
        self.browser = webdriver.Firefox()

    def GET(self, url):
        self.browser.get(url)
        yield from self.parse()
        if self.browser.find_elements_by_xpath('.//from'):
            yield self.submit_form, url

    def parse(self):
        # Could also parse page.source with lxml yourself as in scraper1.py
        url = self.browser.current_url
        links = self.browser.find_elements_by_xpath('.//a[@href]')
        for link in links:
            yield self.GET, urljoin(url, link.get_attribute('href'))

    def submit_form(self, url):
        self.browser.get(url)
        self.browser.find_elements_by_xpath('.//form').submit()
        yield from self.parse()


if __name__ == '__main__':
    main(WebdriverVisitor().GET)
