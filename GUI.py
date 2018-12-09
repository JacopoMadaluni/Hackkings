from tkinter import *

from tkinter import filedialog

import matplotlib.pyplot as plt

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from RandomForestRegressor import RandomForestRegressor
from Controller import Controller
from Reader import Reader
from Presentation import start_presentation

from tkinter import messagebox




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
header_map = None
choices = []
current_y = 0
prediction_inputs = []
status_text = "Result: "
result_var = StringVar()
result_var.set(status_text)


def run_presentation():
    start_presentation()

def UploadAction(event=None):
    print("what is happening")
    file = filedialog.askopenfilename(filetypes = (("csv files","*.csv"),("all files","*.*")))
    filename.set(file)
    print('Selected:', file)
    controller.set_file(file)

    global reader
    reader = Reader(file)
    set_map()
    set_choices()

def set_map():
    header_map = reader.headers_dict

def set_choices():
    global choices
    choices = reader.get_headers_names()
    init_choices_panel()

def scatter():
    regressor.scatter_tests()

def quit():
    root.destroy()

def set_y_to_controller():
    controller.set_y_index(current_y)

def ignore_variable():
    message = controller.add_to_ignore(current_y, reader)
    choices.remove(reader.headers_dict.get(current_y))
    if len(message) != 0:
        errorMessage(message)
    init_choices_panel()

def set_best_regressor():
    global regressor
    regressor = controller.get_best_regressor()
    print("regressor name = {}".format(regressor.name))
    if regressor is None:
        print("diocane")
        # display error plot
        pass

def predict_inputs():
    print(prediction_inputs)
    args = [float(s.get()) for s in prediction_inputs]
    result = regressor.predict(*[args])
    status_text = "Result: {}".format(result)
    result_var.set("Result: {}".format(result))

def predict_test():
    print(predictionPoints.get())
    regressor.predict_test()
    plot = FigureCanvasTkAgg(regressor.get_plot(), main)
    plot.get_tk_widget().pack()

def predict_window():
    global prediction_inputs
    prediction_inputs = [StringVar() for _ in range(len(choices) - 1)]
    x = root.winfo_x()
    y = root.winfo_y()

    top = Toplevel(bg = cBackground)
    top.title("Predict")
    top.minsize(350, 200)
    top.geometry("%dx%d+%d+%d" % (350, 200, x + 375, y + 200))
    top.resizable(0,0)

    label_x = 10
    box_x = 208
    starting_y = 20;
    for i, header in enumerate(choices):
        if header != reader.headers_dict.get(current_y):
            xLabel = Label(top, text = header, bg = cBackground, fg="white", borderwidth=0)
            xLabel.config(font = font)
            xLabel.place(x= label_x, y= starting_y + i*30)

            box = Entry(top, textvariable = prediction_inputs[i])
            box.place(x=box_x, y = starting_y + i*30)
            #prediction_inputs.append(box)

    predict = Button(top, text="Predict", bg=cButtons, fg="white", borderwidth=0, command=predict_inputs)
    predict.config(font = font)
    predict.place(x=260, y=150)

    dismiss = Button(top, text="Dismiss", bg=cButtons, fg="white", borderwidth=0, command=top.destroy)
    dismiss.config(font = font)
    dismiss.place(x=160, y=150)


def test_plot():
    if regressor:
        #regressor.train()
        regressor.predict([1],[2],[3],[4],[5],[6],[7],[8],[9], [10],[11])
        print(regressor.name)
        return regressor.get_plot()

def plot():
    print("Plotting")
    regressor.predict_test()
    plot = FigureCanvasTkAgg(regressor.plot(), main)
    plot.get_tk_widget().pack()

def errorMessage(error):
    messagebox.showerror("Error", error)

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
    #if (len(choices) > 2):
#        for e in controller.to_ignore:
    #        if e in choices:
    #            choices.remove(reader.headers_dict.get(e))
            #controller.to_ignore.remove(e)
    tkvar.set(choices[0])
    #else:
    #    errorMessage("Can't remove any more variables, needs at least 2")
    popupMenu = OptionMenu(leftMenu, tkvar, *choices,).place(x= 60, y= 260)

# on change dropdown value
def change_dropdown(*args):
    #controller.set_y_index(dic.get(tkvar.get))
    global current_y
    current_y = reader.get_header_col(tkvar.get())
    #print( tkvar.get() )

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

statusLabel = Label(navbar, textvariable = result_var, bg = cBackground, fg = "White", borderwidth=0)
statusLabel.config(font = font)
statusLabel.place(x= 300, y=20)

predictButton = Button(navbar, text="Predict", bg=cButtons, fg="white", borderwidth=0, command=predict_window)
predictButton.config(font = font)
predictButton.place(x= 50, y=14)

plotButton = Button(navbar, text="Plot", bg=cButtons, fg="white", borderwidth=0, command = plot)
plotButton.config(font = font)
plotButton.place(x= 150, y=14)


scatterButton = Button(navbar, text="Scatter", bg=cButtons, fg="white", borderwidth=0, command = scatter)
scatterButton.config(font = font)
scatterButton.place(x= 200, y=14)

presentationButton = Button(navbar, text="Presentation", bg=cButtons, fg="white", borderwidth=0, command=run_presentation)
presentationButton.config(font = font)
presentationButton.place(x= 560, y=14)

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
