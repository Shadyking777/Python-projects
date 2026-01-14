#How do you define a class

class Player():
    #PRIVATE name : STRING
    #PRIVATE age : INTEGER

    
    #You should make a constructor
    def __init__(self, nameuser, ageuser):
        self.__name = nameuser
        self.__age = ageuser
    
    # Methods
    def Getage(self):
        return self.__age

    def Displayname(self):
        return self.__name
    
    # Setter
    # If you want to change your private
    # attributes then use setter
    
    # if you want to just access private 
    # attributes then use getter

    def SetName(self, NewName):
        self.__name = NewName
        # P2.__name = "Bano Taha"

#Making Objects By Using Class

P1 = Player("Ghost", 21)
P2 = Player("Ninja", 19)


print("Before", P2.Displayname())
P2.SetName("Bano Taha")
print("After", P2.Displayname())

# Constructor is linked with object creation
