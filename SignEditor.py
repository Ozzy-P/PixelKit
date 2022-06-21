# File to change current table values in Steins;Gate
# Printed data has to be manually exported onto corresponding table value

from tkinter import *
import re

import keyboard # pip install keyboard


# Create main window.
window = Tk()
window.title("Sign Pixel Editor")
window.geometry("400x400")
window.resizable(False, False)
window.grid_columnconfigure(0,weight=1)
globalDraw = True
globalErase = False

def toggleDraw():
    global globalDraw 
    globalDraw = not globalDraw


def toggleErase():
    global globalErase
    global globalDraw 
    if globalErase:     
        globalErase = not globalErase
        globalDraw = True
    else:
        globalErase = not globalErase
        globalDraw = False


keyboard.on_press_key("d", lambda _:toggleDraw())
keyboard.on_press_key("e", lambda _:toggleErase())

# Rows = 8; Colums = 128 / 8
#totalPixels = 512
#maximumPixelHeight = 16

totalPixels = 1024
maximumPixelHeight = 32


#window.geometry(str((totalPixels // 8) * 59) + "x500")
window.geometry(str((totalPixels // 8) * 25) + "x" + str((maximumPixelHeight) * 32))

pixelOrder = []
buttons = {}
dataValues = []
# it does something, don't know much about it other than it takes in args for a new button. Also, custom attributes
class NewButton(Button):
    def __init__(self, master, isActive=False,bIndex = 0, currentPixelIndex = 0, *args, **kwargs):
        Button.__init__(self, master, *args, **kwargs)
        self.master, self.isActive,self.bIndex,self.currentPixelIndex = master, isActive, bIndex,currentPixelIndex


######################################################
##copy pasted
#https://stackoverflow.com/questions/20399243/display-message-when-hovering-over-something-with-mouse-cursor-in-python
#cause yes.
class ToolTip(object):

    def __init__(self, widget):
        self.widget = widget
        self.tipwindow = None
        self.id = None
        self.x = self.y = 0

    def showtip(self, text):
        "Display text in tooltip window"
        self.text = text
        if self.tipwindow or not self.text:
            return
        x, y, cx, cy = self.widget.bbox("insert")
        x = x + self.widget.winfo_rootx() + 57
        y = y + cy + self.widget.winfo_rooty() +27
        self.tipwindow = tw = Toplevel(self.widget)
        tw.wm_overrideredirect(1)
        tw.wm_geometry("+%d+%d" % (x, y))
        label = Label(tw, text=self.text, justify=LEFT,
                      background="#ffffe0", relief=SOLID, borderwidth=1,
                      font=("tahoma", "8", "normal"))
        label.pack(ipadx=1)

    def hidetip(self):
        tw = self.tipwindow
        self.tipwindow = None
        if tw:
            tw.destroy()

def CreateToolTip(widget, text):
    toolTip = ToolTip(widget)
    global globalDraw
    global globalErase
    
    def enter(event):
        toolTip.showtip(text)
        if globalDraw and Tk.cget(widget,"bg") == "black":
            changeArray(widget)
    def leave(event):
        toolTip.hidetip()
        if globalErase and Tk.cget(widget,"bg") == "green":
            changeArray(widget)
    widget.bind('<Enter>', enter)
    widget.bind('<Leave>', leave)
#######################################################

# Change array (its actually an array this time)
# Adds or removes corresponding vector and its button depending on state of the button
def changeArray(selected):
    if (selected.isActive == False):
        newPixelIndex = len(pixelOrder)
        pixelOrder.append([dataValues[selected.bIndex][0],selected])
        selected.currentPixelIndex = newPixelIndex
        selected.isActive = True
        selected.configure(bg="green")
        #print("New data values:")
        #print(pixelOrder)
    else:
        selected.isActive = False
        selected.configure(bg="black")
        markedIndex = selected.currentPixelIndex
        pixelOrder.pop(markedIndex)
        selected.currentPixelIndex = 0
        for x in range(markedIndex+1,len(pixelOrder)+1):
            pixelOrder[x-1][1].currentPixelIndex -= 1
            #print(pixelOrder[x-1][1].currentPixelIndex, "deleted")
        #print("New data values:")
        #print(pixelOrder)


# Assign button to index in ascending order (starting from 0)
def assignButton(button):
    buttonValue = int(Tk.cget(button,"text"))
    button.configure(command=lambda: changeArray(button),text="")
    button.bIndex = buttonValue - 1

# Default button schema best looking button
for i in range(1,totalPixels+1):
    buttons[str(i)] = NewButton(window,text=i,padx=1,pady=1,width=5,bg="black")
    CreateToolTip(buttons[str(i)],"Ida")

currentSet = 1
currentRow = 0
# When you're too tired to copy and paste 20 buttons but you take longer to do it this way anyway:
for i in range(1,totalPixels+1):
    index = buttons[str(i)]
    number = int(Tk.cget(index,"text"))
    assignButton(buttons[str(i)])
    currentRow +=1
    dataValues.append([(currentSet,currentRow),buttons[str(i)],0])
    index.grid(row=currentRow, rowspan=1, column=currentSet+1)
    if (i % maximumPixelHeight == 0):
        currentRow = 0
        currentSet += 1


#print("Initial data values:")
#print(dataValues)

def removeData():
    global dataValues
    global pixelOrder
    for button in buttons:
        buttonValue = buttons[button]
        dataValues[buttonValue.bIndex-1][1] = buttonValue
        buttonValue.isActive = False
        buttonValue.configure(bg="black")
        buttonValue.currentPixelIndex = 0
    pixelOrder = []

def printData():
    assembledRDict = "{"
    if len(pixelOrder) == 1:
        print("{" + re.sub("[() ]", "",  str(pixelOrder[0][0])) + "}")
        return
    elif len(pixelOrder) == 0:
        print("Data is empty.")
        return
    for value in range(1,len(pixelOrder)+1):
        if (not value >= len(pixelOrder)):
            assembledRDict += re.sub("[() ]", "",  str(pixelOrder[value-1][0])) + ", "
        else:
            assembledRDict += re.sub("[() ]", "",  str(pixelOrder[value-1][0])) + "}"
    print(assembledRDict)



clearData = Button(window,text="Clear",padx=8,pady=8,width=5,bg="white",command=removeData)
clearData.grid(row=maximumPixelHeight+1,rowspan=1,column=0)

clearData = Button(window,text="Print Data",padx=8,pady=8,width=5,bg="white",command=printData)
clearData.grid(row=maximumPixelHeight+2,rowspan=1,column=0)


#currentEntry = Label(window,text = "",font=("Arial","15"),padx=45)
#currentEntry.grid(row=0, rowspan=1, column=5)

window.mainloop()

