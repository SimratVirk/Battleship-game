#!/usr/bin/python3
import sys
import numpy as np
import random
import copy

ships=np.empty(shape=(10,10),dtype=str)
grids=np.empty(shape=(10,10),dtype=str)
opponent=[]
my_ships=[]
locate_ship_C1=[]
C1=[]
locate_ship_C2=[]
C2=[]
locate_ship_B1=[]
B1=[]
locate_ship_B2=[]
B2=[]
locate_ship_K1=[]
K1=[]
locate_ship_K2=[]
K2=[]
locate_ship_S1=[]
S1=[]
locate_ship_S2=[]
S2=[]
locate_ship_D1=[]
D1=[]
locate_ship_D2=[]
D2=[]
C="Carrier"
B="Battleship"
K="Cruiser"
S="Submarine"
D="Destroyer"

def drawguesses():
    print("Your Guesses")
    print("   ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J']")
    for x in range(10):
        print(x," ",end="")
        print(grids[x],sep=",")
        
def drawboard():
    print("Your Ships")
    print("   ['A' 'B' 'C' 'D' 'E' 'F' 'G' 'H' 'I' 'J']")
    for x in range(10):
        print(x," ",end="")
        print(my_ships[x],sep=",")



def opponent_ships(n,char):
    z=random.randint(0,1)
    if z==0:
        x=random.randint(0,9)
        y=random.randint(0,9-n)
    else:
        x=random.randint(0,9-n)
        y=random.randint(0,9)
    while not_allowed(n, x, y, z):
        if z==0:
            x=random.randint(0,9)
            y=random.randint(0,9-n)
        else:
            x=random.randint(0,9-n)
            y=random.randint(0,9)
    opponent_board(n, x, y, z,char)
            


def opponent_board(n, x, y, z,char):
    if z == 0:
        for i in range(y,y+n):
            opponent[x][i]=char
            

    if z == 1:
        for i in range(x,x+n):
            opponent[i][y]=char
   
            

def not_allowed(n, x, y, z):
    boolean=True
    if z == 0:
        if (y+n) < 10:
            for i in range(y,y+n):
                if opponent[x][i]=="-":
                    boolean*=True
                else:
                    boolean*=False
        else:
            boolean*=False
            
    elif z == 1:
        if (x+n) < 10:
            for i in range(x,x+n):
                if opponent[i][y]=="-":
                    boolean*=True
                else:
                    boolean*=False
        else:
            boolean*=False
    if boolean==1:
        return False
    else:
        return True
    
    
        
        
def moves(p):
    if len(p)>0 and p[0].isalpha() and p[1].isdigit and int(p[1])>=0 and int(p[1])<=9 and ord(p[0])-65>=0 and ord(p[0])-65<=9:
        y=ord(p[0])-65
        x=int(p[1])
        if opponent[x][y]=="C" or opponent[x][y]=="B" or opponent[x][y]=="K" or opponent[x][y]=="S" or opponent[x][y]=="D":
            grids[x][y]="H"
            ship_wreck_C1()
            ship_wreck_B1()
            ship_wreck_K1()
            ship_wreck_S1()
            ship_wreck_D1()
        elif opponent[x][y]=="-":
            grids[x][y]="X"
    else:
        x=random.randint(0,9)
        y=random.randint(0,9)
        while grids[x][y]=="H" or grids[x][y]=="X":
            x=random.randint(0,9)
            y=random.randint(0,9)
        if opponent[x][y]=="C" or opponent[x][y]=="B" or opponent[x][y]=="K" or opponent[x][y]=="S" or opponent[x][y]=="D":
            grids[x][y]="H"
            ship_wreck_C1()
            ship_wreck_B1()
            ship_wreck_K1()
            ship_wreck_S1()
            ship_wreck_D1()
        elif opponent[x][y]=="-":
            grids[x][y]="X"
    drawguesses()
        
    
    
    
def ai_move():
    x=random.randint(0,9)
    y=random.randint(0,9)
    while my_ships[x][y]=="H" or my_ships[x][y]=="X":
        x=random.randint(0,9)
        y=random.randint(0,9)
    if ships[x][y]=="C" or ships[x][y]=="B" or ships[x][y]=="K" or ships[x][y]=="S" or ships[x][y]=="D":
        my_ships[x][y]="H"
        ship_wreck_C2()
        ship_wreck_B2()
        ship_wreck_K2()
        ship_wreck_S2()
        ship_wreck_D2()
    elif ships[x][y]=="-":
        my_ships[x][y]="X"
    drawboard()
        
def f_locate_ship_C1():
    x = np.where(opponent == "C")
    for j in range(len(x[0])):
        locate_ship_C1.append(chr(x[1][j]+65)+str(x[0][j]))
        
        
