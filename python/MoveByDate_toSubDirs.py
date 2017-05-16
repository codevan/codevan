import os, time, shutil, sys

# change this path
dir = 'C:/data/blockchains/ETH/geth/chaindata/'

os.chdir(dir)

# foreach file in listed directory, move to a new folder named after file date/HH
for f in os.listdir('.'):
    gtime = os.path.getmtime(f)#getmtime = modified time, getctime = createdtime
    ftime = time.gmtime(os.path.getmtime(f))
    ctime_dir = str(ftime.tm_year) +  str(ftime.tm_mon).rjust(2,'0') + str(ftime.tm_mday).rjust(2,'0') + '_' + str(ftime.tm_hour).rjust(2,'0')

    if not os.path.isdir(ctime_dir):
        print('making dir: ' +ctime_dir)
        os.mkdir(ctime_dir)
    dest = ctime_dir + '/' + f
    shutil.move(f, dest);
    
print('\ne.g.: File ' + dir + f + ' has been moved to ' + dest)
