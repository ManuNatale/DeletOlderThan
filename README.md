# delet-older-than
Python script for deleting folders or files older than .... in a given path

Windows and Linux compatible

# Utilisation for the console mode:

  In command prompt type:
  
         ~$ python DeletOlderThan.py --path --older --test                        
                                                        
  
 Arguments:
  - --path "Enter the destination path to delet files"
  - --older "Time older than ... in days. For same day, use coma (ex : 0.2 day)"
  - --test "You can set it to True to only check the folders and not delet them.
            It is set to True by default to reduce the risk of error. It need to be 
            manually set to False.
 - --help "Display help"
                                                             
# Example:

    ~$ python DeletOlderThan.py --path C:\Users\pictures\ --older 5 --test True  #Checking picture older than 5 days with test enable
    
        #Output : Checking files older than 5.0 days in folder : C:\Users\pictures\
    
    ~$ python DeletOlderThan.py --path C:\Users\pictures\ --older 5 --test False  #Deleting all files in pictures older than 5 days
