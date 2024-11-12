import tkinter as tk
import tkinter.messagebox as mg

w1 = tk.Tk()
w1.title("Sentiment-Analyzer")
w1.geometry('400x120')
w1.resizable(False,False)

# general message when the Application starts
# mg.showinfo('Application General Information','It is general notice regarding the Application that it is used for getting the score Sentiment and Emotion calculated after you give your text based content in the input prompt.')

# creating a label here
lb1 = tk.Label(w1,text = 'Sentiment Analyzer',font = ('Bitstream Charter',12,'bold'))
lb1.pack(padx = 2 ,pady = 5)

# creating an entry point here
e1 = tk.Entry(w1,width = 40)
e1.pack(padx = 2,pady = 5)

def doThis():
    print(e1.get())

# creating a button here
btn1 = tk.Button(w1,text = 'Submit Text to Analyse',command = doThis)
btn1.pack()

w1.mainloop()