import csv
import os
import sys

directory = sys.argv[1]
challangeNames = []
if(os.path.exists(os.path.join(os.getcwd(),directory)) == False):
    os.mkdir(directory)
with open(sys.argv[2].split('/')[-1],'r') as f:
    reader = csv.reader(f)
    next(reader,None)
    for line in reader:
        if(os.path.exists(os.path.join(os.getcwd(),directory,line[1])) == False):
           os.mkdir(os.path.join(os.getcwd(),directory,line[1]))
        newname = line[2].replace(' ','_').replace('"','').replace("'",'')
        if(newname not in challangeNames):
            challangeNames.append(newname)
        filename = os.path.join(os.getcwd(),directory,line[1],newname+'.c')
        with open(filename,'w') as f:
            f.write(line[-1])

with open('../moss/filenames.txt','w') as f:
    f.writelines([x+'.c'+'\n' for x in challangeNames])



