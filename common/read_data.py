import yaml
from configparser import ConfigParser


class ReadFileData:
    def __init__(self):
        pass

    @staticmethod
    def load_yaml(file_path):
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        return data

    @staticmethod
    def load_ini(file_path):
        config = ConfigParser()
        config.read(file_path, encoding='utf-8')
        return config
