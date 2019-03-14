import tkinter as tk
import csv
from DND_Classes import Items
from DND_Classes import Regions
from DND_Classes import Locations
from DND_Classes import Merchants
from DND_Classes import Rarity

items_csv = open('save_data.csv', newline='')

#declaring 'regular' non-tk variables

regionIndex = None
textmsg = "this button should increment by one every time you press it"
outPutInt = 0

items_list = []
regions_list = []
locations_list = []
merchants_list = []
rarity_list = []


reader = csv.DictReader(items_csv)
for row in reader:
    items_list.append(Items(row['weapon'], row['cost']))
    regions_list.append(Regions(row['region'], row['region_var']))
    locations_list.append(Locations(row['locations'], row['location_var']))
    merchants_list.append(Merchants(row['merchants'], row['merchant_var']))
    rarity_list.append(Rarity(row['rarity'], row['rarity_var'])) 


#it gets mad if this isn't first

root = tk.Tk()

#special tk varibles I don't understand

regionVar = tk.IntVar()
regionVar.set(1)
locationVar = tk.IntVar()
locationVar.set(1)
itemVar = tk.IntVar()
itemVar.set(1) 
merchantVar = tk.IntVar()
merchantVar.set(1)
rarityVar = tk.IntVar()
rarityVar.set(1)
buttonCountInt = 1
buttonCountStr = tk.StringVar()
outPutStr = tk.StringVar()
outPutStr.set("still not set")

#framework and other tk 'objects'
frame = tk.Frame(root)
regionFrame = tk.Frame(root)
locationFrame = tk.Frame(root)
itemFrame = tk.Frame(root)
merchantFrame = tk.Frame(root)
rarityFrame = tk.Frame(root)
w = tk.Label(frame, text = textmsg)
outPut = tk.Label(root, width = 35, textvariable = outPutStr)
root.title("DND Economy Version 0.0.4")


def calculateCost():
    print("locations_list[locationVar.get()].value = " + locations_list[locationVar.get()].value)
    outPutStr.set(str(float(items_list[itemVar.get()].value) * (float(regions_list[regionVar.get()].value) + float(locations_list[locationVar.get()].value) + float(merchants_list[merchantVar.get()].value) + float(rarity_list[rarityVar.get()].value))) + " Gold Pieces")

#usage = buildButtonStack(array_of_strings_for_button_labels, frame_for_buttons, int_for_index_of_array    
def buildButtonStack(strList, buttonFrame, trackerInt):
    for val, btnMsg in enumerate(strList):
        print("btnMsg = " + str(btnMsg))
        print("trackerInt = " + str(trackerInt))
        tk.Radiobutton(buttonFrame, 
                  text = btnMsg.name,
                  padx = 20, 
                  variable = trackerInt, 
                  command = calculateCost,
                  indicatoron = 0,
                  width = 15,
                  value=val).pack()
        #for some reason this if statement doesnt work, likely because csv is reading the blank cells as objects
        if strList is None:
            break
    



def increaseCount():
    global buttonCountInt
    global buttonCountStr
    buttonCountInt += 1
    
    buttonCountStr.set(str(buttonCountInt))


button = tk.Button(frame,
                   textvariable = buttonCountStr,
                   
                   command = increaseCount)

buttonCountStr.set("1")



buildButtonStack(items_list, itemFrame, itemVar)
buildButtonStack(regions_list, regionFrame, regionVar)
buildButtonStack(locations_list, locationFrame, locationVar)
buildButtonStack(merchants_list, merchantFrame, merchantVar)
buildButtonStack(rarity_list, rarityFrame, rarityVar)

                  

w.pack(side = tk.LEFT)
button.pack(side = tk.LEFT)



frame.pack()
itemFrame.pack(side = tk.LEFT)
regionFrame.pack(side = tk.LEFT)
locationFrame.pack(side = tk.LEFT)
merchantFrame.pack(side = tk.LEFT)
rarityFrame.pack(side = tk.LEFT)
outPut.pack(side = tk.LEFT)
root.mainloop()
