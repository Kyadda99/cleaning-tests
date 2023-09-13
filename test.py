import os
import time

def rozszerzenie(oneFile):
    temp = oneFile.split('.')[-1]
    return + temp


def wgraj(rozszerzenie):
    pathname = 'rozszerzenia %s' % (rozszerzenie)
    if not os.path.exists(pathname):
        os.makedirs(pathname)
    
    

def dateCheck(fileName):
    data = os.path.getctime(fileName)
    dataTranslated = time.ctime(data)
    el1 = dataTranslated[4:7]
    el2 = dataTranslated[20:24]
    return [el1,el2]



wyn = dateCheck("C:\\Users\lukasz.ligezka\Downloads\Dziennik praktyk.docx")


print(wyn)