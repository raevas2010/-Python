import os.path

class FileReader:

    def __init__(self, file_path):
        self.file_path = file_path

    def read(self):
        try:
            if not os.path.exists(self.file_path):
                raise ValueError("")
            with open(self.file_path) as f:
                content = f.read()
        except ValueError as err:
            content = err.args[0]
        finally:
            return content