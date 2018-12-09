from tkinter import *

from tkinter import filedialog

import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from RandomForestRegressor import RandomForestRegressor
from Controller import Controller
from Reader import Reader




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
controller = Controller()
reader = None
regressor = None
map = None
choices = []
current_y = 0

def UploadAction(event=None):
    print("what is happening")
    file = filedialog.askopenfilename()
    filename.set(file)
    print('Selected:', file)
    controller.set_file(file)

    global reader
    reader = Reader(file)
    set_map()
    set_choices()

def set_map():
    map = reader.headers_dict

def set_choices():
    global choices
    choices = reader.get_headers_names()
    init_choices_panel()

def quit():
    root.destroy()

def set_y_to_controller():
    controller.set_y_index(current_y)

def ignore_variable():
    controller.add_to_ignore(current_y, reader)

def set_best_regressor():
    global regressor
    regressor = controller.get_best_regressor()
    print("regressor name = {}".format(regressor.name))
    if regressor is None:
        print("diocane")
        # display error plot
        pass

def predict_test():
    regressor.predict_test()
    plot = FigureCanvasTkAgg(regressor.plot(), main)
    plot.get_tk_widget().pack()

def test_plot():
    if regressor:
        #regressor.train()
        regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9], [10],[11])
        print(regressor.name)
        return regressor.plot()

def plot():
    print("Plotting")
    plot = FigureCanvasTkAgg(test_plot(), main)
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

importButton = Button(leftMenu, text="Set Y", bg=cButtons, fg="white", borderwidth=0, command=set_y_to_controller )
importButton.config(font = font)
importButton.place(x= 15, y= 350)

importButton = Button(leftMenu, text="Ignore", bg=cButtons, fg="white", borderwidth=0, command=ignore_variable )
importButton.config(font = font)
importButton.place(x= 90, y= 350)


tkvar = StringVar(root)

def init_choices_panel():
# Dictionary with options
    #choices = { 'Pizza','Lasagne','Fries','Fish','Potatoe'}
    #tkvar.set('Pizza') # set the default option
    tkvar.set(choices[0])
    popupMenu = OptionMenu(leftMenu, tkvar, *choices,).place(x= 60, y= 260)

# on change dropdown value
def change_dropdown(*args):
    #controller.set_y_index(dic.get(tkvar.get))
    global current_y
    current_y = reader.get_header_col(tkvar.get())
    print( tkvar.get() )

# link function to change dropdown
tkvar.trace('w', change_dropdown)

startButton = Button(leftMenu, text="Start", bg=cButtons, fg="white", borderwidth=0, command=set_best_regressor)
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

predictButton = Button(navbar, text="Predict", bg=cButtons, fg="white", borderwidth=0, command=predict_test)
predictButton.config(font = font)
predictButton.place(x= 50, y=14)

plotButton = Button(navbar, text="Plot", bg=cButtons, fg="white", borderwidth=0, command = plot)
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
