import csv
import os

from crawler.exporters.base_exporter import BaseExporter
from crawler.logger import setup_logger

logger = setup_logger(__name__)

OUTPUT_FOLDER = './data'


class TsvFileExporter(BaseExporter):
    def __init__(self, filename):
        self.filename = filename

    def export(self, data):
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        with open(os.path.join(OUTPUT_FOLDER, self.filename), 'w', newline='', encoding='utf-8') as tsv_file:
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            tsv_writer.writerow(['URL', 'Depth', 'Rank'])

            for url_item in data:
                tsv_writer.writerow([url_item.url, url_item.depth, url_item.rank])
