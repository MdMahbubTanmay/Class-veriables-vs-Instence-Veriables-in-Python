class Main:
    health = None
    def __init__(self):
        self.Num = None

    

x = Main()

#Class can change Class variables like health but not instence variable like Num here
Main.Num=66 #No effect
Main.health = 100  #Has Effect

print(x.Num,x.health) #None 100

print(Main.Num,Main.health) #66 100


#Object Modifier can change its own Class variables like health that is belongs to  x object here and instence verible like Num 
# but not Global Class Variable like health that belongs to everyone
x.health = 99
x.Num = 9

print(x.Num,x.health) #9 99

print(Main.Num,Main.health) #66 100 (same as line 16)






#************ So The question is is there any way using which we can change class global variable
# without using class like Main.health = 7575  with using instance like x.health = 7575?
#The answer is yes. 



class Main2:
        health = None

        def GlobalChange(self,h): # it will change k.health value not global health value
             self.health = h

        @classmethod #Now it will change global health value but it will have no effect on instance like x.health 
        def GlobalChange2(self,h): 
             self.health = h


k = Main2()
k.health = 33

print(k.health) #Changed
print(Main2.health) #Unchanged




k.GlobalChange(6969)
print(k.health) #Changed
print(Main2.health) #Unchanged


#Lets try that @classmethod
k.GlobalChange2(7575)
print(k.health) # Unchanged
print(Main2.health) # Changed
