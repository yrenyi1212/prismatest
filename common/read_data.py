import yaml
from configparser import ConfigParser


class ReadFileData:
    def __init__(self):
        pass

    def load_yaml(self, file_path):
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    def load_ini(self, file_path):
        config = ConfigParser()
        config.read(file_path, encoding='utf-8')
        # data = config.sections()
        return config


data = ReadFileData()
