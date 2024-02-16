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
    "--raw_dir",
    required= True,
    type = str,
    help = "Raw directory to store wet downloaded data (wet_data)"
)
parser.add_argument(
    "--dst",
    required = True,
    type = str,
    help = "Directory to store the out put result"
)

if __name__ == '__main__':
    args = parser.parse_args()

    path = args.path

    
    data = wet_paths.get_files(path)
    print(data)

