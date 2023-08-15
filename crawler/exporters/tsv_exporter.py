import os
import csv

from crawler.exporters.base_exporter import BaseExporter
from crawler.exporters.consts import OUTPUT_FOLDER
from crawler.logger import setup_logger

logger = setup_logger(__name__)


class TsvFileExporter(BaseExporter):
    def export(self, data, filename='output.tsv', *args, **kwargs):
        os.makedirs(OUTPUT_FOLDER, exist_ok=True)

        with open(os.path.join(OUTPUT_FOLDER, filename), 'w', newline='', encoding='utf-8') as tsv_file:
            tsv_writer = csv.writer(tsv_file, delimiter='\t')
            tsv_writer.writerow(['URL', 'Depth', 'Rank'])

            for url_item in data:
                tsv_writer.writerow([url_item.url, url_item.depth, url_item.rank])
