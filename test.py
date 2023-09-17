import os
import time
import shutil
from tkinter import filedialog

location = filedialog.askdirectory()
locationNew = location.split('/')[-1]
locationNew = location.replace(locationNew,'')
# print (locationNew)
i=1
if os.path.exists(locationNew+'/Porządek'):
    while i>0:
        if not os.path.exists(locationNew+'/Porządek'+'(%s)'%(i)):
            sortedDir='Porządek'+'(%s)'%(i)
            break
        else:
            i=i+1
else:
    sortedDir= 'Porządek'





# Pożądek był w tym folderze co pliki
# dodać if żeby pliki bez rozszerzenia tam lądąowały


def rozszerzenie(oneFile):
    if '.' in oneFile:
        return oneFile.split('.')[-1]
    else:
        return 'brak_rozszerzenia' 
 

def check(file,loc):
    way=loc+"/"+ file
    # print("        way  "+way)
    boolean = os.path.isfile(way)
    if not boolean:
        main(way)
    else:
        wgraj(way,loc)



def wgraj(file,locFrom,loc=locationNew,sortDir=sortedDir):
    end= rozszerzenie(file)
    folderName = 'rozszerzenia %s' % (end)
    # print(folderName)
    loc = loc+sortDir+"/"+folderName
    if not os.path.exists(loc):
        os.makedirs(loc)
    filePathNew=loc+'/'+file.split('/')[-1]
    exist = os.path.exists(filePathNew)
    if not exist:
        shutil.move(file,loc)
    else:
        i=1
        while i>0:
            if not os.path.exists(copyName(filePathNew,i)):
                os.rename(file,copyName(loc+'/'+file.split('/')[-1],i))
                break
            else:
                i=i+1

def copyName(name,numer):
    after = name.split('.')[-1]
    before = name.replace('.'+after,'')

    return before + '(%s)' % (str(numer)) +'.'+ after




    
def dateMove(date,loc):
    # print (date)
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
    # print(dirList)
    for i in dirList:
        dirPath=loc+'/'+i
        newDirList=os.listdir(dirPath)
        # print(newDirList)
        for j in newDirList:
            filePath=dirPath+'/'+j
            datefile=dateCheck(filePath)
            dateMove(datefile,filePath)
        




def all(loc,locNew,sortDir=sortedDir):
    main(loc)
    locNew=locNew+'/'+sortedDir
    datySort(locNew)


all(location,locationNew)



