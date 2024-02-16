import os
import subprocess

class Download:
    def __init__(self, index: str, dst: str, task: int = 10) -> None:
        self.index = index
        self.dst = dst
        self.task = task
    
    def start_download(self):
        process = subprocess.run(
          [f'ungoliant download -t {self.task} ./{self.index} {self.dst}/{self.index.split("/")[-1]}'],
            shell=True, 
            capture_output=True, 
            text=True  
        )
        return process.returncode
    
    def mark(self, dst: str):
        try:
            os.rename(self.path, dst)
            return True
        except FileExistsError as e:
            print(e)
            return False
