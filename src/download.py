import os
import subprocess

class Download:
    def __init__(self, index: str, dst: str, task: int = 10) -> None:
        '''
        index: One cc wet.path
        dst: Where wet file is stored
        task: number of wet file it will download per time
        '''
        self.index = index
        self.dst = dst
        self.task = task
    
    def start_download(self):
        os.makedirs(self.dst, exist_ok=True)
        print(f"Downloading: {self.index}")
        process = subprocess.run(
          [f'ungoliant download -t {self.task} ./{self.index} ./{self.dst}'],
            shell=True, 
            capture_output=True, 
            text=True  
        )
        print(f"Download {self.index} completed")

        # move to completed dir
        completed_dir = self.index.split("/")
        
        dir = "/".join(completed_dir[:-1]) + "/completed/"
        os.makedirs(dir, exist_ok=True)
        os.rename(self.index, dir + + completed_dir[-1])

        return True
        

if __name__ == "__main__":
    index = "src/wet_paths/0.cc-2023-50-wet.paths"
    dst = "src/wet_data"

    download = Download(index, dst)
    download.start_download()