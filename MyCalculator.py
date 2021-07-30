import tkinter as tk
from tkinter import Button, font

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

        self.total_expression ="0"
        self.current_expression ="0"

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
        self.create_buttom()
        self.create_operator_buttoms()

    def create_operator_buttoms(self):
        i=0
        for operator,symbol in self.operations.items():
            buttom = tk.Button(self.buttom_fame,text=symbol,font=("Arial",20),bg=WHITE,borderwidth=0)
            buttom.grid(row=i,column=4,sticky=tk.NSEW)
            i+=1
    def create_buttom(self):
        for digit,grid_value in self.digits.items():
            button = tk.Button(self.buttom_fame,text=str(digit),bg=WHITE,fg=LABEL_COLOR,font=("Times New Roman", 20, "bold"),borderwidth=0)
            button.grid(row=grid_value[0],column=grid_value[1],sticky=tk.NSEW)


    def display_total_labes(self):
        total_label = tk.Label(self.window,text=self.total_expression,anchor=tk.E,bg=LIGHT_GRAY,font=(LABEL_COLOR,25),padx=20)
        total_label.pack(expand=True,fill="both")

        return total_label 

    def display_label(self):
        label=tk.Label(self.window,text=self.current_expression,anchor=tk.E,bg=LIGHT_GRAY,font=LABEL_COLOR,padx=20)
        label.pack(expand=True,fill="both")
        return label

        
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


if __name__ == "__main__":
    calc = Calculator()

    calc.run_app()