from email.mime import image
import os
import pathlib
from tkinter.tix import CheckList
from PIL import Image

strFullPath = "D:\p"

arrFiles = os.listdir(strFullPath)

Cehck_List = set()

for tgtVal in arrFiles:
    
    strTargetPath = strFullPath + "\\" +  tgtVal
    
    strExtension = pathlib.Path(tgtVal).suffix

    if strExtension == "":
    
        arrFolder = os.listdir(strTargetPath)
        
        for tgtFile in arrFolder:
            
            strTempPath = strTargetPath + "\\" + tgtFile
            
            strFile_Extension = pathlib.Path(strTempPath).suffix
            
            if strFile_Extension != ".png":

                Cehck_List.add(tgtFile.replace(strFile_Extension , ""))

        for tgtFile in arrFolder:
            
            strTempPath = strTargetPath + "\\" + tgtFile
            
            strFile_Extension = pathlib.Path(strTempPath).suffix
            
            if strFile_Extension == ".png":
                
                if tgtFile.replace(strFile_Extension , "") in Cehck_List:
                    
                    os.remove(strTempPath)
    else:
        print(strExtension)
    
    
    

    

        

        