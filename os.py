import os
import subprocess

#os.chdir("..")

result = subprocess.check_output('dir /S /B *.txt',shell=True).decode(errors="replace").split()

for i in result:
    os.remove(i)
