import tkinter as tk
import csv

root = tk.Tk()
frame = tk.Frame(root)

def printDatCost(messageToPrint):
    print(messageToPrint)

with open('Weapons.csv', newline='') as csvfile:
     reader = csv.DictReader(csvfile)
     for row in reader:
         print(row['Weapon'], row['Cost'])
         tk.Radiobutton(frame, 
                  text=row["Weapon"],
                  padx = 20, 
                  command=printDatCost(row['cost'],
                  indicatoron = 0,
                  width = 15,
                  value=val).pack()
        


print("help")
frame.pack()
root.mainloop()
