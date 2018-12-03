import sys
from itertools import islice

def GeoList(filename):
    ''' open a text file containing a list of geocodes, strip the /n and '-', save each geocode to a list of lists '''

    lst=[] #Create an empty list 
    with open(filename) as g: #Open geocode file 
        for line in g: # for each line in geocode file 
            b = line.strip() #strips the /n from the end of the line
            [lst.append(b.split('-'))] #strips the - and adds the row to a list
    return lst

    '''Create a loop to create a list of URL's to query against NMP split across multiple files, since NMP will timeout after apprx 5K rows'''

def write_nmpURL (lst):
    with open('c:/pyfund/geocodes_URL_1.txt', mode='wt',encoding='utf-8') as urlfile:  #open a new text file 
        for list in islice(lst,0,5000): # for each list in the lst, '\' used to escape ' 
            print ("https://nmp.services.skypeforbusiness.com/proxy/tnm/api/v1/Regions(\'{}\')/Countries(\'{}\')/Areas(\'{}\')/Cities(\'{}\')".format(*list), file = urlfile) # unpack the list and use string formating to create each url  

    with open('c:/pyfund/geocodes_URL_2.txt', mode='wt',encoding='utf-8') as urlfile:  #open a new text file 
            for list in islice(lst,5001,10000): # for each list in the lst, '\' used to escape ' 
                print ("https://nmp.services.skypeforbusiness.com/proxy/tnm/api/v1/Regions(\'{}\')/Countries(\'{}\')/Areas(\'{}\')/Cities(\'{}\')".format(*list), file = urlfile) # unpack the list and use string formating to create each url  

    with open('c:/pyfund/geocodes_URL_3.txt', mode='wt',encoding='utf-8') as urlfile:  #open a new text file 
            for list in islice(lst,10001,15000): # for each list in the lst, '\' used to escape ' 
                print ("https://nmp.services.skypeforbusiness.com/proxy/tnm/api/v1/Regions(\'{}\')/Countries(\'{}\')/Areas(\'{}\')/Cities(\'{}\')".format(*list), file = urlfile) # unpack the list and use string formating to create each url  

    ''' Create a function so the main function can be tested from repl'''
def main(filename):
    geocodes = GeoList(filename)
    write_nmpURL(geocodes)

''' Enables code to be ran as a python script'''
if __name__ == '__main__':
    main(sys.argv[1])