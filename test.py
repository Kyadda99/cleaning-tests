import os
import time



def dateCheck(file):
    data = os.path.getctime(file)
    dataTranslated = time.ctime(data)
    el1 = dataTranslated[4:7]
    el2 = dataTranslated[20:24]
    return [el1,el2]



wyn = dateCheck("C:\\Users\lukasz.ligezka\Downloads\Dziennik praktyk.docx")


print(wyn)