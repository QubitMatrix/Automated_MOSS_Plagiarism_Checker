import os
import sys
from datetime import date

session = sys.argv[1]
year = str(date.today().year)
print(session)
for i in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'a_aiml', 'b_aiml']:
    print(f"daa-s{session}-{i}-{year}")
    while(os.path.exists(os.path.join(os.getcwd(),"daa-s"+session+"-"+i+"-"+year+'.csv'))==False):
        os.system(f"./start.sh daa-s{session}-{i}-{year}")