def ship_wreck_C1():
    string=""
    boolean=True
    x = np.where(grids == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_C1:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(C1)<1:
        print("You wreck my "+C)
        C1.append(1)

def f_locate_ship_C2():
    x = np.where(ships == "C")
    for j in range(len(x[0])):
        locate_ship_C2.append(chr(x[1][j]+65)+str(x[0][j]))
        
        
def ship_wreck_C2():
    string=""
    boolean=True
    x = np.where(my_ships == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_C2:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(C2)<1:
        print("You lost your "+C)
        C2.append(1)
        
def f_locate_ship_B1():
    x = np.where(opponent == "B")
    for j in range(len(x[0])):
        locate_ship_B1.append(chr(x[1][j]+65)+str(x[0][j]))
        
        
def ship_wreck_B1():
    string=""
    boolean=True
    x = np.where(grids == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_B1:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(B1)<1:
        print("You wreck my "+B)
        B1.append(1)
        
        
def f_locate_ship_B2():
    x = np.where(ships == "B")
    for j in range(len(x[0])):
        locate_ship_B2.append(chr(x[1][j]+65)+str(x[0][j]))
        
        
def ship_wreck_B2():
    string=""
    boolean=True
    x = np.where(my_ships == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_B2:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(B2)<1:
        B2.append(1)
        print("You lost your "+B)

def ship_wreck_K1():
    string=""
    boolean=True
    x = np.where(grids == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_K1:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(K1)<1:
        print("You wreck my "+K)
        K1.append(1)

def f_locate_ship_K1():
    x = np.where(opponent == "K")
    for j in range(len(x[0])):
        locate_ship_K1.append(chr(x[1][j]+65)+str(x[0][j]))
        
        
def f_locate_ship_K2():
    x = np.where(ships == "K")
    for j in range(len(x[0])):
        locate_ship_K2.append(chr(x[1][j]+65)+str(x[0][j]))
        
        
def ship_wreck_K2():
    string=""
    boolean=True
    x = np.where(my_ships == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_K2:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(K2)<1:
        K2.append(1)
        print("You lost your "+K)
        
        
def f_locate_ship_S1():
    x = np.where(opponent == "S")
    for j in range(len(x[0])):
        locate_ship_S1.append(chr(x[1][j]+65)+str(x[0][j]))
        
def ship_wreck_S1():
    string=""
    boolean=True
    x = np.where(grids == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_S1:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(S1)<1:
        print("You wreck my "+S)
        S1.append(1)

def f_locate_ship_S2():
    x = np.where(ships == "S")
    for j in range(len(x[0])):
        locate_ship_S2.append(chr(x[1][j]+65)+str(x[0][j]))
        
        
def ship_wreck_S2():
    string=""
    boolean=True
    x = np.where(my_ships == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_S2:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(S2)<1:
        S2.append(1)
        print("You lost your "+S)
        
def f_locate_ship_D1():
    x = np.where(opponent == "D")
    for j in range(len(x[0])):
        locate_ship_D1.append(chr(x[1][j]+65)+str(x[0][j]))
        
def ship_wreck_D1():
    string=""
    boolean=True
    x = np.where(grids == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_D1:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(D1)<1:
        D1.append(1)
        print("You wreck my "+D)

def f_locate_ship_D2():
    x = np.where(ships == "D")
    for j in range(len(x[0])):
        locate_ship_D2.append(chr(x[1][j]+65)+str(x[0][j]))
        
        
def ship_wreck_D2():
    string=""
    boolean=True
    x = np.where(my_ships == "H")
    for j in range(len(x[0])):
        string+=chr(x[1][j]+65)+str(x[0][j])+" "
    for x in locate_ship_D2:
        if x in string:
            boolean*=True
        else:
            boolean*=False
    if boolean==1 and len(D2)<1:
        D2.append(1)
        print("You lost your "+D)
    
        
        
        
def win():
    if np.count_nonzero(grids == "H")==17:
        print("You win")
        return False
    elif np.count_nonzero(my_ships == "H")==17:
        print("You lose")
        return False
    else:
        return True
        
    
    
    
    

if __name__ == "__main__" :
    file_name=sys.argv[1]
    string=open(file_name+".dat").read().replace(" ","").replace("\n","")
    for x in range(10):
        for y in range(10):
            grids[x][y]="-"
            ships[x][y]=string[x*10+y]
    opponent = copy.deepcopy(grids)
    my_ships = copy.deepcopy(ships)
    drawboard()
    drawguesses()
    opponent_ships(5,"C")
    opponent_ships(4,"B")
    opponent_ships(3,"K")
    opponent_ships(3,"S")
    opponent_ships(2,"D")
    f_locate_ship_C1()
    f_locate_ship_C2()
    f_locate_ship_B1()
    f_locate_ship_B2()
    f_locate_ship_K1()
    f_locate_ship_K2()
    f_locate_ship_S1()
    f_locate_ship_S2()
    f_locate_ship_D1()
    f_locate_ship_D2()
    while win():
        p=input("Enter your position")
        ai_move()
        moves(p)
    sys.exit(0)
