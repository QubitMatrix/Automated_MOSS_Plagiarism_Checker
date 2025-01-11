import sys
import re
from datetime import date

year = str(date.today().year)
allsrn = open("all_srn_"+sys.argv[1]+".txt","r")
all_list = allsrn.readlines()
leaderboardsrn = open("daa-s"+sys.argv[2]+"-"+sys.argv[1]+"-"+year+".csv","r")
lead_list = leaderboardsrn.readlines()
plagsrn = open("../../moss/daa-s"+sys.argv[2]+"-"+sys.argv[1]+"-"+year+".txt","r")
plag_list = plagsrn.readlines()
file1 = open("daa-s"+sys.argv[2]+"-"+sys.argv[1]+"-"+year+"-final.csv", "w")
pattern = r"^pes2ug22cs[0-9][0-9][0-9]$"
for x in all_list:
    flag=0
    for y in lead_list:
        x=x.strip("\n").lower()
        y=y.strip("\n")
        y=y.split(",")
        srn=y[1].lower()
        pla_flag=0
        if(x==srn):
            for z in plag_list:
                z=z.split()[0].lower()
                if(z==x):
                    print(x+","+y[2]+","+str(eval(y[2])*0.6), file=file1)
                    pla_flag=1
                    break
            if(pla_flag==0):
                print(x+","+y[2]+","+y[2], file=file1)
            flag=1
            break
    if(flag==0):
        print(x+",0,0", file=file1)
for x in lead_list:
    x=x.split(",")
    srn=x[1].lower()
    if(not bool(re.match(pattern,srn))):
        print(srn+","+x[2], file=file1)
allsrn.close()
leaderboardsrn.close()
plagsrn.close()
file1.close()
