import os
import logging

from zipfile import ZipFile
from datetime import datetime


class FileExtraction:
    def __init__(self, landing_path, raw_path):
        self._landing_path = landing_path
        self._raw_path = raw_path

        self.date_now = datetime.now().strftime("%m%d%Y")

    @property
    def landing_path(self):
        return self._landing_path

    @landing_path.setter
    def landing_path(self, path):
        self._landing_path = self.validate_directory(path)

    @property
    def raw_path(self):
        return self._raw_path

    @raw_path.setter
    def raw_path(self, path):
        self._raw_path = self.validate_directory(path)

    @staticmethod
    def validate_directory(path):
        if os.path.isdir(path):
            return path
        else:
            logging.error("Please use a valid file path.")

    def load_compressed_file(self):
        files = [file for file in os.listdir(self._landing_path)
                 if os.path.isfile(os.path.join(self._landing_path, file))]

        for file in files:
            with ZipFile(os.path.join(self._landing_path, file)) as zip_file:
                for zip_ in zip_file.namelist():
                    origin_name = f"{self._raw_path}{zip_}"
                    destine_name = f"{self._raw_path}{self.date_now}_{zip_}"

                    if zip_.endswith('.json') and "__MACOSX" not in zip_:
                        zip_file.extract(zip_, self._raw_path)
                        os.replace(origin_name, destine_name)



