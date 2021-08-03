import tkinter as tk
from tkinter import Button, font
from tkinter.constants import COMMAND

LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
WHITE ="#FFFFFF"
DIGIT_FONT_STYLE=("Arial" ,24, "bold")
class Calculator():

    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("500x500")
        self.window.resizable(0,0)
        self.window.title("CALCULATOR")

        self.total_expression =""
        self.current_expression =""

        self.total_labels=self.display_total_labes()
        self.labels=self.display_label()

        self.display_frame =self.create_display_frame()
        self.buttom_fame = self.create_buttom_frame()
        
        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }
        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttom_fame.rowconfigure(0,weight=1)
        for x in range (1,5):
            self.buttom_fame.rowconfigure(x,weight=1)
            self.buttom_fame.columnconfigure(x, weight=1)
        self.create_buttom()
        self.create_operator_buttoms()
        self.create_clear_buttom()
        self.create_euqals_buttom()
        self.create_squer_buttom()
    def create_operator_buttoms(self):
        i=0
        for operator,symbol in self.operations.items():
            buttom = tk.Button(self.buttom_fame,text=symbol,font=("Arial",20),bg=WHITE,borderwidth=0,command=lambda x=operator :self.append_operator(x))
            buttom.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    
    def create_clear_buttom(self):

            buttom = tk.Button(self.buttom_fame,text="C",font=("Arial",20),bg=WHITE,borderwidth=1,command=lambda:self.clear_button_functionality())
            buttom.grid(row=0,column=1,sticky=tk.NSEW)

    def create_squer_buttom(self):

        buttom = tk.Button(self.buttom_fame,text="x\u00b2",font=("Arial",20),bg=WHITE,borderwidth=0,command=lambda: self.square())
        buttom.grid(row=0,column=2,sticky=tk.NSEW)

    def square(self):
        self.current_expression= str(eval(f"{self.current_expression}**2"))
 
        self.update_current_label()

    def evaluate_function(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        self.current_expression = str(eval(self.total_expression))
        self.update_current_label()



    def create_euqals_buttom(self):
            buttom = tk.Button(self.buttom_fame,text="=",font=("Arial",20),bg="light sky blue",borderwidth=1,command=lambda:self.evaluate_function())
            buttom.grid(row=4,column=3,columnspan=2,sticky=tk.NSEW)

    def clear_button_functionality(self):
            self.current_expression=""
            self.total_expression =""
            self.update_total_label()
            self.update_current_label()

    def create_buttom(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttom_fame,text=str(digit),bg=WHITE,fg=LABEL_COLOR,font=("Times New Roman", 20, "bold"),borderwidth=0,command=lambda x=digit : self.add(x))
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)

    def add(self,value):
        self.current_expression += str(value)
        self.update_current_label()

    def display_total_labes(self):
        total_label = tk.Label(self.window,text=self.total_expression,anchor=tk.E,bg=LIGHT_GRAY,font=(LABEL_COLOR,25),padx=20)
        total_label.pack(expand=True,fill="both")

        return total_label 

    def display_label(self):
        label=tk.Label(self.window,text=self.current_expression,anchor=tk.E,bg=LIGHT_GRAY,font=LABEL_COLOR,padx=20)
        label.pack(expand=True,fill="both")
        return label

    def append_operator(self,operator):
        self.current_expression +=operator
        self.total_expression +=self.current_expression
        self.current_expression =""
        self.update_current_label()
        self.update_total_label()

    def run_app(self):
        self.window.mainloop()

    def create_display_frame(self):
        display_frame = tk.Frame (self.window,width=100,height=50,bd=0,highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
        display_frame.pack(expand= True ,fill= "both")
        return display_frame

    def create_buttom_frame(self):
        buttom_frame =tk.Frame(self.window)
        buttom_frame.pack(expand=True,fill="both")
        return buttom_frame

    def update_total_label(self):
        self.total_labels.config(text=self.total_expression)

    def update_current_label(self):
        self.labels.config(text=self.current_expression)

if __name__ == "__main__":
    calc = Calculator()

    calc.run_app()