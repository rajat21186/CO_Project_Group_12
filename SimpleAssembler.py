#CO PROJECT Gp12
import sys
#with open("test1.txt","r") as f:
A = sys.stdin.readlines()
B = [i.rstrip() for i in A]    
    #print(B)
beg=0
for t in B:
    if(t==""):
        B.remove(t) 
    #print(B)
D=[] 
dcv=dict()
dcl=dict()
def dict():
    dcr={"R0":"000","R1":"001","R2":"010","R3":"011","R4":"100","R5":"101","R6":"110"}
    dc={"add":"10000","sub":"10001","movI":"10010","movR":"10011","ld":"10100","st":"10101","mul":"10110","div":"10111","rs":"11000","ls":"11001","xor":"11010","or":"11011","and":"11100","not":"11101","cmp":"11110","jmp":"11111","jlt":"01100","jgt":"01101","je":"01111","hlt":"01010"}
    return dc,dcr
def list():
    d=[]
    for t in range(7):
        s="R"+str(t)
        d.append(s)       
    return d
def var(B,j,beg,pc):
    c=B[j].split()
    es="line"+str(j+1)
    #print(c)
    if(beg!=0):
        sys.stdout.write("Variable not declared in the beginning")
        sys.stdout.write("\n")
        return 0,D
    elif(len(c)==2 and(c[0]!=c[1])):
        #print("Valid")
        D.append(c[1])
        return 1,D
    else:
        sys.stdout.write("Invalid syntax for variable")
        sys.stdout.write("\n")
        return 0,D
def typeA(B,j,pc): 
    c=B[j].split()
    es="line"+str(j+1)
    #print(c)
    d=list()
    x=0
    #print(d)
    dc,dcr=dict()
    for u in c:
        if u in d:
            #print(u)
            x+=1
    if(len(c)==4 and x==3):
        if(c[0]=="add"):
            k=dc["add"]
        elif(c[0]=="sub"):
            k=dc["sub"]
        elif(c[0]=="mul"):
            k=dc["mul"]
        elif(c[0]=="xor"):
            k=dc["xor"]
        elif(c[0]=="or"):
            k=dc["or"]
        elif(c[0]=="and"):
            k=dc["and"]
        s=k+"00"
        for g in c[1:]:
            if g in dcr.keys():
                k=dcr[g]
                s=s+k
        if(pc==1):
            sys.stdout.write(s)
            sys.stdout.write("\n")
        return 1
    else:
        sys.stdout.write("Invalid syntax for "+c[0])
        sys.stdout.write("\n")
        return 0
def typeB(B,j,pc):
    c=B[j].split()
    es="line"+str(j+1)
    intg=["0","1","2","3","4","5","6","7","8","9"]
    if(len(c)==3):
        p=c[2][0]
        if(p=="$"):
            st=c[2][1:]
            for e in st:
                if e not in intg:
                    sys.stdout.write("Invalid immediate value")
                    sys.stdout.write("\n")
                    return 0
            ps=bin(int(st))
            sz=ps[2:]
            if(len(str(sz))>8):
                sys.stdout.write("Size of immediate value exceeds 8 bits")
                sys.stdout.write("\n")
                return 0
            last=""
            for u in range(8-len(sz)):
                last=last+"0"
            last=last+sz
            dc,dcr=dict()
            if c[1] in dcr.keys():
                last=dcr[c[1]]+last
            else:
                sys.stdout.write("Invalid Register"+c[1])
                sys.stdout.write("\n")
                return 0
            if(c[0]=="mov"):
                last=dc["movI"]+last
            else:
                last=dc[c[0]]+last
            if(pc==1):
                sys.stdout.write(last)
                sys.stdout.write("\n")
            return 1
        else:
            if(c[0]!="mov"):
                sys.stdout.write("Invalid Syntax for "+c[0])
                sys.stdout.write("\n")
            return 0
    else:
        if(c[0]!="mov"):
            sys.stdout.write("Invalid Syntax for "+c[0])
            sys.stdout.write("\n")
        return 0

            
