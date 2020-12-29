### ImageFap Gallery Downloader
### General purpose download function

from os import path, makedirs
import request
import time

def DownloadImage(url,Dir,attempts=2):
    #print("in DownloadImage")
    startTime = time.time()
    success = 0
    for k in range(attempts):
        pic = request.ReqUrl(url)
        if (pic!=[]):
            success = 1
            break
        else:
            time.sleep(0.5)

    if success:    
        ### create output directory if it doesn't exist
        if not path.exists(Dir):
            makedirs(Dir)
        i=0
        while True:
            _i = i
            i = url.find('/',i+1)
            if (i==-1): break
        
        fname_end = url.find('?')
        
        fname = url[_i+1:fname_end]
        #print("Fname is: "+fname)
        #print("URL is: " +url)
        _path = Dir+'/'+fname

        while True:
            ### check if file already exists, in which case progressing numbers are added to the new filename to avoid overwriting of older files.
            pic_num = 0
            if not path.exists(_path):
                f = open(_path,'wb')
                f.write(pic)
                f.close()
                break
            else:
                pic_num+=1
                k = fname.find('.')
                fn1 = fname[:k]
                ext = fname[k:]
                fname = fn1+str(pic_num)+ext
                _path = Dir+'/'+fname
      #  print("Success: was in download.py for: " + str(time.time() - startTime))
        return 1
    else:
       # print("Failure: was in download.py for: " + str(time.time() - startTime))
        return 0
    
    #print("should download: " +url)
    return(0)
