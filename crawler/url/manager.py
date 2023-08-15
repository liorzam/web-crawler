

import logging
from crawler.exporters.consts import ExporterType
from crawler.exporters.factory import ExporterFactory
from crawler.logger import setup_logger
from crawler.url.item import UrlItem

logger = setup_logger(__name__)


class UrlManager:
    def __init__(self, export_type=ExporterType.TSV):
        # Dictionary to hold UrlItem instances
        self.urls = {}
        self.export_types = [export_type]

        if logger.isEnabledFor(logging.DEBUG):
            self.export_types.append(ExporterType.CONSOLE)

        self.exporters = [ExporterFactory.create_exporter(export_type) for export_type in self.export_types]

    def get_urls_sorted_by_rank(self):
        return sorted(self.urls.values(), key=lambda log: log.rank, reverse=True)

    def add(self, url, same_domain_links, all_links, depth):
        log = self.urls.get(url, None)

        if not log:
            log = UrlItem(url, depth)
            self.urls[url] = log

        log.add(same_domain_count=len(same_domain_links),
                all_links_count=len(all_links))

    def export(self):
        sorted_urls = self.get_urls_sorted_by_rank()

        for exporter in self.exporters:
            exporter.export(sorted_urls)
