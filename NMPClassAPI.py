import requests
import json
import sys
import pandas as pd

class NmpApi:

    # self._filename enables the arguments passed at initializatio to be available throughout the class 
    def __init__(self, filename):
        self._filename = filename

    # To enble repl testing of filename 
    def filename(self):
        #return self._filename
        self._filename = filename

    def CreateCJar(self):

        ''' Create the cookie jar to access NMP'''
        jar1=requests.cookies.RequestsCookieJar()
        # request user enters AspNet and csrf cookies 

        aspc = input("Please enter the AspNet cookie:")
        csrf = input("Please enter the csrf cookie:")
        # set the cookies in the jar
        jar1.set('.AspNet.Cookies',aspc,domain='nmp.services.skypeforbusiness.com',path='/')

        jar1.set('csrf',csrf,domain='nmp.services.skypeforbusiness.com',path='/')

        self._jar1 = jar1
    
    def jar1(self):
        return self._jar1


    def NMPQuery(self):
        ''' Query the nmp service'''
        data =[line.strip() for line in open(self._filename,'r')] 
        with open('c:/pyfund/gitrepo/GeocodesNMP/geocode_json.txt', mode='wt',encoding='utf-8') as jsonfile:
            for item in data:
                r = requests.get(item,cookies = self._jar1).json()
                print(json.dumps(r), file = jsonfile)
    
    def ExcelExport(self):
         # opens json data into a list of dictionaries
        jdata = []
        with open('c:/pyfund/gitrepo/geocodesnmp/geocode_json.txt', 'r') as jsondata:
            for line in jsondata:
                jdata.append(json.loads(line))

        # Create a pandas dataframe from the dictionary items in the list 
        df= pd.DataFrame(jdata)

        #Export the pandas dataframe as an excel doc
        with open('c:/pyfund/GITRepo/GeocodesNMP/geocode.xlsx', 'wb') as geoxls:
            df.to_excel(geoxls)

def main(filename):
    obj = NmpApi(filename)
    obj.CreateCJar()
    obj.NMPQuery()
    obj.ExcelExport()


''' Enables code to be ran as a python script'''

if __name__ == '__main__':
    main(sys.argv[1])