from crawler.exporters.base_exporter import BaseExporter
from crawler.logger import setup_logger

logger = setup_logger(__name__)


class ConsoleExporter(BaseExporter):
    def export(self, data):
        if data:
            logger.info(f"Highest Ranked {data[0]}")

            for url in data[1:]:
                logger.info(url)
