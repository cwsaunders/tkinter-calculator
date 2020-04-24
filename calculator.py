import tkinter as tk
import os
from calculatoroperators import *

#Base window:
root = tk.Tk()

#Operators such as multiply, subtract, divide, etc:
op = calculatoroperators()

#Aesthetics:
root.title("Calculator")


frame = tk.Frame(root, bg="white")
frame.place(relwidth=0.8, relheight=0.8, relx=0.1, rely=0.1)

# Number buttons


# Operator buttons
subtract = tk.Button(root, text="-", padx=10, pady=6, fg="white", bg="#263D42", command=op.subtract)
subtract.pack()
add = tk.Button(root, text="+", padx=10, pady=6, fg="white", bg="#263D42", command=op.add)
add.pack()
divide = tk.Button(root, text="/", padx=10, pady=6, fg="white", bg="#263D42", command=op.divide)
divide.pack()
multiply = tk.Button(root, text="*", padx=10, pady=6, fg="white", bg="#263D42", command=op.multiply)
multiply.pack()


#Main():
root.mainloop()
