# Automated_MOSS_Plagiarism_Checker
This is a guide to a MOSS Plagiarism Checker for Hacckerrank contests with customized automation scripts. It is originally derived from [sbk173/Hackerrank-Scraper-and-MOSS-Plagiarism](https://github.com/sbk173/Hackerrank-Scraper-and-MOSS-Plagiarism) and a few changes have been made to it so as to automate the process completely.

## Download dependencies
   - Perl
   - Node (>=18)
   - Selenium - https://github.com/password123456/setup-selenium-with-chrome-driver-on-ubuntu_debian
   - npm 

## Important Note
- The scripts have been written using bash and it is recommended to use unix shells or run the WSL distro shell by running the distro from windows search (WSL required)   
- If it is not possible to run the script please follow the commands in the scripts and execute them individually (Installing WSL is much more easier and just requires a few steps -> `wsl --install -d Ubuntu`)

> Line endings and other special character issues might pop up if run on windows command prompt or powershell directly, some users might face an issue with even `bash` on powershell so it is best to follow the steps given above 

## Setup (just needed for the first time)
1. Clone the repo   
   `git clone https://github.com/QubitMatrix/Automated_MOSS_Plagiarism_Checker.git`
2. Ensure all dependencies are fulfilled   
   `pip install -r requirements.txt`
2. Move into the Scraper folder   
   `cd Automated_MOSS_Plagiarism_Checker/Scraper`
3. Retrieve Cookie   
   - Get the cookie value from any XHR requests on the hackerrank page (Developer Tools, Network Tab)
   - Set the cookie variable in `./start.sh` with the value from previous step
4. Give execution permission to start.sh and moss.pl   
      `chmod u+x start.sh`   
      `chmod u+x ../moss/moss.pl`
5. Save a file with all students SRN   
   For each section handled create a file `all_srn_'section'.txt` in the `Scraper/Results` directory. This file should contain the sorted list of all SRN as given in the shared excel sheet

## Execution
1. Move back to the main directory and execute the script   
   `cd ../ && bash ./automate.sh "enter session number here"`   
   > Eg: `bash ./automate.sh 1` can generate report for all contests with daa-s1-'section'-'year'   
   => Replace the sections list in `automate.sh` and `./Scraper/scraper_script.py` with the sections that you are handling, not changing the sections will lead to invalid json response errors.  

> If execution gives an error `/usr/bin/env: ‘bash\r’: No such file or directory` it might be due to npm not being installed, install npm on the WSL distro and try again   

> `FetchError: invalid json response body at https://www.hackerrank.com/rest/contests` error might be caused if the cookies have changed recheck if the cookie value given in start.sh and the admin contest page match   

## Results
- The final plagiarism links will be available in `./moss/plagiarismReport.csv`   
- The list of students with plagiarism above threshold will be stored in individual files `./moss/'contest_slug'.txt`   
- The scores extracted from the leaderboard will be stored in `./Scraper/Results`

**The only file required to fill the marksheet is the `'contestslug'-final.csv` in the `Scraper/Results` directory.**   
  > If any student's username doesn't follow the naming convention their results will be stored at the end of this file and will have to be manually handled.

If you have questions or ideas, just drop them in the issues section!
