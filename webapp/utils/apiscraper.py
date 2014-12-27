
import requests
import urllib

from django.conf import settings


SCRAPER_ENDPOINT = getattr(settings, 'SCRAPER_ENDPOINT', 'http://localhost:8000/api/scrape/')


ERROR_BAD_REQUEST = 422
class ScrapeAppException(Exception):
    pass

class APIScraper(object):

    def handle_response(self, response):
        if response.status_code == 200:
            data = response.json()
            if 'error' in data:
                try:
                    raise ScrapeAppException(data['error'])
                except AttributeError as e:
                    error_code = data['error']['code']
                    if error_code == ERROR_BAD_REQUEST:
                        raise ScrapeAppException("APIScraper::scrape_url: [%s] %s" % (error_code, data['error']['reason']))
                    else:
                        raise ScrapeAppException("APIScraper::scrape_url: [%s] %s" % (error_code, ERROR_CODES.get(error_code, "Unknown exception")))
            return data
        else:
            raise ScrapeAppException("APIScraper::scrape_url: SCRAPER_ENDPOINT=%r -> requests.response.status_code = %r" % (SCRAPER_ENDPOINT, response.status_code))


    def scrape_url(self, url):
        qs = {'url': urllib.unquote(url)}
        response = requests.get(SCRAPER_ENDPOINT, params=qs)
        return self.handle_response(response)

    def scrape_urls(self, urls):
        qs = {'urls': ','.join([urllib.unquote(url) for url in urls])}
        response = requests.get(SCRAPER_ENDPOINT, params=qs)
        return self.handle_response(response)