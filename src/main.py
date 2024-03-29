import os
import time
import datetime
import argparse
from download import Download
from extract import Extract
from utils import wet_paths

parser  = argparse.ArgumentParser()
parser.add_argument(
    "--path",
    required = True,
    type = str,
    help = "Directory storing the wet path indexes"
)

# parser.add_argument(
#     "--dst",
#     required = True,
#     type = str,
#     help = "Directory to store the output result"
# )

WET_DATA_DIR = "src/wet_data/"
LANG_MODEL = "lid.176.bin"
EXTRACTED_DIR = "src/extracted_data"

def run(path_indexes):
    ''' Run pipeline.

    Parameters
    ----------
    path_indexs: str
        Directory of wet index file.
    det: 

    Attributes
    ----------
    cc_path: list
        list of cc index path, read from directory.
    cc_path: str
        Name of cc path file in list 

    '''
    cc_paths = wet_paths.get_files(path_indexes)
    for cc_path in cc_paths:
        # 1. download
        ts_download = time.time()
        print(f"Indexes: {cc_path}")
        print(f"Download start at: {datetime.datetime.now()}")

        download = Download(cc_path, WET_DATA_DIR)
        is_downloaded = download.start_download()
        
        # 2. extract (get the dst from download)
        if not is_downloaded:
            print(f"Failed download:", cc_path)
            continue
        print(f"Download finish at {datetime.datetime.now()}")
        print(f"Download completed for {(time.time() - ts_download):.2f} sec.")
        
        ts_extract = time.time()
        print("Start extracting...")
        extract = Extract(WET_DATA_DIR, LANG_MODEL, EXTRACTED_DIR, cc_path)
        extract.start_extract()
        print(f"Extract completed for {(time.time() - ts_extract):.2f} sec")
        print("Done!")


if __name__ == '__main__':
    args = parser.parse_args()
    path = args.path

    run(path)
    