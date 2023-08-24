import subprocess

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
    print("1.Operation all Text Details ")
    print("2.Upper case Letter,Count(uc) ")
    print("3.Lower case Letter,Count(lc) ")
    print("4.Number,Count(nc) ")
    print("5.Symbol,Count(sc) ")
    print("6.Exit(x)")

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



while ch!="exit":
    print("__________________________________")
    print("        List Of Files in Dir      ")
    print("__________________________________")
    listfile=subprocess.run(["ls"])
    print(listfile.returncode)
    print("__________________________________")
    file=input()
    mode=input()
    f=open(file,mode)
    bannerList()
    ch=input()
    if ch=="exit":
        exit(0)
    elif ch=="1" or ch=="all":
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

