str=input("dou you want to start---___------____---")
for new in range(500):
    if str=="yes":
        n=int(input("enter number for turn it binery=  "))
        a=[]
        while(n>0):
            z=n%2
            a.append(z)
            n=n//2
        
        a.reverse()
        for i in a:
            print(i,end=" ")
    else:
         print("ok go from here 😅 ")   
 
