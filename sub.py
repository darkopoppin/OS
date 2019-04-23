import sys
import subprocess

with open (None, 'a+') as PIPE:
    subprocess.run(["python3", "test.py", "test1"], stdout = PIPE)
