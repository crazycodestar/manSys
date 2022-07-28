from tkinter import *
from tkinter import ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import os

from setuptools import Command

from processor import Ledger

# from processor import Ledger

ledgerType = type(Ledger(""))
income = None
filetypes = [("Excel Files", "*.xlsx")]

root = Tk()
root.geometry("400x500")
root.title("Statement Genator")

style = ttk.Style()
style.configure("primary", relief="flat", background="#ff0000")


main = ttk.Frame(root, padding=10)
action = ttk.Frame(root, padding=10)

main.pack(side=TOP, expand=True)
action.pack(side=BOTTOM, expand=True)

# Main
ttk.Label(main, text="Income Generator", font=("bold", 24)).grid(column=0, row=0)

# functions


def saveExcelFile():
    file = fd.asksaveasfilename(
        initialdir=os.getcwd(),
        title="Save Transactions",
        defaultextension=".xlsx",
        filetypes=filetypes,
        initialfile="generated",
    )
    status = income.generateStatement(file)
    if status == 200:
        showinfo(message="file saved successfully")
    if status == 401:
        showinfo(message="The file is opened, Please close and try again")
    # os.startfile(file)


def select_file():
    # income.generateStatement
    global income

    filename = fd.askopenfilename(
        title="Open a file", initialdir=os.getcwd(), filetypes=filetypes
    )

    income = Ledger(filename)

    ttk.Label(main, text="file selected").grid(column=0, row=2)
    ttk.Button(action, text="generate expenses", command=saveExcelFile).grid(
        column=2, row=0, sticky="E"
    )


# call to action
ttk.Label(action, text="Select Expenses file").grid(column=0, row=0, sticky="W")
ttk.Button(action, text="Select File", command=select_file).grid(
    column=1, row=0, sticky="E"
)

root.mainloop()
