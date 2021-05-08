import json

class Json(object):
    def __init__(self, file_path):
        self.file_path = file_path

        with open(file=file_path, mode='r') as json_file:
            self.json_data = json_file.read()

    def to_dict(self):
        return json.loads(self.json_data)
        