import tkinter as tk
import csv

items_csv = open('Weapons.csv', newline='')

#declaring 'regular' non-tk variables

regionIndex = None
textmsg = "this button should increment by one every time you press it"
outPutInt = 0

items_list = []
regions_list= []
locations_list = []
merchants_list = []
rarity_list = []


from DND_Classes import Items
from DND_Classes import Regions
from DND_Classes import Locations
from DND_Classes import Merchants
from DND_Classes import Rarity

reader = csv.DictReader(items_csv)
for row in reader:
    items_list.append(Items(row['weapon'], row['cost']))
    regions_list.append(Regions(row['region'], row['region_var']))
    locations_list.append(Locations(row['locations'], row['location_var']))
    merchants_list.append(Merchants(row['merchants'], row['merchant_var']))
    rarity_list.append(Rarity(row['rarity'], row['rarity_var'])) 
    
    




Adrivian_Empire = Regions("Adrivian Empire", 2.7)
Sylvian_Kingdom = Regions("Sylvian Kingdom", 2.6)
Evasol_Court = Regions("Evasol Court", 2.5)
Adrokk = Regions("Adrokk", 3.4)
Treerock_Peninsula = Regions("Treerock Peninsula", 2.7)

regions = [
    Adrivian_Empire,
    Sylvian_Kingdom,
    Evasol_Court,
    Adrokk,
    Treerock_Peninsula
    ]



wilderness = Locations("wilderness", 0.3)
village = Locations("village", 0)
town = Locations("town", 0.1)
city = Locations("city", 0.3)
road = Locations("road", 0.5)

locations = [
    wilderness,
    village,
    town,
    city,
    road
    ]



craftsman = Merchants("craftsman", -0.5)
general = Merchants("general", 0.1)
specialized = Merchants("specialized", 0.2)
ultraspecialized =Merchants("ultraspecialized", 0.5)
walmart = Merchants("walmart", -1.2)

merchants = [
    craftsman,
    general,
    specialized,
    ultraspecialized,
    walmart
    ]


rare = Rarity("rare", 1.2)
unusual = Rarity("unusual", 0.9)
occasional = Rarity("occasional", 0.3)
frequent = Rarity("frequent", 0)
up_the_yin_yang = Rarity("up the yin yang", -0.5)

rarity = [
    rare,
    unusual,
    occasional,
    frequent,
    up_the_yin_yang
    ]

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
root.title("DND Economy Version 0.0.3")


def regionChoice():
    global regionIndex
    itemIndex = itemVar.get()
    regionIndex = regionVar.get()
    locationIndex = locationVar.get()
    merchantIndex = merchantVar.get()
    rarityIndex = rarityVar.get()
    outPutStr.set(str(items[itemIndex].value * (regions[regionIndex].region_value + locations[locationIndex].location_value + merchants[merchantIndex].merchant_value + rarity[rarityIndex].rarity_value)) + " Gold Pieces")
    print(items[itemIndex].value * (regions[regionIndex].region_value + locations[locationIndex].location_value))

#usage = buildButtonStack(array_of_strings_for_button_labels, frame_for_buttons, int_for_index_of_array    
def buildButtonStack(strList, buttonFrame, trackerInt):
    for val, btnMsg in enumerate(strList):
        print("btnMsg = " + str(btnMsg))
        tk.Radiobutton(buttonFrame, 
                  text=btnMsg.name,
                  padx = 20, 
                  variable=trackerInt, 
                  command=regionChoice,
                  indicatoron = 0,
                  width = 15,
                  value=val).pack()
    



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
