import tkinter as tk
import csv

root = tk.Tk()
frame = tk.Frame(root)
#I am so mad that I can't figure out how to make this work without this global variable
weaponCostWhichIsUnfortunatelyAGlobalVariable = "not yet set"

def printDatCost():
    global weaponCostWhichIsUnfortunatelyAGlobalVariable
    print(weaponCostWhichIsUnfortunatelyAGlobalVariable)

csvfile = open('Weapons.csv', newline='')


reader = csv.DictReader(csvfile)
for row in reader:
    print(row['Weapon'], row['Cost'])
    weaponCostWhichIsUnfortunatelyAGlobalVariable = row['Cost']
    tk.Radiobutton(frame, 
                   text=row["Weapon"],
                   padx = 20, 
                   command=printDatCost,
                   indicatoron = 0,
                   width = 15,
                   value=row).pack()
        


print("help")
frame.pack()
root.mainloop()


#when we last saw our hero on 2019-2-28 the problem I was having was that the buttons don't like, print their cost, odd
