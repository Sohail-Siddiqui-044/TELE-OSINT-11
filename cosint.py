import username, EmailScan
from username import NameUser
from EmailScan import GetEmail
from phonenum import carrierlookup
from web import Web
from metadata import gps_analyzer
#from reverseimg import reverseImg
from multipleip import get_ip
from maclookup import macLookup
#from sentinment import GetTweet

MainFunctions={
 1: carrierlookup,
 2: GetEmail,
 3: Web,
 4: gps_analyzer,
 5: get_ip,
 6: macLookup,
}


def Menu():
    Selection = 1
    while True:
        print("Intership Project")
        print('')
        print("1. Phone Number")
        print("2. Email")
        print("3. Domain")
        print("4. Metadata Analyzer")
        print("5. IP Heatmap")
        print("6. Mac Address Lookup")
        print("7. Exit")
        
        print('')
        Selection = int(input(">> "))
        print('')
        if (Selection == 1):
            MainFunctions[Selection]()
        elif (Selection == 2):
            MainFunctions[Selection]()
        elif (Selection == 3):
            MainFunctions[Selection]()
        elif (Selection == 4):
            MainFunctions[Selection]()
        elif (Selection == 5):
            MainFunctions[Selection]()
        elif Selection == 6:
            MainFunctions[Selection]()
        elif Selection == 7:
            
            exit()            
        else:
            print("Please choose an Appropriate option")



if __name__ == "__main__":
    Menu()
