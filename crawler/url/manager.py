
from crawler.url.item import UrlItem


class UrlManager:
    def __init__(self):
        self._url_items = {}  # Dictionary to hold UrlItem instances

    def add(self, url, same_domain_links, all_links):
        log = self._url_items.get(url, None)

        if not log:
            log = UrlItem(url)
            self._url_items[url] = log

        log.add(same_domain_count=len(same_domain_links),
                all_links_count=len(all_links))
        
    def get_urls_sorted_by_rank(self):
        return sorted(self._url_items.values(), key=lambda log: log.rank, reverse=True)