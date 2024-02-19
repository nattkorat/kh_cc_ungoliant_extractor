import os
import numpy as np

def split_cc(cc_index: str, num_per_file: int, dst: str):
    '''
        Splite index data to small chunks
        -----------------------
        - cc_index: org file paths
        - num_per_file: 
            <int>
            amount of index per file after spling
        - dst: destination to store the output
        
    '''
    with open(cc_index, 'r', encoding='utf-8') as wetpaths:
        data = np.array(wetpaths.readlines())
    
    sub_data = np.array_split(data, len(data)// num_per_file)
    for i in range(len(sub_data)):
        with open(f"{dst}/{i}-cc-wet.paths", 'w', encoding='utf-8') as f:
            f.write("".join(sub_data[i]))

    return True

if __name__ == '__main__':
    split_cc('cc-2023-50-wet.paths', 50, 'src/wet_paths')