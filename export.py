import os
import shutil

filesToCreateX1 = []
filesToCreateX2 = []
filesToCopyX1 = []
filesToCopyX2 = []
dirsToCreate = []

newFolder = 'newOnes'
toCopy = 'tree_palm'

# get directories structure
for dir in os.listdir('./') :
    if os.path.isdir(dir) and newFolder not in dir :
        dirsToCreate.append(dir)

# create the directories structure fot the new files
if os.path.isdir(newFolder) :
    # delete then create to avoid override
    shutil.rmtree(newFolder)
    os.mkdir(newFolder)

    for dir in dirsToCreate :
        os.mkdir(newFolder+'/'+dir)
else :
    os.mkdir(newFolder)

    for dir in dirsToCreate :
        os.mkdir(newFolder+'/'+dir)

# create the arrays and setup the data
for r, d, f in os.walk('./'):
    for file in f:
        if 'dmg.png' in file :
            # do nothing
            pass
        elif 'd.png' in file:
            # do nothing
            pass
        elif '.slx' in file :
            pass
        elif '.py' in file:
            pass
        elif toCopy in file :
            if 'x1' in file :
                filesToCopyX1.append(os.path.join(r, file))
            else :
                filesToCopyX2.append(os.path.join(r, file))
        else:
            if 'x1' in file :
                filesToCreateX1.append(os.path.join(r, file))
            else :
                filesToCreateX2.append(os.path.join(r, file))



# copy x1 files
i = 0
for f in filesToCreateX1 :

    if i == len(filesToCopyX1) :
        i = 1
    else :
        # print(filesToCopyX1[i][:-4])
        # copy the file
        shutil.copy(filesToCopyX1[i], './'+newFolder+f[1:])
        i += 1

# copy x2 files
i = 0
for f in filesToCreateX2 :

    if i == len(filesToCopyX2) :
        i = 1
    else :
        shutil.copy(filesToCopyX2[i], './'+newFolder+f[1:])
        i += 1
