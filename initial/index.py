from tkinter import *
from tkinter import ttk

root = Tk()
root.geometry("400x500");
root.title("Statement Genator")

style = ttk.Style()
style.configure("primary", relief="flat", background="#ff0000")



main = ttk.Frame(root, padding=10)
action = ttk.Frame(root, padding=10)

main.pack(side=TOP, expand=True)
action.pack(side=BOTTOM, expand=True)

# Main
ttk.Label(main, text="Income Generator", font=("bold", 24)).grid(column=0, row=0)

# call to action
ttk.Label(action, text="Select Expenses file").grid(column=0, row=0, sticky="W")
ttk.Button(action, text="Select File", command=root.destroy).grid(column=1, row=0, sticky="E")
root.mainloop()