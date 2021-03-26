"""

Name: Ruby (Ning) Chen

Solitaire Game "cool" ver.

Take the regular rules of solitaire with a double twist!
1. To operate the game enter a deck size and click “Load Deck”
2. Press the “Go position” button to initiate the deck.
3. Then type in two integer values; placement of the deck to move from and deck to
move to, and simply click “Go position” to execute!

CHANGES:
When you enter a deck size, the game will produce two times of the deck! (Excluding the last biggest value which only has one). To win this game you must stack all, yes all the cards onto ONE pile! To make this easier for you, you can stack both ways; from 0 1 2 3 or 3 2 1 ; you can mix and match these two methods BUT they must be within 1 integer value of each other.
To win you must stack all cards onto one pile!
There are VERY limited solutions to get all the cards onto one pile!

"""
import tkinter as tk
from tkinter import ttk
import sys
import random
from tkinter.messagebox import showinfo

class Deque:

    def __init__(self):
        self.item = []

    def add_front(self, item):
        self.item.append(item)

    def add_rear(self, item):
        self.item.insert(0, item)

    def remove_front(self):
        return self.item.pop()

    def remove_rear(self):
        return self.item.pop(0)

    def size(self):
        return len(self.item)

    def peek(self):
        return self.item[-1]

    def peeklast(self):
        return self.item[0]

    def printall(self, index):
        if index == 0:
            if self.size() > 0:
                print(self.item[0], "* " * (len(self.item)-1))
            else:
                print()
        if index > 0:
            if self.size() > 0:
                for i in range(len(self.item)):
                    print("{} ".format(self.item[i]), end = "")
                print()
            else:
                print()

class Solitaire:
    
    def __init__(self, ncards):
        self.t = []
        self.CardNo = len(ncards)
        self.ColNo = (self.CardNo // 8) + 4
        self.ChanceNo = self.CardNo * 2
        
        for i in range(self.ColNo):
            self.t.append(Deque())
        for i in range(self.CardNo):
            self.t[0].add_front(ncards[i])

    #display used for each step 
    def display(self):
        for i in range(self.ColNo):
            print("{}: ".format(i), end = "")
            self.t[i].printall(i)

    #placing cards into the different decks
    def move(self, c1 , c2):
        if c1 == 0 and c2 == 0:
            self.t[0].add_front(self.t[0].remove_rear())
        if c1 == 0 and c2 > 0:
            if self.t[c2].size() == 0 or self.t[c2].peek()  == self.t[0].peeklast()+1 or\
               self.t[c2].peek()+1  == self.t[0].peeklast() :
                self.t[c2].add_front(self.t[0].remove_rear())
        if c1 > 0 and  c2 > 0:
            if self.t[c2].size() == 0 or self.t[c2].peek() == self.t[c1].peeklast()+1 or\
               self.t[c2].peek()+1  == self.t[0].peeklast():
                for i in range(self.t[c1].size()):
                    self.t[c2].add_front(self.t[c1].remove_rear())
 

    #operates each time per button click  
    def play(self, col1, col2):
        
        #col1 and col2 for two positions entered by user
        if col1 >= 0 and col2 >= 0 and col1 < self.ColNo and col2 < self.ColNo:
            self.move(col1, col2)
            self.display()
        #condition code if complete operating every round
        if (self.IsComplete() == True):
            print("Congratulations! HERE IS A SPECIAL PRIZE ")
            print("To play again, load a new deck")
            popup()


    def IsComplete(self):
        count = 0 
        for i in range(self.ColNo):
            if self.t[i].size() > 0:
                count += 1 
        
        if count > 1:
            return False
        if self.t[0].size() != 0:
            return False
        return True



#popup prize, its very cute
def popup():
    global photo
    congrats = tk.Toplevel()
    congrats.title("MEOW")
    photo = photo.subsample(5)
    bg_label = tk.Label(congrats,image = photo)
    bg_label.place(relx = 0.16, rely = 0.25)
    buton = ttk.Button(congrats, text="CAT REVEAL", command=congrats.destroy)
    buton.place(relx = 0.20, rely =0.16)


#this generates a shuffled deck of num amount of cards
def generate_cards(num):
    li = [x for x in range(1, num+1)]
    li += [x for x in range(1, num)]
    random.shuffle(li)
    return li

def redirector(inputStr):
    textbox.insert(tk.END, inputStr)


#loads desired deck size from user input 
def load_deck():
    global s
    s = Solitaire(generate_cards(int(entry.get())))
    print("Click 'go position' to start")
    s.display()

def play():
    try:
        global s
        print("Enter a legal move then click 'go position'")
        s.play(int(entry1.get()), int(entry2.get()))
    except:
        pass




HEIGHT = 700
WIDTH = 900
window = tk.Tk()
window.title("Solitaire with me-ow")
canvas = tk.Canvas(window, height= HEIGHT, width= WIDTH)
canvas.pack()

#background photo very important
photo = tk.PhotoImage(file="catt.png")
#resizing photo
photo = photo.subsample(5)
bg_label = tk.Label(window,image = photo)
bg_label.image = photo
bg_label.place(relheight = 1, relwidth = 1)


#loading the deck values into solitaire class
load_button = ttk.Button(window, text= "Load deck", command= load_deck)
load_button.place(relx = 0.65, rely = 0.10, relwidth = 0.2, relheight = 0.03)

#entry of position 1 (deck to move from)
entry1 = tk.Entry(window, font = 30)
entry1.place(relx = 0.15, rely = 0.150, relwidth = 0.2, relheight = 0.03)
entry1.insert(tk.END, 0)
#entry of position 2 (deck to move to) 
entry2 = tk.Entry(window, font = 30)
entry2.place(relx = 0.45, rely = 0.150, relwidth = 0.2, relheight = 0.03)
entry2.insert(tk.END, 0) 

#click to execute the move) 
to =ttk.Button(window,text="Go to deck!", command = play)
to.place( relx = 0.65, rely = 0.15, relwidth = 0.2, relheight = 0.03)

#labels for user entries 
from_label =tk.Label(window,text="From deck:")
from_label.place( relx = 0.05, rely = 0.15, relwidth = 0.1, relheight = 0.03)
from_label2 =tk.Label(window,text="To deck:")
from_label2.place( relx = 0.35, rely = 0.15, relwidth = 0.1, relheight = 0.03)

#entry for initial deck size
entry = tk.Entry(window)
entry.place(relx = 0.45, rely = 0.10, relwidth = 0.2, relheight = 0.03)

textbox = tk.Text(window, bg = 'white')
textbox.place(relx = 0.35, rely = 0.25, relwidth = 0.5, relheight = 0.7)

sys.stdout.write = redirector
window.mainloop()


