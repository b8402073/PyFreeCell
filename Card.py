#http://yltang.net/tutorial/python/7/

acc_name=("C","D","H","S","@")
class Card:
    Suit=acc_name[4]
    Num=(-1)
    ID=(-1)
    pass
     
    def __init__(self, inn):
        if (inn>=0 and inn<=51):
            self.ID=inn
            self.Suit=acc_name[inn%4]
            self.Num=1+ inn//4
        else:
            pass
        
    def __str__(self):
        if (self!=None):
            return f"{self.Num}{self.Suit}"
        else:
            return"none"

    def __getitem__(self,index):
        if (self==None) : return 10000
        if (index==0): return self.ID
        elif (index==1): return self.Num
        else: return self.Suit


    @classmethod
    def defCard(cls):
        return cls(13)
    

class Buffer:
    Hand=[None,None,None,None]
    SZ=0    
    def __init(self):
        pass
    
    def add(self,that)->bool:
        if (self.SZ<4):
            self.Hand[self.SZ]=that
            self.SZ+=1
            self.sort()
            return True
        return False
    def get(self,index)->Card:
        return self.Hand[self.index]
    def __str__(self):
        return f"Buffer:[{self.Hand[0]},{self.Hand[1]},{self.Hand[2]},{self.Hand[3]}]"
    def swap(self,i,j):
        (self.Hand[i], self.Hand[j]) = (self.Hand[j], self.Hand[i])
    def pop(self,thatCard)->Card:
        idx=self.Hand.index(thatCard)
        ret=self.Hand[idx]
        if (idx>=0): 
            self.Hand[idx]=None
            self.sort()
            return ret
        return None
                
    def sort(self):
        for i in range(3):
            for j in range(i+1,4):                
                if (self.Hand[i]==None and self.Hand[j]!=None):
                    self.swap(i,j)
                elif (self.Hand[i]!=None and self.Hand[j]==None):
                    continue
                if (self.Hand[i]!=None and self.Hand[j]!=None):                    
                    if (self.Hand[i].Num > self.Hand[j].Num):
                        self.swap(i,j)
                    elif (self.Hand[i].Num == self.Hand[j].Num):
                        if (acc_name.index(self.Hand[i]) > acc_name.index(self.Hand[j])):
                            self.swap(i,j)
    
              
        
print("-------------------------")
C1=Card(50)
print ("C1=",C1)

C2=Card(30)
print ("C2=",C2)
    
C3=Card.defCard()
print("C3=",C3)
    
B=Buffer()
print(B)
B.add(C3)    
print(B)
B.add(C2)
print(B)
B.add(C1)
print(B)
B.pop(C1)
print(B)
B.pop(C2)
print(B)
B.pop(C3)
print(B)


    
  

