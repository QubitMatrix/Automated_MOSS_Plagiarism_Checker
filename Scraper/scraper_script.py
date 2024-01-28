import os
import sys

session = sys.argv[1]
print(session)
for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k']:
    print(f"daa-s{session}-{i}")
    while(os.path.exists(os.path.join(os.getcwd(),"daa-s"+session+"-"+i+'.csv'))==False):
        os.system(f"./start.sh daa-s{session}-{i}")
