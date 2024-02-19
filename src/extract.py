import os
import subprocess


class Extract:
    '''
    path_data: directory of wet compress data
    lang_model: model path
    dst: extracted directory

    
    '''
    def __init__(self, path_data: str, lang_model: str, dst: str, cc_path: str):
        self.path_data = path_data
        self.lang_model = lang_model
        self.dst = dst
        self.cc_path = cc_path
    
    def start_extract(self):
        extract = subprocess.run(
            # ungoliant pipeline [OPTIONS] <src> <dst>
            [f'ungoliant pipeline --lid-path {self.lang_model} {self.path_data} ./temp'],
            shell=True,
            capture_output=True, 
            text=True
        )
        if extract.returncode != 0:
            return False
        
        subprocess.run(
            [f'rm', '-rf', self.path_data]
        )

        filename = self.cc_path.split("/")[-1] + ".jsonl"
        os.rename(f"temp/km_meta.jsonl", f"{self.dst}/{filename}")
        subprocess.run(
            [f'rm', '-rf', 'temp']
        )

        return True 

if __name__ == '__main__':
    pass