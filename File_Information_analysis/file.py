import subprocess
import os
f=""
lowletter=""
upletter=""
number=""
symbol=""
space=""
ch=""

def uppercount():
    global upletter
    print("Upper case in Txt:",upletter,"\nCount of Upper case:",len(upletter))
def lowercount():
    global lowletter
    print("Lower case in Txt:",lowletter,"\nCount of Lower case:",len(lowletter))
def Number():
    print("Number in the Txt",number,"\nCount of Number:",len(number))
def Space():
    print("Count of space:",len(space))
def Symbol():
     print("Symbols int Txt",symbol,"\nCount of Symbol",len(symbol))

def display():
    uppercount()
    lowercount()
    Number()
    Space()
    Symbol()   
    

def bannerList():
    print("---------------------------Opreation in TxT File----------------------------")
    print("1.Modifiy File Text File")
    print("2.Operation all Text Details ")
    print("3.Upper case Letter,Count(uc) ")
    print("4.Lower case Letter,Count(lc) ")
    print("5.Number,Count(nc) ")
    print("6.Symbol,Count(sc) ")
    print("7.Exit(x)")


def opeartionText():
   
    global lowletter
    global upletter
    global number
    global symbol
    global space
    global f  
    
    for x in f:
        i=0
        while len(x)!=i:
            if x[i].isalpha():
                if x[i].isupper():
                    upletter=upletter+x[i]
                else :
                    lowletter=lowletter+x[i]
            elif x[i].isalnum():
                number=number+x[i]
            elif x[i].isspace():
                space=space+x[i]
            else:
                symbol=symbol+x[i]
            i+=1

def chocie():
    print("---------------Dir Info------------")
    print("------------------------------------")
    print("1.View of File(v or view)")
    print("2.Path of current File (path or p)")

    


while ch!="exit":
    print("__________________________________")
    print("        List Of Files in Dir      ")
    print("__________________________________")
    listfile=subprocess.run(["ls"])
    print(listfile.returncode)
    print("__________________________________")
    print("Commond are ->\n1.dir(to basic operation like(cat,pwd))\n2.file(Operation of file)")
    ch=input()
    if ch=="dir":
        chocie()
        cf=input()
        if cf=="view" or cf=="v":
            print("File Name to Perview:",end="")
            fif=input()
            os.system("cat "+fif)
        elif cf=="path" or cf=="p":
            os.system("pwd")
        
    elif ch=="file":
        print("Type File Name:",end="")
        file=input()
        
        f=open(file)
        bannerList()
        ch=input()
        if ch=="exit":
            exit(0)
        elif ch=="modifiy" or ch=="m":
            subprocess.run(["xdg-open",file])
        elif ch=="a" or ch=="all":
            opeartionText()
            display()
        elif ch=="uc" or ch=="upcount":
            uppercount()
        elif ch=="lc" or ch=="locount":
            lowercount()
        elif ch=="nc":
            Number()
        elif ch=="sc":
            Symbol()

