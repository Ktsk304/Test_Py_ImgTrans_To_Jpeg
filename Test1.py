def get_fileList_from_dir(dir_path):
    import os
    fileList = []
    for root, dirs, files in os.walk(dir_path):
        for file in files:
            fileList.append(os.path.join(root, file))
    
    print(fileList)

    return fileList

get_fileList_from_dir("C:\\Users\\grgst\\Downloads")