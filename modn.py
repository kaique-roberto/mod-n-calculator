# Python program to create a simple GUI mod N calculator using Tkinter.
# This code is based on a template provided by GeeksforGeeks at
# https://www.geeksforgeeks.org/python-simple-gui-calculator-using-tkinter/

# import modules
from tkinter import *
from tkinter import ttk

# globally declare the expression variable
expression = ""

# class for tkinter app
class modCalculator:

    def __init__(self, master):
        master.title('Mod N Calculator')
        master.resizable(False, False)
        master.configure(background = '#b2ffff')

        self.style = ttk.Style()
        self.style.configure('TFrame', background = '#b2ffff')
        self.style.configure('TButton', background = '#b2ffff')
        self.style.configure('TLabel', background = '#b2ffff', font = ('Arial', 11))
        self.style.configure('Header.TLabel', font = ('Arial', 18, 'bold'))

        self.frame_header = ttk.Frame(master)
        self.frame_header.pack()

        self.frame_integer = ttk.Frame(master)
        self.frame_integer.pack()
        
        ttk.Label(self.frame_integer, text = 'Integer N:').grid(row = 0, column = 0, padx = 5)
        
        self.integer = StringVar()
        integer_field = ttk.Entry(self.frame_integer, textvariable=self.integer)
        integer_field.grid(row = 0, column = 1, padx = 5, ipadx=5)

        self.frame_content = ttk.Frame(master)
        self.frame_content.pack()

        ttk.Label(self.frame_content, text = '').grid(row = 0, column = 0, padx = 5, sticky = 'sw')

        self.equation = StringVar()
        expression_field = ttk.Entry(self.frame_content, textvariable=self.equation)
        expression_field.grid(row = 1, column = 0, columnspan=4, ipadx=100)
        expression_field.config(state=DISABLED)

        b0 = ttk.Button(self.frame_content, text = '0', command=lambda: self.press(0))
        b1 = ttk.Button(self.frame_content, text = '1', command=lambda: self.press(1))
        b2 = ttk.Button(self.frame_content, text = '2', command =lambda: self.press(2))
        b3 = ttk.Button(self.frame_content, text = '3', command =lambda: self.press(3))
        b4 = ttk.Button(self.frame_content, text = '4', command =lambda: self.press(4))
        b5 = ttk.Button(self.frame_content, text = '5', command =lambda: self.press(5))
        b6 = ttk.Button(self.frame_content, text = '6', command =lambda: self.press(6))
        b7 = ttk.Button(self.frame_content, text = '7', command =lambda: self.press(7))
        b8 = ttk.Button(self.frame_content, text = '8', command =lambda: self.press(8))
        b9 = ttk.Button(self.frame_content, text = '9', command =lambda: self.press(9))

        plus = ttk.Button(self.frame_content, text = '+', command =lambda: self.press("+"))
        minus = ttk.Button(self.frame_content, text = '-', command =lambda: self.press("-"))
        prod = ttk.Button(self.frame_content, text = '*', command =lambda: self.press("*"))
        power = ttk.Button(self.frame_content, text = 'a**b', command =lambda: self.press("**"))

        equal = ttk.Button(self.frame_content, text = '=', command = self.equalpress)
        clear = ttk.Button(self.frame_content, text = 'Clear', command = self.clear)

        b0.grid(row = 5, column = 0, padx = 5, pady = 5, sticky = 'e')
        b1.grid(row = 4, column = 0, padx = 5, pady = 5, sticky = 'e')
        b2.grid(row = 4, column = 1, padx = 5, pady = 5, sticky = 'e')
        b3.grid(row = 4, column = 2, padx = 5, pady = 5, sticky = 'e')
        b4.grid(row = 3, column = 0, padx = 5, pady = 5, sticky = 'e')
        b5.grid(row = 3, column = 1, padx = 5, pady = 5, sticky = 'e')
        b6.grid(row = 3, column = 2, padx = 5, pady = 5, sticky = 'e')
        b7.grid(row = 2, column = 0, padx = 5, pady = 5, sticky = 'e')
        b8.grid(row = 2, column = 1, padx = 5, pady = 5, sticky = 'e')
        b9.grid(row = 2, column = 2, padx = 5, pady = 5, sticky = 'e')

        plus.grid(row = 2, column = 3, padx = 5, pady = 5, sticky = 'e')
        minus.grid(row = 3, column = 3, padx = 5, pady = 5, sticky = 'e')
        prod.grid(row = 4, column = 3, padx = 5, pady = 5, sticky = 'e')
        power.grid(row = 5, column = 3, padx = 5, pady = 5, sticky = 'e')

        equal.grid(row = 5, column = 1, padx = 5, pady = 5, sticky = 'e')
        clear.grid(row = 5, column = 2, padx = 5, pady = 5, sticky = 'e')

    # Function to update expression
    # in the text entry box
    def press(self,num):
            # point out the global expression variable
            global expression

            # concatenation of string
            expression = expression + str(num)

            # update the expression by using set method
            self.equation.set(expression)

    # Function to evaluate the final expression
    def equalpress(self):
            # Try and except statement is used
            # for handling the errors like zero
            # division error etc.

            # Put that code inside the try block
            # which may generate the error
            try:

                    global expression

                    # eval function evaluate the expression
                    # and str function convert the result
                    # into string
                    N = int(self.integer.get())
                    total = str(eval(expression)%N)

                    self.equation.set(total)

                    # initialize the expression variable
                    # by empty string
                    expression = ""

            # if error is generate then handle
            # by the except block
            except:

                    self.equation.set(" error ")
                    expression = ""


    # Function to clear the contents
    # of text entry box
    def clear(self):
            global expression
            expression = ""
            self.equation.set("")
            
def main():            
    
    root = Tk()
    feedback = modCalculator(root)
    root.mainloop()
    
if __name__ == "__main__": main()
