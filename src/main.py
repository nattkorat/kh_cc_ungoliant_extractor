import os
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

parser.add_argument(
    "--dst",
    required = True,
    type = str,
    help = "Directory to store the output result"
)

WET_DATA_DIR = "src/wet_data/"
LANG_MODEL = "lid.176.bin"

def run(path_indexes, dst):
    for indexes in path_indexes:
        # 1. download
        download = Download(indexes, WET_DATA_DIR)
        wet_data_path = download.start_download()
        
        # 2. extract (get the dst from download)
        # extract = Extract(wet_data_path, LANG_MODEL, dst)

if __name__ == '__main__':
    args = parser.parse_args()
    path = args.path
    dst = args.dst
    path_indexes = wet_paths.get_files(path)

    run(path_indexes, dst)
    
    


