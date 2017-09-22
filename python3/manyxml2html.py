# 10.09.2017
# есть папка. обойти подпапки, выбрать xml, из него название отчёта и сохранить в html

# исходная папка
IN_FOLDER="c:\\temp\\2017-iasp\\water\\explorationreport\\Data"

# файл с результатом
OUT_FILE="c:\\temp\\2017-iasp\\expreplist.js"

import os
import codecs
import xml.etree.ElementTree as ET
import json


def addReport(folder,fullpath):
    tree = ET.parse(fullpath)
    rt = tree.getroot()
    rname = rt.find('name').text
    rinv = rt.get('inv')
    ryear = rt.find('year').text
    result.append({"n":rname,"y":ryear,"i":rinv})
    


#=== main function


result=[]
for d in os.listdir(IN_FOLDER) :
    abfile=os.path.join(IN_FOLDER,d, "about.xml")
    if os.access(abfile,os.F_OK):
        addReport(d,abfile)
file = codecs.open(OUT_FILE, "w", "utf-8")
file.write("rr="+json.dumps(result))
file.close()
print("--Done--")


#file.write("rlist=[")
#file = codecs.open("temp", "w", "utf-8")
#file.write(codecs.BOM_UTF8)
#file.close()
#    print(type(tree.findall('./name')))
#name = tree.findall('./Valute[@ID="R01235"]/Value')[0].text
#for root,dirs,files in os.walk(IN_FOLDER):
#    if os.access(os.path.join(root, "about.xml"),os.F_OK):
#        print (root)



#    print ("==here==")
#    print(root)
#    for dirname in root:
#        print (os.path.join(root, dirname))
#        print ("here")
#        print(dirname)
