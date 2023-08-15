import csv
from crawler.exporters.base_exporter import BaseExporter
from crawler.logger import setup_logger

logger = setup_logger(__name__)

class TsvFileExporter(BaseExporter):
    def __init__(self, filename):
        self.filename = filename

    def export(self, data):
        with open(self.filename, 'w', newline='', encoding='utf-8') as tsv_file:
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            tsv_writer.writerow(['URL', 'Depth', 'Rank'])

            for url_item in data:
                tsv_writer.writerow([url_item.url, url_item.depth, url_item.rank])