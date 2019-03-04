import tkinter as tk

#declaring 'regular' non-tk variables

regionIndex = None
textmsg = "this button should increment by one every time you press it"
outPutInt = 0

from DND_Classes import Items

leather_armor = Items("leather armor", 10)
plate_armor = Items("plate armor", 25000)
light_crossbow = Items("light crossbow", 25)
dagger = Items("dagger", 2)
longsword = Items("longsword", 15)

items = [
    leather_armor,
    plate_armor,
    light_crossbow,
    dagger,
    longsword
]

from DND_Classes import Regions

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

from DND_Classes import Locations

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

from DND_Classes import Merchants

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

from DND_Classes import Rarity

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



buildButtonStack(items, itemFrame, itemVar)
#for val, btnMsg in enumerate(items):
    #tk.Radiobutton(itemFrame,
                   #text=btnMsg,
                   #padx = 20,
                   #variable=itemVar,
                   #command=regionChoice,
                   #indicatoron = 0,
                   #width = 15,
                   #value=val).pack()


for val, btnMsg in enumerate(regions):
    tk.Radiobutton(regionFrame, 
                  text=btnMsg.region_name,
                  padx = 20, 
                  variable=regionVar, 
                  command=regionChoice,
                  indicatoron = 0,
                  width = 15,
                  value=val).pack()
                  
for val, btnMsg in enumerate(locations):
    tk.Radiobutton(locationFrame, 
                  text=btnMsg.location_type,
                  padx = 20, 
                  variable=locationVar, 
                  command=regionChoice,
                  indicatoron = 0,
                  width = 15,
                  value=val).pack()
                  
for val, btnMsg in enumerate(merchants):
    tk.Radiobutton(merchantFrame, 
                  text=btnMsg.merchant_type,
                  padx = 20, 
                  variable=merchantVar, 
                  command=regionChoice,
                  indicatoron = 0,
                  width = 15,
                  value=val).pack()
                  
for val, btnMsg in enumerate(rarity):
    tk.Radiobutton(rarityFrame, 
                  text=btnMsg.rarity_type,
                  padx = 20, 
                  variable=rarityVar, 
                  command=regionChoice,
                  indicatoron = 0,
                  width = 15,
                  value=val).pack()
                  

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
