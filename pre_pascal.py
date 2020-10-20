# %%
import os
import re
import glob
import math

extension = 'xml'
dot_extension = '.xml'
jpg_extension = '.jpg'
tags = ['_binarize', '_blurring', '_corners',
        '_edges', '_contrast_gray', '_contrast',
        '_isolate', '_kernel', '_rmbk', '_shi_corner']


def insensitive_glob(pattern):
    def either(c):
        return '[%s%s]' % (c.lower(), c.upper()) if c.isalpha() else c
    return glob.glob(''.join(map(either, pattern)))


# %%
## %%timeit -n 1
for filename in insensitive_glob(os.path.join('data', '*', '*.{}').format(extension)):
    if '.DS_Store' in filename:
        continue
    with open(filename, "rt") as file:
        xmlData = file.read()
        for w in re.finditer(r"<filename>\w+.\w+</filename>", xmlData):
            name = str(w.group(0))[10:-15]
            before = xmlData[:w.start()+10]
            after = xmlData[w.end()-11:]
            for tag in tags:
                xmlData = before + name + tag + jpg_extension + after
                with open(filename[:-4]+tag+dot_extension, "wt") as file_w:
                    file_w.write(xmlData)


# %%
