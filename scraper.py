import sys
import requests
from bs4 import BeautifulSoup
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
YELLOW = '\033[33m'
BLUE = '\033[34m'
MAGENTA = '\033[35m'
CYAN = '\033[36m'
WHITE = '\033[37m'
RESET = '\033[0m' 
def scrape(url,iid=0,given_tag=0):
    global RED,RESET
    if iid==0 and given_tag!=0:
        print(f"getting all {given_tag} tags from {url}\n")
    elif iid!=0 and given_tag==0:
        print(f"finding {iid}")
    elif iid==0 and given_tag==0:
        print(f"getting all content of {url}\n")
    try:
    
        responce=requests.get(url)
        
        
        
        if responce.status_code==200:
            soup=BeautifulSoup(responce.content,"html.parser")
            if iid ==0 and given_tag!=0:
                tags=soup.find_all(given_tag)
                i=1
                for tag in tags:
                    print(f"({i}). tag: {tag}\n")
                    print(f"id: {tag.get('id')}\n")
                    print(f"text: {tag.text}\n")
                
                    i+=1
            elif iid!=0 and given_tag==0:
                tag=soup.find_all(id=iid)
                print(tag)
            elif iid==0 and given_tag==0:
                print(responce.content.decode())
        else:
            print(RED+f"can not connent to {url}"+RESET)
    except Exception as e:
        print(RED+str(e)+RESET)

    
        
        


args=sys.argv[1:]

if len(args)==1:
    scrape(url=args[0])

elif len(args)==2:

    scrape(url=args[0],given_tag=args[1])
elif len(args)==3 and args[1]=='id':

    scrape(iid=args[2],url=args[0])
else:
    print(RED+"enter all arguments"+RESET)


