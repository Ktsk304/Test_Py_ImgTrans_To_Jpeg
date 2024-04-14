from email.mime import image
import os
import pathlib
from PIL import Image

strFullPath = "D:\\t"

arrFiles = os.listdir(strFullPath)

for tgtVal in arrFiles:
    
    strTargetPath = strFullPath + "\\" +  tgtVal
    
    strExtension = pathlib.Path(tgtVal).suffix

    if strExtension == "":
    
        arrFolder = os.listdir(strTargetPath)
        
        for tgtFile in arrFolder:
            
            strTempPath = strTargetPath + "\\" + tgtFile
            
            strFile_Extension = pathlib.Path(strTempPath).suffix
            
            if strFile_Extension == ".png":
                
                im = Image.open(strTempPath)
                
                im = im.convert("RGB")
                
                strFolderpath = str(pathlib.PurePath(strTempPath).parent)

                strFilename = str(pathlib.Path(strTempPath).stem)
                
                im.save(strFolderpath + "\\" + strFilename + ".jpeg")
                
                im.close

                os.remove(strTempPath)
    else:

        strFile_Extension = pathlib.Path(strTargetPath).suffix
            
        if strFile_Extension == ".png":
                
            im = Image.open(strTargetPath)
                
            im = im.convert("RGB")
                
            strFolderpath = str(pathlib.PurePath(strTargetPath).parent)

            strFilename = str(pathlib.Path(strTargetPath).stem)
                
            im.save(strFolderpath + "\\" + strFilename + ".jpeg")
                
            im.close

            os.remove(strTargetPath)
    
    
    

    

        

        