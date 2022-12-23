from tkinter import *
import random

root=Tk()
root.title("color randomizer")
root.geometry("600x600")
root.configuration(bg="snow")

lbl_random_color_name = Label(root, font=("comicsans",28,"bold"), bg="white")
lbl_random_color_name.place(relx=0.5,rely=0.5,anchor=CENTER)

class game():
    def __init__(self):
        self.__socre=0
    
    def updateGame(self):
        self.text=['BLUE','GREEN','YELLOW','BLACK']
        self.random_number_fro_text=random.randint(0,3)
        self.color=['blue','green','yellow','black']
        self.random_number_for_color = random.randint(0,3)
        lbl_random_color_name['text']=self.text[self.random_number_for_text]
        lbl_random_color_name['fg']=self.color[self.random_number_for_color]
        
        
game_obj=game()
btn=Button(root,text="Start",command=game_obj.updateGame,bg='gray',fg="white",relief=FLAT,padx=3,pady=3,font=("comicsans",18,"BOLD"))
btn.place(relx=0.6,rely=0.6,anchor=CENTER)

root.mainloop()