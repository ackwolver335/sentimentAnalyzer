import tkinter as tk
import tkinter.messagebox as mg

w1 = tk.Tk()
w1.title("Sentiment-Analyzer")
w1.geometry('400x220')
w1.resizable(False,False)
w1.config(background = '#d9d9d9')

# general message when the Application starts
# mg.showinfo('Application General Information','It is general notice regarding the Application that it is used for getting the score Sentiment and Emotion calculated after you give your text based content in the input prompt.')

# creating a label here
lb1 = tk.Label(w1,text = 'Sentiment Analyzer',font = ('Bitstream Charter',15,'bold'))
lb1.pack(padx = 2 ,pady = 5)

# creating an entry point here
e1 = tk.Entry(w1,width = 30,font = ('Bitstream Charter',12,'italic'),border = None)
e1.pack(padx = 2,pady = 5)

# function's or Method's Block to be used as a command afterwards
def doThis():
    
    # initiating the second window
    w2 = tk.Tk()
    w2.title("Analysed Sentiment")
    w2.geometry('300x150')
    w2.resizable(False,False)

    # initiative label
    wlb1 = tk.Label(w2,text = "Analysed Sentiment",font = ('Bitstream Charter',12,'bold'))
    wlb1.pack(padx = 2,pady = 5)

    # final detailed label

    # ending of the window
    w2.mainloop()

def dark_mode():

    # enable dark mode configurations
    if var1.get() == 1:

        w1.config(background = '#292826')
        chb1.config(text = "Disable Dark Mode",bg = '#292826',fg = 'white')
        lb1.config(bg = '#292826',fg = 'white')
        
        # frame configuration
        frm1.config(bg = '#292826')
        flb1.config(bg = '#292826',fg = 'white')
        flb2.config(bg = '#292826',fg = 'white')

        # main button configuration
        btn1.config(bg = '#292826',fg = 'white')
    
    # disable dark mode configuration
    else:

        w1.config(background = '#d9d9d9')
        chb1.config(text = "Enable Dark Mode",bg = '#d9d9d9',fg = 'black')
        lb1.config(bg = '#d9d9d9',fg = 'black')
        
        # frame configuration
        frm1.config(bg = '#d9d9d9')
        flb1.config(bg = '#d9d9d9',fg = 'black')
        flb2.config(bg = '#d9d9d9',fg = 'black')

        # main button configuration
        btn1.config(bg = '#d9d9d9',fg = 'black')

# adding frame for getting example
frm1 = tk.Frame(w1,width = 50,relief = 'groove')
frm1.pack(fill = 'both',padx = 2,pady = 4)

# components of the frame
flb1 = tk.Label(frm1,text = 'Example Overview',font = ('Bitstream Charter',12,'bold'),anchor = tk.CENTER)
flb1.pack(padx = 2,pady = 2)

# Example overview
text_entry = "Your Sentiment : POSITIVE\nYour Emotion : Happy\nYour Score : 0.91 or 91%"

flb2 = tk.Label(frm1,text = text_entry,font = ('Bitstream Charter',10,'bold'),anchor = tk.CENTER)
flb2.pack(padx = 2,pady = 2)

# adding a checkbox for dark mode
var1 = tk.IntVar()
chb1 = tk.Checkbutton(w1,text = "Enable Dark Mode",font = ('Bitstream Charter',10),variable = var1,onvalue = 1,offvalue = 0,command = dark_mode,border = None)
chb1.pack(side = 'left',padx = 4,pady = 1)

# creating a button here
btn1 = tk.Button(w1,text = 'Submit Text to Analyse',border = None,command = doThis)
btn1.pack(side = 'right',padx = 4,pady = 1) 

w1.mainloop()