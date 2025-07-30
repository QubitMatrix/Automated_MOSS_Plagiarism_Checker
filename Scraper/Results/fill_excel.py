import sys
import re
from datetime import date

year = str(date.today().year)
allsrn = open("all_srn_"+sys.argv[1]+".txt","r")
all_list = allsrn.readlines() # List of students SRN
leaderboardsrn = open("dsa-s"+sys.argv[2]+"-"+sys.argv[1]+"-"+year+".csv","r")
lead_list = leaderboardsrn.readlines() # List of all usernames in the leaderboard
plagsrn = open("../../moss/dsa-s"+sys.argv[2]+"-"+sys.argv[1]+"-"+year+".txt","r")
plag_list = plagsrn.readlines() # List of students with high plagiarism values
output_file = open("dsa-s"+sys.argv[2]+"-"+sys.argv[1]+"-"+year+"-final.csv", "w")
pattern = r'pes2ug2[2-4](cs|am)[0-9]{3}'
for student in all_list:
    flag=0
    for user_entry in lead_list:
        student = student.strip("\n").strip().lower()
        user_entry = user_entry.strip("\n").strip()
        user_entry = user_entry.split(",")
        username = user_entry[1].lower()
        score = user_entry[2]
        pla_flag = 0
        if(student in username):
            for plag_entry in plag_list:
                plag_srn = plag_entry.split()[0].lower()
                plag_val = plag_entry.split()[1][1:-1]
                if(student in plag_srn):
                    print(student+","+score+","+str(eval(score)*0.4)+","+plag_val, file=output_file)
                    pla_flag = 1
                    break
            if(pla_flag==0):
                print(student+","+score+","+score+",-", file=output_file)
            flag = 1
            break
    if(flag==0):
        print(student+",0,0,-", file=output_file)
for user_entry in lead_list:
    user_entry = user_entry.split(",")
    username = user_entry[1].lower()
    if(not bool(re.search(pattern,username))):
        print(username+","+user_entry[2], file=output_file)
allsrn.close()
leaderboardsrn.close()
plagsrn.close()
output_file.close()
