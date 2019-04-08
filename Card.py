
acc_name=("C","D","H","S","@")
class Card:
    Suit=acc_name[4]
    Num=(-1)
    pass
     
    def __init__(self, inn):
        if (inn>=0 and inn<=51):
            self.Suit=acc_name[inn%4]
            self.Num=1+ inn//4
        else:
            pass
        
    def __str__(self):
        return f"{self.Num}{self.Suit}"
    
    @classmethod
    def defCard(cls):
        return cls(13)





C1=Card(0)
print (C1.Num)
print (C1.Suit)
print (C1)

C2=Card(18)
print (C2.Num)
print (C2.Suit)
print (C2)
    
C3=Card.defCard()
print(C3)
    

    
  

