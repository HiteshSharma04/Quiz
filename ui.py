from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"

class Interface:
    def __init__(self,a:QuizBrain):
        self.quin = a
        self.Window = Tk()
        self.Window.title("QUIZZY")
        self.Window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.label = Label(text=f"Score : 0",fg="white",bg=THEME_COLOR)
        self.label.grid(row=0,column=1)        

        self.canva = Canvas(width=600,height=400,bg="white")
        self.question = self.canva.create_text(300,200,width=580, text="Question",fill=THEME_COLOR,font=("Arial",20,"bold"))
        self.canva.grid(row=1,column=0,columnspan=2,pady=50)

        self.t = PhotoImage(file="projects/API/quizapp/true.png")
        self.t_button = Button(image=self.t,highlightthickness=0,command=self.true)
        self.t_button.grid(row=2,column=1)

        self.f = PhotoImage(file="projects/API/quizapp/false.png")
        self.f_button = Button(image=self.f,highlightthickness=0,command=self.false)
        self.f_button.grid(row=2,column=0)
        self.next()


        self.Window.mainloop()
    
    def next(self):
        self.canva.config(bg="white")
        if self.quin.still_has_questions():          
            self.label.config(text=f"Score : {self.quin.score}")
            q = self.quin.next_question()
            self.canva.itemconfig(self.question,text = q)
        else:
            self.canva.itemconfig(self.question,text = f"THE END! \n Your Score {self.quin.score}/10")
            self.t_button.config(state="disabled")
            self.f_button.config(state="disabled")

    def true(self):
        self.right = self.quin.check_answer("False")
        self.feed(self.right)

    def false(self):
        self.right = self.quin.check_answer("False")
        self.feed(self.right) 

    def feed(self,right):
        if self.right:
            self.canva.config(bg="green")
        else:
            self.canva.config(bg="red")
        self.Window.after(1000,self.next)