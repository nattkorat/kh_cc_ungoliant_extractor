import os
import subprocess


class Extract:
    def __init__(self, path_data: str, lang_model: str, dst: str, all_lang: bool = False):
        self.path_data = path_data
        self.lang_model = lang_model
        self.dst = dst
        self.all_lang = all_lang
    
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
        if self.all_lang:
            return True
        
        filename = self.path_data.split("/")[-1] + ".jsonl"
        os.rename(f"{self.dst}/km_meta.jsonl", f"src/extracted_data/{filename}")
        subprocess.run(
            [f'rm -rf {self.dst}']
        )

        return True 
        