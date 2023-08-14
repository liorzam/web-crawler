import itertools
from urllib.parse import urldefrag, urljoin, urlparse

import requests
from bs4 import BeautifulSoup
from requests.adapters import HTTPAdapter
from urllib3 import Retry

from crawler.logger import measure_time, setup_logger
from crawler.url.manager import UrlManager

logger = setup_logger(__name__)

class WebCrawler:
    def __init__(self, root_url, depth_limit, page_link_limit):
        self._init_request_adapter()
        logger.debug(f"Scraping page: {root_url}, depth: {depth_limit}")
        if not root_url:
             raise ValueError("The root_url cannot be None.")
        
        self._root_url = root_url
        self._depth_limit = depth_limit
        self._page_link_limit = page_link_limit
        self._visited_urls = set()
        self._manager = UrlManager()

    @measure_time(logger)
    def fetch_page(self, url):
        try:
            logger.debug(f"fetching {url}")

            # TODO export timeout to config using env var
            response = self._session.get(url, timeout=10)
            response.raise_for_status()
            
            return response.content
        except requests.exceptions.RequestException as e:
            logger.error(f"Error fetching {url}: {e}")
            return None
        
    def start_crawling(self):
        logger.info(f"Starting web crawling from: {self._root_url} with depth: {self._depth_limit}")

        # Initialize the crawling process
        self._crawl(self._root_url, 1)

        sorted_urls_by_rank = self._manager.get_urls_sorted_by_rank()

        if sorted_urls_by_rank:
            logger.info(f"Highest Ranked {sorted_urls_by_rank[0]}")

        for url in sorted_urls_by_rank[1:5]:
                    logger.info(f"Ranked {url}")


    def _crawl(self, url, depth):
        if depth > self._depth_limit or url in self._visited_urls:
            return

        try:
            content = self.fetch_page(url)
            if content is None:
                return

            self._visited_urls.add(url)
            
            url_links = self._explore_urls_to_visit_v2(content, url)

            limited_links = list(itertools.islice(url_links, self._page_link_limit))

            if limited_links:
                logger.debug("Discover new URLs to crawl: %s", limited_links)

            same_domain_links = [link for link in limited_links if urlparse(link).netloc == urlparse(url).netloc]
            
            # Calculate page rank based on same_domain_links
            self._manager.add(url, same_domain_links, url_links)

            for link in same_domain_links:
                self._crawl(link, depth + 1)

        except Exception as e:
            logger.error(f"Error while crawling a page: {url}", e)
        
    def _init_request_adapter(self):
        self._retries = Retry(total=3, backoff_factor=0.5, status_forcelist=[500, 502, 503, 504])
        self._session = requests.Session()
        self._adapter = HTTPAdapter(max_retries=self._retries)
        self._session.mount('http://', self._adapter)
        self._session.mount('https://', self._adapter)
        
    
    def _explore_urls_to_visit_v1(self, content, base_url):
        # Use BeautifulSoup to parse the HTML content and extract links
        #TODO: can be improved by contextmanager and generator
        soup = BeautifulSoup(content, 'html.parser')

        return set(urldefrag(urljoin(base_url, link.get('href'))).url for link in soup.find_all('a') if link.get('href') and urljoin(base_url, link.get('href')))
    
    def _explore_urls_to_visit_v2(self, content, base_url):
        urls_to_visit = set()
        
        soup = BeautifulSoup(content, 'html.parser')

        for link in soup.find_all('a'):
            href = link.get('href')
            if href and urljoin(base_url, href):
                parsed_url = urlparse(urljoin(base_url, href))
                sanitized_url = f"{parsed_url.scheme}://{parsed_url.netloc}{parsed_url.path}"

                if not sanitized_url:
                    logger.warn("Non compatible link: {base_url}")
                    continue

                if sanitized_url not in self._visited_urls and \
                    sanitized_url not in urls_to_visit:
                    urls_to_visit.add(sanitized_url)

        return urls_to_visit