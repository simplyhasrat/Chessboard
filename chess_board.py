i=1
k=0
while i<=64:
    if i%9==0 or i%25==0 or i%41==0 or i%57==0:
       for j in range(8):
           if j%2==0:
               print("■", end=" ")
           else:
               print("□",end=" ")
           i+=1
    
      
    else:
       for j in range(8):
            if j%2==0:
                print("□",end=" ")
            else:
                print("■",end=" ")
            i+=1
    print()
    