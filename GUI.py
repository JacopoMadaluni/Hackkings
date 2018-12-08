from tkinter import *

from tkinter import filedialog

import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg




font=("Helvetica Neue", 14)

cBackground = "#292d34"
cButtons = "#424B54"
#cButtons = "#9da39d"
#font = Font(family = "Helvetica Neue", size = 20, weight = "bold")

root = Tk()
root.title("Supreme")
root.minsize(900, 550)
root.geometry("900x550+0+0")
root.resizable(0,0)

filename = StringVar()
def UploadAction(event=None):
    file = filedialog.askopenfilename()
    filename.set(file)
    print('Selected:', file)

def quit():
        root.destroy()

def plot():
    getPlot();
    print("Plotting")
    f = plt.Figure(figsize=(5,5), dpi=100)
    plot = FigureCanvasTkAgg(f, main)
    plot.get_tk_widget().pack()

window = PanedWindow(orient=HORIZONTAL)
window.config(bg = "Black")

#----#

leftMenu = PanedWindow(window, orient=VERTICAL)
leftMenu.config(bg = cBackground, width = 200)

datasetLabel = Label(leftMenu, text = "Dataset", bg = cBackground, fg="white", borderwidth=0)
datasetLabel.config(font = font)
datasetLabel.place(x= 60, y= 20)

datasetNameLabel = Label(leftMenu, textvariable = filename, bg = cBackground, fg="white", borderwidth=0)
datasetNameLabel.config(font = font)
datasetNameLabel.place(x= 40, y= 103)

x = Button(leftMenu, text="X", bg=cBackground, fg="white", borderwidth=0)
x.config(font = font)
x.place(x= 160, y= 100)

importButton = Button(leftMenu, text="Import", bg=cButtons, fg="white", borderwidth=0, command=UploadAction )
importButton.config(font = font)
importButton.place(x= 60, y= 150)

dependantLabel = Label(leftMenu, text = "Dependent Var = ", bg = cBackground, fg="white", borderwidth=0)
dependantLabel.config(font = font)
dependantLabel.place(x= 25, y= 220)


tkvar = StringVar(root)

# Dictionary with options
choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
tkvar.set('Pizza') # set the default option

popupMenu = OptionMenu(leftMenu, tkvar, *choices,).place(x= 60, y= 260)

# on change dropdown value
def change_dropdown(*args):
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

startButton = Button(leftMenu, text="Start", bg=cButtons, fg="white", borderwidth=0)
startButton.place(x= 60, y= 400)
startButton.config(font = font)
#startButton.pack(padx=5, pady=5)


exitButton = Button(leftMenu, text="Exit", bg=cButtons, fg="white", borderwidth=0, command = quit)
exitButton.config(font = font)
exitButton.place(x= 60, y= 450)

#----#


window.add(leftMenu)

#----#

content = PanedWindow(window, orient=VERTICAL)
content.config(bg = "Black")

#------#

navbar = PanedWindow()
navbar.config(bg = cBackground, height = 70)

statusLabel = Label(navbar, text = "ESKETIT", bg = cBackground, fg = "White", borderwidth=0)
statusLabel.config(font = font)
statusLabel.place(x= 500, y=20)

predictButton = Button(navbar, text="Predict", bg=cButtons, fg="white", borderwidth=0)
predictButton.config(font = font)
predictButton.place(x= 50, y=14)

plotButton = Button(navbar, text="Plot", bg=cButtons, fg="white", borderwidth=0)
plotButton.config(font = font)
plotButton.place(x= 150, y=14)

main = PanedWindow()
main.config(bg = cBackground)





#------#

content.add(navbar)
content.add(main)


#----#

window.paneconfigure(leftMenu, minsize = 200)
window.add(content)
window.pack(fill=BOTH, expand=1)

root.mainloop()
