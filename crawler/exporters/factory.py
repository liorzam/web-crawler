from crawler.exporters.console_exporter import ConsoleExporter
from crawler.exporters.consts import ExporterType
from crawler.exporters.tsv_exporter import TsvFileExporter


class ExporterFactory:
    EXPORTER_MAP = {
        ExporterType.CONSOLE: ConsoleExporter,
        ExporterType.TSV: TsvFileExporter,
    }
        
    @classmethod
    def create_exporter(cls, exporter_type: ExporterType, *args, **kwargs):
        exporter_class = cls.EXPORTER_MAP.get(exporter_type)
        if exporter_class:
            return exporter_class(*args, **kwargs)
        else:
            raise ValueError("Invalid exporter type")