def typeC(B,j,pc):
    c=B[j].split()
    es="line"+str(j+1)
    dc,dcr=dict()
    s=dc[c[0]]+"00000"
    if(len(c)==3):
        if c[1] in dcr.keys():
            s=s+dcr[c[1]]
        else:
            sys.stdout.write("Invalid Register"+c[1])
            sys.stdout.write("\n")
            return 0
        if c[2] in dcr.keys():
            s=s+dcr[c[2]]
        else:
            sys.stdout.write("Invalid Register"+c[2])
            sys.stdout.write("\n")
            return 0
        if(pc==1):
            sys.stdout.write(s)
            sys.stdout.write("\n")
        return 1
    else:
        sys.stdout.write("Invalid Syntax for "+c[0])
        sys.stdout.write("\n")
        return 0

def typeD(B,j,D,pc):
    c=B[j].split()
    es="line"+str(j+1)
    dc,dcr=dict()
    st=dc[c[0]]
    if(len(c)==3):
        if c[1] in dcr.keys():
            st=st+dcr[c[1]]
        else:
            sys.stdout.write("Invalid Register "+c[1])
            sys.stdout.write("\n")
            return 0
        if c[2] in D:

            return 1
        else:
            sys.stdout.write("Invalid Variable "+c[2])# sys.stdout.write(es)
            sys.stdout.write("\n")
            return 0
    else:
        sys.stdout.write("Invalid Syntax for "+c[0])
        sys.stdout.write("\n")
        return 0
def dp(B,j,dcv):
    dc,dcr=dict()
    c=B[j].split()
    q = dcv[c[2]]
    S = ""
    for v in range(8-len(q)):
        S = S + "0"
    S = S + q
    st = dc[c[0]] + dcr[c[1]] + S
    sys.stdout.write(st)
    sys.stdout.write("\n")
    return 1
def typeE(B,j,D,pc,dcl):
    c=B[j].split()
    es="line"+str(j+1)
    dc,dcr=dict()
    st=dc[c[0]]+"000" 
    #print(dcl)
    #print(c[1])
    if(len(c)==2):
        if c[1] in dcl.keys():
            return 1
        else:
            sys.stdout.write("Mentioned label not defined ")
            sys.stdout.write("\n")
            return 0
def ef(B,j,dcv,dcl):
    dc,dcr=dict()
    c=B[j].split()
    q = dcl[c[1]]
    S = ""
    for v in range(8-len(q)):
        S = S + "0"
    S = S + q
    st=dc[c[0]]+"000"
    st = st + S
    sys.stdout.write(st)
    sys.stdout.write("\n")
    return 1

def typeF(B,j,D,pc):
    c=B[j].split()
    es="line"+str(j+1)
    dc,dcr=dict()
    st=dc[c[0]]
    if(len(c)==1):
        if(pc==1):
            st=st+"00000000000"
            sys.stdout.write(st)
            sys.stdout.write("\n")
        return 1
    else:
        sys.stdout.write("Invalid syntax for hlt")
        sys.stdout.write("\n")
        return 0
def movR(B,j,D,pc):
    #print(pc)
    c=B[j].split()
    es="line"+str(j+1)
    dc,dcr=dict()
    st = dc["movR"] + "00000"
    #print(c[1])
    if c[1] in dcr:
        st = st + dcr[c[1]]
    elif c[1]=="FLAGS":
        st=st+"111"
        #print(st)
    else:
        sys.stdout.write("Invalid Register "+c[1])
        sys.stdout.write("\n")
        return 0
    if c[2] in dcr:
        st = st + dcr[c[2]]
        #print("C1")
        #print(pc)
        if(pc == 1):
            #print("C2")
            sys.stdout.write(st)
            sys.stdout.write("\n")
            
        return 1
    else:
        sys.stdout.write("Invalid Register "+c[1])
        sys.stdout.write("\n")
        return 0
