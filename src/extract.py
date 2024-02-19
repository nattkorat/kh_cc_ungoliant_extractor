import os
import subprocess


class Extract:
    '''
    path_data: directory of wet compress data
    lang_model: model path
    dst: extracted directory
    is_all_lang: Store all languages, default = False
    
    '''
    def __init__(self, path_data: str, lang_model: str, dst: str, is_all_lang: bool = False):
        self.path_data = path_data
        self.lang_model = lang_model
        self.dst = dst
        self.is_all_lang = is_all_lang
    
    def start_extract(self):
        extract = subprocess.run(
            # ungoliant pipeline [OPTIONS] <src> <dst>
            [f'ungoliant pipeline --lid-path {self.lang_model} {self.path_data} ./{self.dst}'],
            shell=True,
            capture_output=True, 
            text=True
        )
        if extract.returncode != 0:
            return False
        subprocess.run(
            [f'rm -rf {self.path_data}']
        )
        if self.is_all_langall_lang:
            return True
        
        filename = self.path_data.split("/")[-1] + ".jsonl"
        os.rename(f"{self.dst}/km_meta.jsonl", f"src/extracted_data/{filename}")
        subprocess.run(
            [f'rm -rf {self.dst}']
        )

        return True 
        