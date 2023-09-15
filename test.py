import os
import time
import shutil

os.makedirs('Porządek')

location = 'D:\\Śmietnik\Testowy — kopia'
locationNew = os.getcwd()
# location = os.getcwd()
# print(location)

def rozszerzenie(oneFile):
    return oneFile.split('.')[-1]
 

def check(file,loc):
    way=loc+"\\"+ file
    if os.path.isdir(way):
        main(way)
    else:
        wgraj(way,loc)



def wgraj(file,locFrom,loc=locationNew):
    rozszerzenie(file)
    loc = loc+"\\"+folderName
    folderName = 'rozszerzenia %s' % (rozszerzenie)
    if not os.path.exists(loc):
        os.makedirs(loc)
    shutil.move(locFrom,loc)
    
    

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


    





