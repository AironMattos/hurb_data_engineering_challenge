from zipfile import ZipFile
import os

# Extract data from zip file
def unzip_data(path):
    with ZipFile(path) as zip:
        for zip_info in zip.infolist():
            if zip_info.filename[-1] == '/':
                continue
            zip_info.filename = os.path.basename(zip_info.filename)
            zip.extract(zip_info, 'data/raw/')
