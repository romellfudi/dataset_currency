import os
import re
import glob
import math
dir_ = "annots/"
width = 512
height = width
extension = 'xml'

def replacenth(string, sub, wanted, n):
    where = [m.start() for m in re.finditer(sub, string)][n-1]
    before = string[:where]
    after = string[where:]
    after = after.replace(sub, wanted, 1)
    return before + after
    
for filename in glob.glob('input_/*.{}'.format(extension)): 
    if filename == '.DS_Store':
        continue
    with open(filename, "rt") as file: 
        xmlData = file.read()
        for w in re.finditer(r"<width>\d+</width>",xmlData):
            widthImage = int(re.findall(r"<width>\d+</width>",w.group(0))[0][7:-8])
            before = xmlData[:w.start()+7]
            after = xmlData[w.end()-8:]
            xmlData = before + str(width) + after
        for w in re.finditer(r"<height>\d+</height>",xmlData):
            heightImage = int(re.findall(r"<height>\d+</height>",w.group(0))[0][8:-9])
            before = xmlData[:w.start()+8]
            after = xmlData[w.end()-9:]
            xmlData = before + str(height) + after
            
        itera = re.finditer("(<xmin>\d+</xmin>|<xmax>\d+</xmax>)",xmlData) 
        delay = 0
        for data in itera:
            val = int(re.findall(r"\d+",data.group(0))[0])
            newData = math.ceil(val * width / widthImage)
            before = xmlData[:data.start()+6-delay]
            after = xmlData[data.end()-7-delay:]
            delay = delay + len(str(val)) - len(str(newData))
            xmlData = before + str(newData) + after
            
        delay = 0
        itera = re.finditer("(<ymin>\d+</ymin>|<ymax>\d+</ymax>)",xmlData) 
        for data in itera:
            val = int(re.findall(r"\d+",data.group(0))[0])
            newData = math.ceil(val * height / heightImage)
            before = xmlData[:data.start()+6-delay]
            after = xmlData[data.end()-7-delay:]
            delay = delay + len(str(val)) - len(str(newData))
            xmlData = before + str(newData) + after
            
    with open(filename, "wt") as file: 
        file.write(xmlData)