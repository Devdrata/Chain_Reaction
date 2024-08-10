#clear screen func
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')
#defining colors 
def Red(skk):
    return ("\033[91m {}\033[00m" .format(skk))
def cyan(skk):
    return ("\033[96m {}\033[00m" .format(skk))
def yellow(skk):
    return ("\033[93m {}\033[00m" .format(skk))


class cell(object):
    def __init__(self,i):
        self.identification = i
        if self.identification in (0,9,90,99):
            self.tag = "Corner"
        elif 1<=self.identification<=8:
            self.tag = "Top Edge"
        elif 91<=self.identification<=98 :
            self.tag = "Bottom Edge"
        elif self.identification%10 == 0 :
            self.tag = "Left Edge"
        elif self.identification%10 == 9:
            self.tag = "Right Edge"

        else:
            self.tag = "Middle"
        self.content = 0
        self.representation = Red(self.content)
        self.owner = None


    def collision(self,iden,new_owner):
        cell_list[iden].owner = new_owner
        # if new_owner == 1:
        #     cell_list[iden].representation = yellow(self.content)
        # else:
        #     cell_list[iden].representation = cyan(self.content)
        self.increment(iden,new_owner)
        



    def burst(self,identification,owner):
        num = identification
        cell_list[num].content = 0
        cell_list[num].representation = Red(cell_list[self.identification].content)
        neighbours = []
        
        if self.tag == "Middle":
            neighbours = [
                num-1,
                num+1,
                num-10,
                num+10
                ]
        elif self.tag == "Top Edge":
            neighbours = [
                num-1,
                num+1,
                num+10,
            ]
        elif self.tag == "Right Edge":
            neighbours = [
                num-10,
                num+10,
                num-1,
            ]
        elif self.tag == "Left Edge":
            neighbours = [
                num+10,
                num-10,
                num+1,
            ]
        elif self.tag == "Bottom Edge":
            neighbours = [
                num-10,
                num-1,
                num+1,
            ]
        elif self.tag == "Corner":
            if num == 0:
                neighbours = [1,10]
            elif num == 9:
                neighbours = [8,19]
            elif num == 90:
                neighbours = [80,91]
            elif num == 99:
                neighbours = [89,98]
        for j in neighbours:
                self.collision(j,self.owner)
        
        cell_list[num].owner = None







    def increment(self,identification,new_owner):
        




        if cell_list[identification].owner == None:
            cell_list[identification].owner = new_owner
        
        if cell_list[identification].owner != new_owner:
            print("You do not own this box")
            return "Fail"





        cell_list[identification].content += 1
        cell_list[identification].representation = new_owner(cell_list[identification].content)


        if cell_list[identification].content == 2:
            if cell_list[identification].tag == "Corner":
                cell_list[identification].burst(identification,cell_list[identification].owner)
        elif cell_list[identification].content == 3:
            if cell_list[identification].tag == "Top Edge" or cell_list[identification].tag == "Right Edge" or cell_list[identification].tag == "Left Edge" or cell_list[identification].tag == "Bottom Edge":
                cell_list[identification].burst(identification,cell_list[identification].owner) 
        elif cell_list[identification].content == 4:
            if cell_list[identification].tag == "Middle":
                cell_list[identification].burst(identification,cell_list[identification].owner)
                




def print_grid():
    cls()
    for i in range(1,11):
        print(i,end = "\t")
    for i in range(0,100):
        if i%10 ==0:
            print("\n")
            print(chr(65+(i//10))+"\t")
        print(cell_list[i].representation,end = "\t")
        #print([cell_list[i].tag,cell_list[i].content],end = "\t")
        
        #print(i,end = "\t")
    print("\n"*2)




def initialize():
    #cell generator
    global cell_list
    cell_list = [cell(i) for i in range(0,100)]
    #printing 10x10 grid of cells:
    print_grid()
    game()
    
    #game()


def game():
    count = 0
    print("Player One: Yellow \n Player Two: Cyan. \n Player One's Turn: \n")
    while True:
        var = input_add()
        if var ==None:
            print_grid()
            continue
        if count%2 ==0:                   
            flag = cell_list[var].increment(var,yellow)
            player = "Two"
            if flag == "Fail":
                continue
        else:
            flag = cell_list[var].increment(var,cyan)
            player = "One"
            if flag == "Fail":
                continue
        count += 1
        if count>2:
            flag = check()
            if flag:
                print_grid()
                print(flag)
                input("Press any key to exit")
                break
        print_grid()
        print(f"Player {player}'s turn. \n")


def check():
    cyancount = 0
    yellowcount = 0
    for i in cell_list:
        if i.owner == cyan:
            cyancount+=1
        elif i.owner == yellow:
            yellowcount += 1
    if cyancount == 0:
        return "Yellow Won"
    elif yellowcount == 0:
        return "Cyan Won"
    else:
        return None

def input_add():
    try:
        inp = input("\nEnter cell adress")
        if inp.lower() == "quit":
            raise KeyboardInterrupt
        if not(65<=ord(inp[0])<=90):
            print("Invalid Input")
            return None
        if int(inp[1::])>10:
            print("Invalid Input")
            return None
        if int(inp[1::]==00):
            inp[1::] = 0
        else:
            adr = ((ord(inp[0])-65)*10) + int(inp[1::]) -1
            return adr
    except KeyboardInterrupt:
        print("\n Quitting")
        exit(0)
    except:
        print("Something Went Wrong, Try Again.")
        
    

   
initialize()
