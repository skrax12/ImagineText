import os

def read(filename):
    file = open(filename, 'r')
    #content = file.read()
    lines = file.readlines()

    return lines
    file.close()
    #print(content)

def readdir(dirName):
    fdirectory = dirName  # set directory path
    list = []
    for root, _, files in os.walk(fdirectory):
        for filename in files:
            list.append(os.path.join(root, filename))
    return list

readdir('englishtoclipart')