### ImageFap Gallery Downloader
### download queue management

import config
import IFUser
from Tkinter import Tk

queue = []

def CheckUrl(url):
    ### check if url looks like a gallery url
    if (url.find(config.GalleryLink1)!=-1):
        return 1 #IF1
    elif (url.find(config.GalleryLink2)!=-1):
        return 2 #IF2
    elif (url.find(config.GalleryLink3)!=-1):
        return 3 #XH
    elif (url.find(config.GalleryLink4)!=-1):
        return 4 #IF3
    elif (url.find(config.IFFolder1)!=-1):
        return 5 #IFFolder1
    elif (url.find(config.IFFolder2)!=-1):
        return 6 #IFFolder2
    elif (url.find(config.IFUserLink)!=-1):
        return 7 #IFUser
    else:
        return 0

def PollClipboard():
    ### retrieve the current clipboard content
    try:
        clip = Tk()
        clip.withdraw()
        clipb = clip.clipboard_get()
        clip.destroy()
    except:
        clipb = ''
    return clipb

def AddToQueue(url,urltype,destination_folder):
    global queue
    queue+=[[url,urltype,destination_folder]]

def RemoveFromQueue():
    global queue
    queue.remove(queue[0])

def AddFolder(FolderUrl):
    UserName, FolderName, Galleries = IFUser.ListFolderGalleries(FolderUrl)
    for Gal in Galleries:
        AddToQueue(Gal,4,config.MainDirectory+"/"+config.UserDirectory+"/"+UserName+"/"+FolderName)
    
def CheckClipboard():
    ### check if clipboard content has changed
    ### check if the new content is a valid url and add to queue
    global last_clipboard
    # print(PollClipboard()) # simply checks what's currently in the clipboard
    clipboard = PollClipboard()
            
    if (clipboard!=last_clipboard):
        last_clipboard=clipboard
        urltype = CheckUrl(clipboard)
        if urltype:
            print("Content Detected:")
            if urltype<5:
                ### add url to queue
                #print("URL-type: "+str(urltype))
                if urltype==3:
                    AddToQueue(clipboard,urltype,config.MainDirectory+"/xHamster")
                else:
                    AddToQueue(clipboard,urltype,config.MainDirectory+"/ImageFap")
            elif urltype<7:
                AddFolder(clipboard)
            elif urltype==7:
                #print("Profile:")
                Username, Folders = IFUser.ListUserFolders(clipboard)
                #print("ran folders")
                for Folder in Folders:
                    #print(Folder)
                    AddFolder(Folder[1])

last_clipboard = PollClipboard()
