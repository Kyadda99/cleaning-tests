import os
import time
import shutil
from tkinter import filedialog

location = filedialog.askdirectory()
locationNew = location.split('/')[-1]
locationNew = location.replace(locationNew,'')
print (locationNew)




def rozszerzenie(oneFile):
    return oneFile.split('.')[-1]
 

def check(file,loc):
    way=loc+"/"+ file
    # print("        way  "+way)
    boolean = os.path.isfile(way)
    if not boolean:
        main(way)
    else:
        wgraj(way,loc)



def wgraj(file,locFrom,loc=locationNew):
    end= rozszerzenie(file)
    folderName = 'rozszerzenia %s' % (end)
    # print(folderName)
    loc = loc+"Porządek/"+folderName
    # print("        loc from  "+file)
    # print('             loc  '+loc)
    if not os.path.exists(loc):
        os.makedirs(loc)
    shutil.move(file,loc)
    
def dateMove(date,loc):
    print (date)
    locDate = loc.split('/')[-1]
    locDate = loc.replace(locDate,'')
    locDate = locDate +'/'+ transDate(date)
    if not os.path.exists(locDate):
        os.makedirs(locDate)
    shutil.move(loc,locDate)

def transDate(date):
    month=date[0]
    year=' '+ date[1]
    if month == 'Jan':
        return 'Styczeń'+ year
    elif month == 'Feb':
        return 'Luty'+ year
    elif month == 'Mar':
        return 'Marzec'+ year
    elif month == 'Apr':
        return 'Kwiecień'+ year
    elif month == 'May':
        return 'Maj'+ year
    elif month == 'Jun':
        return 'Czerwiec'+ year
    elif month == 'Jul':
        return 'Lipiec'+ year
    elif month == 'Aug':
        return 'Sierpień'+ year
    elif month == 'Sep':
        return 'Wrzesień'+ year
    elif month == 'Oct':
        return 'Paźdźernik'+ year
    elif month == 'Nov':
        return 'Listopad'+ year
    else:
        return 'Grudzień'+ year
    
    

    

def dateCheck(fileName):
    data = os.path.getctime(fileName)
    dataTranslated = time.ctime(data)
    el1 = dataTranslated[4:7]
    el2 = dataTranslated[20:24]
    return [el1,el2]


def main(loc):
    plikiPrzed= os.listdir(loc)
    
    for i in plikiPrzed:
        check(i,loc)
    os.rmdir(loc)

def datySort(loc):
    dirList=os.listdir(loc)
    print(dirList)
    for i in dirList:
        dirPath=loc+'/'+i
        newDirList=os.listdir(dirPath)
        print(newDirList)
        for j in newDirList:
            filePath=dirPath+'/'+j
            datefile=dateCheck(filePath)
            dateMove(datefile,filePath)
        




def all(loc,locNew):
    main(loc)
    locNew=locNew+'/Porządek'
    datySort(locNew)


all(location,locationNew)



