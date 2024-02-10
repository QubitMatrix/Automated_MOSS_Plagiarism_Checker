while read line
do
	url=$(echo $line | awk -F, '{ print $2 }')
	contest=$(echo $line | awk -F, '{ print $1 }')
	slug=$(echo $url | awk -F/ '{ print $6 }')
	echo $url,$slug,$contest
	if [ ! -f $contest.txt -a ! -f $slug ]
	then
		wget $url 
		grep -i -o PES.*[4-9][0-9]%\) $slug | sed s/"_join.c"/""/g > $contest.txt 
	fi
done < "plagiarismReport.csv"
