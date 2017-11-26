from tkinter import *

def checked(i) :
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
      else :
            player = "X"
            button["bg"] = "lightgreen"

window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)

window.mainloop()


from tkinter import *
import tkinter.messagebox

def checked(i) :
      
      global player
      button = list[i]

      if button["text"] != "     " :
            return
      button["text"] = player 
      button["bg"] = "yellow"

      if player == "X" :
            player = "O"
            button["bg"] = "yellow"
            Checked_W()
      else :
            player = "X"
            button["bg"] = "lightgreen"
            Checked_W()
            
def Checked_W():
       if list[0]["text"] == list[3]["text"] == list[6]["text"] != "     ":
            win()
       elif list[1]["text"] == list[4]["text"] == list[7]["text"] != "     ":
            win()   
       elif list[2]["text"] == list[5]["text"] == list[8]["text"] != "     ":
            win()
       elif list[0]["text"] == list[1]["text"] == list[2]["text"] != "     ":
            win()
       elif list[3]["text"] == list[4]["text"] == list[5]["text"] != "     ":
            win()
       elif list[6]["text"] == list[7]["text"] == list[8]["text"] != "     ":
            win()
       elif list[0]["text"] == list[4]["text"] == list[8]["text"] != "     ":
            win()
       elif list[2]["text"] == list[4]["text"] == list[6]["text"] != "     ":
            win()
            
window = Tk()
player = "X"
list= []

for i in range(9) :
      b = Button(window, text="     ", command=lambda k=i: checked(k))
      b.grid(row=i//3, column=i%3)
      list.append(b)
       
def win():
      if player == "X":
            tkinter.messagebox.showinfo("WINNER", "player 0")
            quit()
      else:
            tkinter.messagebox.showinfo("WINNER", "player X")
            quit()

window.mainloop()
