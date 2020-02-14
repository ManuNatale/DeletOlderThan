import os
import time
import stat
import shutil
from pathlib import Path
from datetime import datetime

def oldDateCheck(path, folder, testTrueFalse, olderThan):
    
    now = time.time()
    #print('heure actu ' + str(now))

    fileStatsObj = os.stat(path)
    #print(str(fileStatsObj))
    creationTime = time.ctime ( fileStatsObj [ stat.ST_CTIME ] )
    creationTimeSec =  ( fileStatsObj [ stat.ST_CTIME ] )
    print(creationTime + ', sec : ' + str(creationTimeSec))
    diff = now - creationTimeSec
    print('diff : ' + str(diff))
    if(diff > olderThan): 
        if(testTrueFalse == False):
            print('Old folder finded. Removing ==> {}\n'.format(folder))
            try:
                shutil.rmtree(path, ignore_errors=True)
            except:
                print('[{}] : Error removing folder : {} !!!'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), folder))
            return True
        else:
            print('Old folder finded ==> {}\nThis is a test, any folder has been removed.'.format(folder))
            return True
    else:
        return False
    
    
def FolderCleaning(path, olderThan, testTrueFalse):
    print('[{}] : Cleaning session started ! Checking folders older than : {} day...\n\n'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), (olderThan/60/60)/24))
    time.sleep(3)
    if(testTrueFalse == True):
        print('[{}] : Test session any folders are gonna be removed'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
    delet_count = 0
    folders = os.listdir(path=path)
    Nb_Of_folders = len(folders)
    #print(folders)
    #print(Nb_Of_folders)

    for i in folders:
        time.sleep(0.2)
        print('\n\nChecking floder : ' + i)
        folder_path = ('{}/{}'.format(path, i))
        print('Path = {}'.format(folder_path))
        if(oldDateCheck(folder_path, i, testTrueFalse, olderThan) == True):
            delet_count += 1
    print('\n[{}] : Number of folders find : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), Nb_Of_folders))
    print('\n[{}] : Number of folders older than {} days : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), (olderThan/60/60)/24, delet_count))
    if(testTrueFalse == True):
        print('\n[{}] : ||Test = True|| number of folders to delet : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), delet_count))
    else:
        print('\n[{}] : Number of deleted folders : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), delet_count))
    
path = Path("./images/")
olderThan = 864000
FolderCleaning(path, olderThan, True) # args = path, remove_folders_older_than (INT, in seconds), Test (True or False)
