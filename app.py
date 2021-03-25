from tkinter import *
from chatbot import get_response, bot

frontColor = "#ccffcc" 
frontColorR = "#C5CE10" 
letterColor = "#333B09"

letterT = "Arial 20"
letterB = "Arial 20 bold"

class ChatApp:
    def __init__(self):
        self.window = Tk()
        self.windows()
    
    def run(self):
        self.window.mainloop()

    def windows(self): #Setup windows to see the chat
        self.window.title('Chat Bot') 
        self.window.resizable(width=False, height=False)
        self.window.configure(width=470, height=550, bg=frontColorR)

        headL = Label(self.window, bg=frontColorR, fg=letterColor,
                   text="Welcome!", font=letterB, pady=10) #title
        headL.place(relwidth=1)

        line = Label(self.window, width=450, bg=frontColor)
        line.place(relwidth=1, rely=0.07, relheight=0.012)
        self.textw = Text(self.window, width=20, height=2, bg=frontColorR, fg=letterColor,
                                font=letterT, padx=5, pady= 5)
        self.textw.place(relheight=0.745, relwidth=1, rely=0.08)
        self.textw.configure(cursor='arrow', state=DISABLED)

        scrollbar = Scrollbar(self.textw)  #create scrollbar
        scrollbar.place(relheight=1, relx=0.974)
        scrollbar.configure(command=self.textw.yview)

        bottonL = Label(self.window, bg=frontColor, height=80)
        bottonL.place(relwidth=1, rely=0.825)

        self.entermsg = Entry(bottonL, bg="#A0A80D", fg=letterColor, font=letterT) #create entry space 
        self.entermsg.place(relwidth=0.74, relheight=0.06, rely=0.008, relx=0.011)
        self.entermsg.focus()
        self.entermsg.bind("<Return>", self.enter)

    def enter(self, event): #integrated the bot with the windos, to get questions and answers.
        msg = self.entermsg.get()
        self.insertmsg(msg, 'You')
    def insertmsg(self, msg, sender):
        if not msg:
            return
        self.entermsg.delete(0, END)  #User message
        msgs = f"{sender}: {msg}\n\n"
        self.textw.configure(state=NORMAL)
        self.textw.insert(END, msgs)
        self.textw.configure(state=DISABLED)

        msgr = f"{bot}: {get_response(msg)}\n\n" #Bot message
        self.textw.configure(state=NORMAL)
        self.textw.insert(END, msgr)
        self.textw.configure(state=DISABLED)

        self.textw.see(END)

if __name__=="__main__":
    app = ChatApp()
    app.run()