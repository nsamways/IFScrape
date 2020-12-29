import config
import request
from gallery import RemoveBlank

def GetUsername(htmldata):
    titlestr = "<title>View "
    start = htmldata.find(titlestr)
    end = htmldata.find("&#039;",start)
   # print("Username is: " + str(htmldata[start+len(titlestr):end]))
    return htmldata[start+len(titlestr):end]
    
def GetUsername2(htmldata):
    titlestr = "<title>Browse"
    start = htmldata.find(titlestr)
    end = htmldata.find("&#039;",start)
   # print("Username is: " + str(htmldata[start+len(titlestr):end]))
    return htmldata[start+len(titlestr):end]


def ListUserFolders(ProfileUrl):
    htmldata = request.ReqUrl(ProfileUrl)
    Username = GetUsername(htmldata)
    galleries_searchstring = "/usergallery.php"
    start = htmldata.find(galleries_searchstring)
    end = htmldata.find('"',start)

    GalsUrl = config.baseurl+htmldata[start:end]
    # print("Trying to get GalsURL: " +GalsUrl)
    htmldata = request.ReqUrl(GalsUrl)

    j=0
    k=0
    
    folderid = ''
    Folders = []
    while (folderid!="folderid=-1"):
        j = htmldata.find("folderid=",k)
        k = htmldata.find('"',j)
        folderid = htmldata[j:k]
        J = j
        l=-1
        while (l==-1):
            J=J-10
            l = htmldata[J:k].find("https:")
        
        FolderUrl = htmldata[l+J:k]

        if (folderid!="folderid=0" and len(folderid)>0):
            n = htmldata.find(">",k)
            m = htmldata.find("<",n)
            FolderName = htmldata[n+1:m]
            Folders+=[[FolderName,FolderUrl]]
            
    return Username, Folders

def GetFolderName(htmldata):
    folderid="folderid=0"
    j=0
    k=0
    while (folderid == "folderid=0"):
        j = htmldata.find("folderid=",k)
        k = htmldata.find('"',j)
        folderid=htmldata[j:k]
    j = htmldata.find("<b>",k)
    k = htmldata.find("</b>",j)
    return htmldata[j+3:k]
    
def ListFolderGalleries(FolderUrl):
    htmldata = request.ReqUrl(FolderUrl)
    UserName = GetUsername2(htmldata)
    #print("username: " + UserName)
    FolderName = GetFolderName(htmldata)
    #print("Folder name is: " +FolderName)
    Galleries = []
    j=0
    k=0
    while True:
        j = htmldata.find("/gallery/",k)
        if (j==-1):break
        k = htmldata.find('"',j)
        GalleryUrl = config.baseurl+htmldata[j:k]

        if not(GalleryUrl in Galleries):
            Galleries+=[GalleryUrl]

    #print(Galleries)
    
    return RemoveBlank(UserName), RemoveBlank(FolderName), Galleries

