import os
import time
import stat
import shutil
import argparse
from datetime import datetime

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
    print('\n[{}] : Cleaning session started ! Checking folders older than : {} day...'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), round((olderThan/60/60)/24, 2)))
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
    print('\n[{}] : Number of folders older than {} days : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), round((olderThan/60/60)/24, 2), delet_count))
    if(testTrueFalse == True):
        print('\n[{}] : ||Test = True|| number of folders to delet : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), delet_count))
    else:
        print('\n[{}] : Number of deleted folders : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), delet_count))
    

parser = argparse.ArgumentParser(description='Delet files older than explanation')
parser.add_argument('-p', '--path', type=str, help='Path to files')
parser.add_argument('-o', '--older', type=float, default=28, help='Older than, in days, for houre use 0.1, 0.2 . 0.3, ... (default: 1 month(2419200s)')
parser.add_argument('-t', '--test', type=str, default=True, help='boolean (default: True) (ex: -t 1/True or -t 0/False')  
parsed_args = parser.parse_args()

#############################################################
# Checking if arguments are correct
argTest = True
argsCheckOk = False

if parsed_args.path is not None:
    if type(parsed_args.older) is float or int:
        if (parsed_args.older > 0):
            if(parsed_args.test == '1' or parsed_args.test == 'True' or parsed_args.test == 'true' or parsed_args.test == True):
                argTest = True
                argsCheckOk = True
            elif(parsed_args.test == '0' or parsed_args.test == 'False' or parsed_args.test == 'false'):
                argTest = False
                argsCheckOk = True           
            else:
                print('Test argument error. Accepted arguments 1, True, true, 0, False, false')
        else:
            print('Older value is too small')
    else:
        print('Error, older argument must be an int or float')
else:
    print('No path, please enter a path. For help : -h, --help')

#############################################################

if(argsCheckOk == True):
    daysToSec = ((parsed_args.older*24)*60)*60
    #print('\n' + parsed_args.path + '\n' + str(daysToSec) + '\n' + str(parsed_args.test) + '\n')
    if(parsed_args.older >= 1):
        print('\n[{}] : Checking files older than {} days in folder : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), parsed_args.older, parsed_args.path))
    else:
        print('\n[{}] : Checking files older than {} days ({} sec) in folder : {}'.format(datetime.now().strftime('%Y-%m-%d %H:%M:%S'), parsed_args.older, round(daysToSec), parsed_args.path))
    time.sleep(5)
    FolderCleaning(parsed_args.path, daysToSec, argTest) # args = path, remove_folders_older_than (INT, in seconds), Test (True or False)

