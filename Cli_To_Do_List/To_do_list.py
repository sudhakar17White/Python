import sys
def help():
    s="1.Show Do List\n2.Add DO To List\n3.Delete Do To List\n4.Exit"
    print(s)

ch=""

def showList():
    print("\n")
    fi=open('do_list.txt','r')
    i=1
    print("To Do List Are :")
    for x in fi:
        print(i,") ",x)
        i+=1
    
    fi.close()
    print("\n")

def addList(s):
    print(s)
    fi=open('do_list.txt','a')
    fi.write(s)
    fi.write("\n")
    
def deleteList(dele):
    print(dele)
    i=0
    di=[]
    fi=open('do_list.txt','r')
    for x in fi: 
        if dele!=i:
            di.append(x)
        i+=1
    print(di)
    fi=open('do_list.txt','a')
    j=0
    for x in fi:
        fi.write(di[j])
        j+=1
    fi.close()




while ch!="exit":
    help()
    ch=input()
    if ch=="1" or ch =="show":
        showList()
    elif ch=="2" or ch=="add":
        addList(input("New To Do List:"))
    elif ch=="3" or ch=="del":
        dele=int(input())
        deleteList(dele)

 