
class BaseExporter:
    def export(self, data):
        raise NotImplementedError("Subclasses must implement this method")
