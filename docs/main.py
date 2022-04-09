import os
from subprocess import call
import pypandoc

path = "./"

for r, d, f in os.walk(path):
    for file in f:
        if file.endswith(".md"):
            filename = r + "/" + file
            newfilename = r + "/" + file[:-3] + ".rst"
            pypandoc.convert_file(filename, "rst", outputfile=newfilename)
