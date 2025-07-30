import os
import sys
from datetime import date

session = sys.argv[1]
year = str(date.today().year)
print(session)
for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'a-aiml', 'b-aiml']:
    print(f"dsa-s{session}-{i}-{year}")
    while(os.path.exists(os.path.join(os.getcwd(),"dsa-s"+session+"-"+i+"-"+year+'.csv'))==False):
        os.system(f"./start.sh dsa-s{session}-{i}-{year}")
