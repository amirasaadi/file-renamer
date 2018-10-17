import os

for filename in os.listdir("."):
    if filename.endswith("ttf"):
        os.rename(filename, filename.replace('_p30download.com',''))
