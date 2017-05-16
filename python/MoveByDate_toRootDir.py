import os, time, shutil, sys

# change this path
dir = 'C:/data/blockchains/ETH/geth/chaindata/'

os.chdir(dir)

# recurse directory tree and move all files into root directory, and delete subdirectories
for dirName, subdirList, fileList in os.walk('.'):
    
    if dirName == '.':
        continue
    print('Found directory: %s' % dirName)
    
    for f in fileList:

        shutil.move(dirName + '/' + f, '.')
        #print('\ne.g.: File ' + dir + f + ' has been moved to ' + dest)
    #print('e.g. \t%s moved to .' % f)
    print(dirName + ' contents has been moved to ' + dir)        
        
    shutil.rmtree(dirName) 
    print(dirName + ' deleted')

