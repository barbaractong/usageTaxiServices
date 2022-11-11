import os
import logging

from zipfile import ZipFile
from datetime import datetime


class FileExtraction:
    def __init__(self, origin_path):
        self._origin_path = origin_path

    @property
    def origin_path(self):
        return self._origin_path

    @origin_path.setter
    def origin_path(self, path):
        if os.path.isdir(path):
            self._origin_path = path
        else:
            self._origin_path = None
            logging.error("Please use a valid file path.")

    def load_compressed_file(self):
        files = [file for file in os.listdir(self._origin_path)
                 if os.path.isfile(os.path.join(self._origin_path, file))]

        for file in files:
            with ZipFile(os.path.join(self._origin_path, file)) as zip_file:
                for zip_ in zip_file.namelist():
                    if zip_.endswith('.json') and "__MACOSX" not in zip_:
                        date_now = datetime.now().strftime("%m%d%Y")
                        zip_file.extract(zip_, '../data/raw_file')

                        os.rename(f"../data/raw_file/{zip_}", f"../data/raw_file/{date_now}_{zip_}")

