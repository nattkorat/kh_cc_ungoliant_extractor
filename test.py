import subprocess
import os
from src.utils import wet_paths

data = wet_paths.get_files("src/wet_paths")

half = len(data) // 2

natt = data[:half]
panha = data[half:]

print(len(natt), len(panha))

for n in natt:
    subprocess.run(["mv", f"{n}",  f"src/wet_paths/natt/{n.split('/')[-1]}"])

for p in panha:
    subprocess.run(["mv", f"{p}", f"src/wet_paths/panha/{p.split('/')[-1]}"])