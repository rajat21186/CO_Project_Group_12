with open("C:\Users\DeLL\OneDrive\Desktop\test1.txt","r") as f:
    A = f.readlines()
    B = [i.strip() for i in A]
for i in B:
    i = i.split()
