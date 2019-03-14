import tkinter as tk
import csv

root = tk.Tk()
frame = tk.Frame(root)
costVar = tk.StringVar()

def printDatCost():
    print(costVar.get())

csvfile = open('save_data.csv', newline='')


reader = csv.DictReader(csvfile)
for row in reader:
    print()
    varName = row["weapon"] + " = " + row["cost"]
    tk.Radiobutton(frame, 
                   text=row["weapon"],
                   padx = 20, 
                   variable = costVar,
                   command=printDatCost,
                   indicatoron = 0,
                   width = 15,
                   value=varName).pack()
        


print("help")
frame.pack()
root.mainloop()


#when we last saw our hero on 2019-2-28 the problem I was having was that the buttons don't like, print their cost, odd
