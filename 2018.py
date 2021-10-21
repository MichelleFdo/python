L = input("Enter List Of Numbers :")
Num_List =[int(i) for i in L.split()]
K=int(input("Enter K as number to search :"))
N=len(Num_List)
i=0
while(i<N):
    if (Num_List[i]==K):
        print("True")
        break
    i=i+1
if(not (i<N)):
    print("False")
