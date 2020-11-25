#UPDATED PROJECT SCRIPT

import requests
from bs4 import BeautifulSoup

def scrape():
    url ="https://en.wikipedia.org/wiki/COVID-19_pandemic_cases"

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    table = soup.findAll('tr')
#     new_table = table[31:-46]
    
    data = [list(item.stripped_strings) for item in table[31:-46]]
    world = [list(item.stripped_strings) for item in table[28:29]]
    
    for lst in data:
        for i,item in enumerate(lst[2:]):
            if type(item) == str:
                lst[i+2] = int(item.replace(",", ''))
                
    for lst in world:
        for i,item in enumerate(lst[1:]):
            if type(item) == str:
                lst[i+1] = int(item.replace(",", ''))
                
    lst_world = [num for item in world for num in item]
                
    latin_america = ["USA","Belize", "Costa Rica", "El Salvador", "Guatemala", "Honduras", "Mexico", "Nicaragua", "Panama",
                    "Argentina", "Bolivia", "Brazil", "Chile", "Colombia", "Ecuador", "French Guiana", "Guyana", 
                     "Paraguay", "Peru", "Suriname", "Uruguay", "Venezuela"]
    
    americas_data = [lst for lst in data if lst[0] in latin_america]

    #PERCENTAGE OF COVID-19 CASES IN LATIN AMERICAN INCLUDING USA COMPARED TO THE REST OF THE WORLD
    for lst in americas_data:
        for i,num in enumerate(lst[2:]):
            lst[i+2]= round((num / lst_world[i+1]) * 100, 2)
    print(americas_data)       
    return americas_data
    
# if __name__ == '__main__':
    scrape()