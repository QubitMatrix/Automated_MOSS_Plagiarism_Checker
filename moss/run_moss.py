import os
import sys
import pandas
import time

slug = sys.argv[1]
os.system("python3 prune_files.py Submissions/ hwX_prune/ hwX_join/ ")
os.system("./moss.pl -l c hwX_join/*.c >> temp.txt")
with open('temp.txt') as f:
    link = f.readlines()[-1].strip()
    df = pandas.read_csv('plagiarismReport.csv',index_col=False)
    df.loc[len(df)] = [slug.split('/')[-1],link]
    df.to_csv('plagiarismReport.csv',index=False)