r=0
d = list()
linch=0
#print(B)
for j in range(len(B)):
    lp = 0
    #k = B[j]
    # R = 0
    # for m in range(len(k) - 1):
    #     if(k[m] == " " and k[m+1] == " "):
    #         sys.stdout.write("line" + str(j + 1))
    #         sys.stdout.write("\n")
    #         R = 1
            
    #         break

    # if(R == 1):
    #     r = 0
    #     break
    y=B[j].split()
    #sys.stdout.write(str(j))
    #sys.stdout.write("\n")
    #print(y)
    pc=0
    ch=0
    lc = y[0][-1]
    cl = 0
    if(len(y)==0):
        r=1
        ch=1
    elif(y[0]=="var"):
        r,D=var(B,j,beg,pc)
        #print(D)
    elif(y[0]=="add" or y[0]=="sub" or y[0]=="mul" or y[0]=="xor" or y[0]=="or" or y[0]=="and"):
        r=typeA(B,j,pc)
        beg+=1
    elif(y[0]=="mov" or y[0]=="ls" or y[0]=="rs"):
        r=typeB(B,j,pc)
        beg+=1
    elif(y[0]=="div" or y[0]=="not" or y[0]=="cmp"):
        r=typeC(B,j,pc)
        beg+=1
    elif(y[0]=="ld" or y[0]=="st"):
        r=typeD(B,j,D,pc)
        beg+=1
    elif(y[0]=="jmp" or y[0]=="jlt" or y[0]=="jgt" or y[0]=="je"):
        r=typeE(B,j,D,pc,dcl)
        beg+=1
    elif(y[0]=="hlt"):
        if(j!=len(B)-1):
            sys.stdout.write("hlt not at last line")
            sys.stdout.write("\n")
            sys.stdout.write("line"+str(j+1))
            sys.stdout.write("\n")
            r=0
            break
        r=typeF(B,j,D,pc)
    elif(lc == ":" and cl == 0):
        a = len(y[0])
        lst=y.pop(0)
        sr = ""
        p = 0
        #print(y)
        while(p < len(y) - 1):
            sr = sr + y[p] + " "
            p += 1
        if (p > 0):

            sr = sr + y[p]
        if(len(y) == 1 and y[0] == "hlt"):
            sr = sr + "hlt"
        
        B[j] = sr
        fn = 0
        for t in B:
            if(t==""):
                sys.stdout.write("line" + str(j + 1))
                sys.stdout.write("\n")
                r = 0
                fn = 1

                break
                #B.remove(t)
        if (fn == 1):
            break    

        #print(B)
        cl = 1
        z = B[j].split()
        if(len(z) == 1 and z[0] != "hlt"):
            r = 0
            sys.stdout.write("line"+str(j + 1))
            sys.stdout.write("\n")
        else:
            if(len(z)==0):
                r=1
                ch=1
            elif(z[0]=="var"):
                r,D=var(B,j,beg,pc)
                #print(D)
            elif(z[0]=="add" or z[0]=="sub" or z[0]=="mul" or z[0]=="xor" or z[0]=="or" or z[0]=="and"):
                r=typeA(B,j,pc)
                beg+=1
            elif(z[0]=="mov" or z[0]=="ls" or z[0]=="rs"):
                r=typeB(B,j,pc)
                beg+=1
            elif(z[0]=="div" or z[0]=="not" or z[0]=="cmp"):
                r=typeC(B,j,pc)
                beg+=1
            elif(z[0]=="ld" or z[0]=="st"):
                r=typeD(B,j,D,pc)
                beg+=1
            elif(z[0]=="jmp" or z[0]=="jlt" or z[0]=="jgt" or z[0]=="je"):
                r=typeE(B,j,D,pc)
                beg+=1
            elif(z[0]=="hlt"):
                r=typeF(B,j,D,pc)
            elif(len(y) == 3 and y[0] == "mov" and (y[1] in d) and (y[2] in d) ):
                r = movR(B,j,D,pc)
    
            else:
                r = 0
            if(len(y) == 3 and y[0] == "mov" and  (y[1] in d) and (y[2] in d)):
                r = movR(B,j,D,pc)
            lp  = 1    
            if(r == 0):
                sys.stdout.write("line" + str(j + 1))
                sys.stdout.write("\n")
            else:
                cl=""
                for yz in range(len(lst)-1):
                    cl=cl+lst[yz]
                #print(cl)
                dcl[cl]=str(bin(j+1)[2:])
                if cl in D:
                    sys.stdout.write("Invalid name of Label")
                    sys.stdout.write("\n")
                    sys.stdout.write("line" + str(j + 1))
                    sys.stdout.write("\n")
                    r=0
                    break

    else:
        r = 0 

    if(len(y) == 3 and y[0] == "mov" and (y[1] in d or y[1]=="FLAGS") and (y[2] in d)):
        r = movR(B,j,D,pc)
    if(j == len(B) - 1 and r == 1):
        if(y[0] != "hlt"):
            sys.stdout.write("hlt missing")
            sys.stdout.write("\n")
            r = 0
            break
    if(r == 0 and lp == 0):
        sys.stdout.write("line" + str(j + 1))
        sys.stdout.write("\n")
        
    if(r==0):
        break
    #print(linch)
    #print(B[linch-1])
    if(linch==256 and B[linch-1]!="hlt"):
        sys.stdout.write("code limit exceed")
        sys.stdout.write("\n")
        r=0
        break
    linch+=1
