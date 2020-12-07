#UPDATED PROJECT SCRIPT

import requests
from bs4 import BeautifulSoup
from app import db, Covid19

def scrape():
    url ="https://en.wikipedia.org/wiki/COVID-19_pandemic_cases"

    req = requests.get(url)
    soup = BeautifulSoup(req.text, "html.parser")
    table = soup.findAll('tr')
    
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

    #PERCENTAGE OF COVID-19 CASES IN LATIN AMERICA INCLUDING USA COMPARED TO THE REST OF THE WORLD
    for lst in americas_data:
        for i,num in enumerate(lst[2:]):
            lst[i+2]= round((num / lst_world[i+1]) * 100, 2)     
    return americas_data
    
def setup_db():
    data = scrape()
    db.drop_all()
    db.create_all()
    for lst in data:
        table = Covid19(country = lst[0], first_case_date = lst[1], jan_1 = lst[2], feb_1 = lst[3], mar_1= lst[4], 
                        apr_1 = lst[5], may_1 = lst[6], jun_1 = lst[7], jul_1 = lst[8], aug_1=lst[9], sept_1 = lst[10],
                        oct_1 = lst[11], nov_1 = lst[12])
        db.session.add(table)
        db.session.commit()

def get_all():
    query = Covid19.query.all()  
    print(query)

if __name__ == '__main__':
    scrape()
    setup_db()
    get_all()
