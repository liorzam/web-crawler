class UrlItem:
    def __init__(self, url):
        self.url = url
        self._same_domain_counter = 0
        self._all_links_counter = 0

    def add(self, same_domain_count, all_links_count):
        self._same_domain_counter += same_domain_count
        self._all_links_counter += all_links_count

    @property
    def rank(self):
        return self._calculate_page_rank()
    
    def _calculate_page_rank(self):
        # Calculate the page rank based on the ratio of same-domain links
        return self._same_domain_counter / self._all_links_counter if self._all_links_counter > 0 else 0.0
    
    def __str__(self):
        return "URL: %s, Rank: %.4f" % (self.url, self.rank) 
