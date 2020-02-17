import os
import time
import stat
import shutil
import argparse
from datetime import datetime


    
# Main function  
def FolderCleaning(path, daysToSec, testTrueFalse): # Use DeletOlderThanImport.FolderCleaning(path, daysToSec, test) # args = path, remove_folders_older_than (INT, in days), Test (True or False)

    def oldDateCheck(path, folder, testTrueFalse, olderThan):
    
        now = time.time()
        #print('heure actu ' + str(now))

        fileStatsObj = os.stat(path)
        #print(str(fileStatsObj))
        creationTime = time.ctime ( fileStatsObj [ stat.ST_CTIME ] )
        creationTimeSec =  ( fileStatsObj [ stat.ST_CTIME ] )
        print('Modification date :' + creationTime + ', sec Unix : ' + str(creationTimeSec))
        diff = now - creationTimeSec
        print('Time difference beetweem now and modification date : ' + str(round(diff)))
        if(diff > olderThan): 
            if(testTrueFalse == False):
                print('Old folder finded. Removing ==> {}\n'.format(folder))
                try:
                    pass
                    #shutil.rmtree(path, ignore_errors=True)
                except:
                    print('[{}] : Error removing folder : {} !!!'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), folder))
                return True
            else:
                print('Old folder finded ==> {}\nThis is a test, any folder has been removed.'.format(folder))
                return True
        else:
            return False

    olderThan = ((daysToSec*60)*60)*24

    print('\n[{}] : Cleaning session started ! Checking folders older than : {} day...'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), round(daysToSec, 2)))
    time.sleep(3)
    if(testTrueFalse == True):
        print('\n[{}] : Test session any folders are going to be removed'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S')))
        time.sleep(5)
    delet_count = 0
    folders = os.listdir(path=path)
    Nb_Of_folders = len(folders)
    #print(folders)
    #print(Nb_Of_folders)

    for i in folders:
        time.sleep(0.01)
        print('\n\nChecking floder : ' + i)
        folder_path = ('{}/{}'.format(path, i))
        print('Path = {}'.format(folder_path))
        if(oldDateCheck(folder_path, i, testTrueFalse, olderThan) == True):
            delet_count += 1
    print('\n[{}] : Number of folders find : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), Nb_Of_folders))
    print('\n[{}] : Number of folders older than {} days : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), round(daysToSec, 2), delet_count))
    if(testTrueFalse == True):
        print('\n[{}] : ||Test = True|| number of folders to delet : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), delet_count))
    else:
        print('\n[{}] : Number of deleted folders : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), delet_count))
