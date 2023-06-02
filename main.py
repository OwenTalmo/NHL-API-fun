import requests

def main():
    # API URL
    API_URL = 'https://statsapi.web.nhl.com/api/v1'

    # get data about a draft
    year = 2018
    round = 1 # 1-7
    pick = 22 # 1-30 (or so, depends on the year!)
    response = requests.get(API_URL + "/draft/"+ str(year)).json()
    player = response["drafts"][0]["rounds"][round-1]["picks"][pick-1]
    print("With pick number " + str(player["pickOverall"]) + " in the NHL Draft, the " + player["team"]["name"] 
          + " are proud to select... " + player["prospect"]["fullName"] + "!")
    

if __name__ == "__main__":
    main()
