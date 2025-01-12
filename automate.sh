session=$1 
array=('a' 'b' 'c' 'd' 'e' 'f' 'g' 'h' 'i' 'j' 'k' 'a-aiml' 'b-aiml')
year=$(date '+%Y')
touch ./moss/plagiarismReport.csv
if [ ! -s "./moss/plagiarismReport.csv" ];
then
    echo Section,Link >> ./moss/plagiarismReport.csv
fi

# Scrape all submissions from hackerrank
cd Scraper
mkdir -p Results
npm install
python3 scraper_script.py "$session"
for section in ${array[@]};
do
    slug="daa-s$session-$section-$year"
	file1="./Results/$slug.csv"
	if [ ! -f $file1 ];
	then
		python3 leaderboard.py "https://www.hackerrank.com/contests/$slug/leaderboard"
	fi
    echo $slug
    cp $slug.csv ../Submission

    # Organize submissions into a separate folder for each student
    cd ../Submission
    mkdir -p Submissions
    python3 organizeCodes.py ./Submissions/ $slug.csv
    mv ./Submissions ../moss/

    # Send the pruned submissions to MOSS servers for plagiarism check
    cd ../moss
    mkdir -p hwX_join hwX_prune
    touch temp.txt plagiarismReport.csv
    python3 run_moss.py $slug

    # Clear all intermediate files and folders generated and go to Scraper
    rm -rf hwX_join hwX_prune Submissions
    truncate -s 0 ./temp.txt
	cd ../Scraper
done

echo -e "Plagiarism links will be available in ./moss/plagiarismReport.csv\n"
cd ../moss
bash ./gen_list.sh

for section in ${array[@]};
do
	# Generate final list from leaderboard and deduction after plagiarism
	cd ../Scraper/Results/
	python3 fill_excel.py $section $session
	cd ../
done
