import requests
from bs4 import BeautifulSoup
wensite_name=""
r=""
suop=""
#It will send requset to the website and retrun respose with data of the site 

def structre_of_site():
#parser object to get the data form the site
    global wensite_name
    global r
    global suop
#prettify print with indentaion
    
    print("Do you want to save:(y OR n)")
    
    ch=input()
    if ch=="y":
        print("File to Save:",end="")
        file=input()
        fi=open(file,"w+")
        fi.write(str(suop))
             
    print(suop.prettify())        
    

def Linktag():
    global wensite_name
    global r
    global suop
    for link in suop.find_all('a'):
        print(link.get('href'))

def imgtag():
    global wensite_name
    global r
    global suop
    images_list = []
    images = suop.select('img')
    for image in images:
        src = image.get('src')
        images_list.append(src)
    
    for image in images_list:
        print(image)
    print("No.of.Photos in:",wensite_name,"---->",len(images_list))

def banner():
    print('''
░
░██╗░░░░░░░██╗███████╗██████╗░  ░██████╗░█████╗░██████╗░░█████╗░██████╗░██╗███╗░░██╗░██████╗░
░██║░░██╗░░██║██╔════╝██╔══██╗  ██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗██║████╗░██║██╔════╝░
░╚██╗████╗██╔╝█████╗░░██████╦╝  ╚█████╗░██║░░╚═╝██████╔╝███████║██████╔╝██║██╔██╗██║██║░░██╗░
░░████╔═████║░██╔══╝░░██╔══██╗  ░╚═══██╗██║░░██╗██╔══██╗██╔══██║██╔═══╝░██║██║╚████║██║░░╚██╗
░░╚██╔╝░╚██╔╝░███████╗██████╦╝  ██████╔╝╚█████╔╝██║░░██║██║░░██║██║░░░░░██║██║░╚███║╚██████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░  ╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░░░░╚═╝╚═╝░░╚══╝░╚═════╝░╗
░░░╚═╝░░░░╚════╝░░╚════╝░╚══════╝''')
    print("                                                               By")
    print("                                                                  Sudhakar")
    
def menu():
    print("-------------------------------------Menu----------------------------------------")
    print("1.Html page code Extraction")
    print("2.Link tag Extraction")
    print("3.Img tag Extraction")
    print("4.Exit")


banner()
print("\n")
wensite_name=input("Site Name:")
r=requests.get(wensite_name)
suop=BeautifulSoup(r.content,"html.parser")
#response of the site status
print("Response of the Site Status:",r)
a=False
while a!=True:
    menu()
    s=int(input())
    if s==1:
        structre_of_site()
    elif s==2:
        Linktag()
    elif s==3:
        imgtag()
    elif s>3:
        print("Exit....")
        a=True