if(r==1):
    xy = list()

    d=len(D)
    b=len(B)
    ins=(b-d)
    for g in D:
        jns=str(bin(ins))
        dcv[g]=jns[2:]
        ins+=1
    pc=1
    beg=0
    for j in range(len(B)):
        y=B[j].split()
        lc = y[0][-1]
    
        #print(y)
        if(len(y) == 3 and y[0] == "mov" and  (y[1] in xy or y[1]=="FLAGS") and (y[2] in xy)):
            r = movR(B,j,D,pc)
        elif(len(y)==0):
            r=1
            ch=1
        elif(y[0]=="var"):
            r,D=var(B,j,beg,pc)
            #print(D)
        elif(y[0]=="add" or y[0]=="sub" or y[0]=="mul" or y[0]=="xor" or y[0]=="or" or y[0]=="and"):
            r=typeA(B,j,pc)
        elif(y[0]=="mov" or y[0]=="ls" or y[0]=="rs"):
            r=typeB(B,j,pc)
        elif(y[0]=="div" or y[0]=="not" or y[0]=="cmp"):
            r=typeC(B,j,pc)
        elif(y[0]=="ld" or y[0]=="st"):
            r=dp(B,j,dcv)
        elif(y[0]=="jmp" or y[0]=="jlt" or y[0]=="jgt" or y[0]=="je"):
            r=ef(B,j,dcv,dcl)
        elif(y[0]=="hlt"):
            r=typeF(B,j,D,pc)
        # elif(len(y) == 3 and y[0] == "mov" and  (y[1] in d or y[1]=="FLAGS") and (y[2] in d)):
        #     print(pc)
        #     r = movR(B,j,D,pc)
        
        
        # elif(lc == ":"):
        #     a = len(y[0])
            
        #     y.pop(0)
        #     sr = ""
        #     p = 0
        #     for p in range(len(y) - 1):
        #         sr = sr + y[p] + " "
        #     sr = sr + y[p]
        #     B[j] = sr
        #     z = B[j].split()
        #     if(len(z)==0):
        #         r=1
        #         ch=1
        #     elif(z[0]=="var"):
        #         r,D=var(B,j,beg,pc)
        #         #print(D)
        #     elif(z[0]=="add" or z[0]=="sub" or z[0]=="mul" or z[0]=="xor" or z[0]=="or" or z[0]=="and"):
        #         r=typeA(B,j,pc)
        #         beg+=1
        #     elif(z[0]=="mov" or z[0]=="ls"):
        #         r=typeB(B,j,pc)
        #         beg+=1
        #     elif(z[0]=="div" or z[0]=="not" or z[0]=="cmp"):
        #         r=typeC(B,j,pc)
        #         beg+=1
        #     elif(z[0]=="ld" or z[0]=="st"):
        #         r=typeD(B,j,D,pc)
        #         beg+=1
        #     elif(z[0]=="jmp" or z[0]=="jlt" or z[0]=="jgt" or z[0]=="je"):
        #         r=typeE(B,j,D,pc)
        #         beg+=1
        #     elif(z[0]=="hlt"):
        #         r=typeF(B,j,D,pc)
                
                
        
        
            

        
            



        
            

        
            

            
