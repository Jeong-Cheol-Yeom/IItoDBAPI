import json, random
from collections import OrderedDict
import os
import platform ,psutil

def printSystemInfor():
 
    print('Process information  :\t', platform.processor())
    
    print('Process Architecture :\t', platform.machine())
    
    print('RAM Size             :\t',str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)")
 
if __name__ == '__main__':
 
    printSystemInfor()

file_data = OrderedDict()
idrange=['a','b','c','d','e']

file_data["ID"] = random.choice(idrange) + str(random.randrange(1,500))
file_data["Process_Information"] = platform.processor()
file_data["Process_Architecture"] = platform.machine()
file_data["RAM_Size"] = str(round(psutil.virtual_memory().total / (1024.0 **3)))+"(GB)"

print(json.dumps(file_data, ensure_ascii=False, indent="\t"))

with open("/home/jc/examples/records.json", 'w', encoding='utf-8') as make_file: json.dump(file_data, make_file, ensure_ascii=False, indent="\t")
