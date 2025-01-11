import sys
import numpy as np
import pandas as pd
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager



def getLeaderBoard(url):
    options = Options()
    #options.add_argument('--headless') # Uncomment to run without GUI but may not work correctly always
    #options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)


    maxPage = 14  # Set the maxPage limit
    pos1 = url[::-1].index("/")
    pos2 = url[::-1].index("/", pos1+1)
    slug = url[len(url)-pos2:len(url)-pos1-1]
    #print(url,slug)

    def getPage(number):  # Return the leaderboard for given page number
        browser.get(url + "/" + str(number))
        browser.implicitly_wait(5)
        if len(browser.find_elements(By.CLASS_NAME,"acm-leaderboard-cell  ")) > 10:
            return 1, [x.text for x in browser.find_elements(By.CLASS_NAME,"acm-leaderboard-cell  ")]
        return 0, [x.text for x in browser.find_elements(By.CLASS_NAME,"leaderboard-list-view")]


    columnLength = 0
    if getPage(1)[0]:
        columnLength = max(int(len(getPage(1)[1]) / 10), int(len(getPage(1)[1]) / 10))
    else:
        if(len(getPage(1)[1]) !=0):
            columnLength = len([text.split('\n') for text in getPage(1)[1]][0])

    if(columnLength == 0):
        print("No Submissions")
        return

    leaderboard = np.empty((0, columnLength))
    print("HackerRank scraping started.\n")
    number = 1  # Current page number

    # Loop over until there are no end page arrows
    while maxPage + 1 > number:
        try:
            pageType, pageList = getPage(number)
            if pageType:
                pageList = np.array(pageList).reshape(-1, columnLength)
            else:
                pageList = np.array([text.split('\n') for text in pageList])
            if pageList.shape[0] < 10:
                try:
                    browser.find_element(By.LINK_TEXT,str(number + 1))
                except NoSuchElementException:
                    #print(pageList)
                    if(len(pageList) != 0):leaderboard = np.append(leaderboard, pageList, axis=0)
                    break
                raise ZeroDivisionError("Could not get all in page {}".format(number))
            leaderboard = np.append(leaderboard, pageList, axis=0)
        except ZeroDivisionError:
            number -= 1
        finally:
            number += 1

    browser.close()
    browser.quit()

    # Convert the array to pandas DataFrame
    leaderboard = pd.DataFrame(leaderboard)
    leaderboard.rename(columns=lambda x: str(int(x)), inplace=True)
    leaderboard.drop_duplicates(keep='last', inplace=True)
    leaderboard["0"] = pd.to_numeric(leaderboard["0"])
    leaderboard.sort_values(by=['0'], inplace=True)
    leaderboard.reset_index(drop=True, inplace=True)

    leaderboard.rename(columns=lambda x: str(int(x) - 3), inplace=True)
    leaderboard = leaderboard.add_prefix('Q')
    leaderboard.rename(columns={'Q-3': 'rank', 'Q-2': 'user', 'Q-1': 'score', 'Q0': 'time'}, inplace=True)

    if leaderboard.shape[0] < 1:
        print("Could not find a leaderboard with this URL. Please check the URL and try again.")
    else:
        print("HackerRank scrape completed.\nScraped board length: ", leaderboard.shape[0])
        leaderboard.to_csv("./Results/"+slug+".csv", index=False)
        print("Results saved in Scraper/Results/")

if(__name__ == '__main__'):
    getLeaderBoard(sys.argv[1])
    
