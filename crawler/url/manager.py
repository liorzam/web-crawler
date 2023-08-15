
import csv
from crawler.exporters.consts import ExporterType
from crawler.exporters.factory import ExporterFactory
from crawler.url.item import UrlItem


class UrlManager:
    def __init__(self, export_type=ExporterType.TSV):
        # Dictionary to hold UrlItem instances
        self.urls = {}
        self._export_type = export_type

    def get_urls_sorted_by_rank(self):
        return sorted(self.urls.values(), key=lambda log: log.rank, reverse=True)
    
    def add(self, url, same_domain_links, all_links, depth):
        log = self.urls.get(url, None)

        if not log:
            log = UrlItem(url, depth)
            self.urls[url] = log

        log.add(same_domain_count=len(same_domain_links),
                all_links_count=len(all_links))
        
    def export(self, exporter_type: ExporterType = None, *args, **kwargs):
        exporter = ExporterFactory.create_exporter(exporter_type or self._export_type, *args, **kwargs)
        exporter.export(self.get_urls_sorted_by_rank())
