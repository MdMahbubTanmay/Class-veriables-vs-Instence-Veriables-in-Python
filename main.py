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
