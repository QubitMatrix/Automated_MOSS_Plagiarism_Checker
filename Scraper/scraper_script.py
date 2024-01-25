import os
import sys

sections = sys.argv[1].split() 
print(sections)
for i in sections:
    print(i)
    while(os.path.exists(os.path.join(os.getcwd(),i+'.csv'))==False):
        os.system(f"./start.sh {i}")