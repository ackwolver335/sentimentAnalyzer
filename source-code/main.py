import tkinter as tk
import tkinter.messagebox as mg                                 # module for showing messages and warning box
from lingua import Language, LanguageDetectorBuilder            # language detector module

# major important modules
from transformers import pipeline,DistilBertTokenizer,DistilBertForSequenceClassification

# tokenizer and model
tokenizer = DistilBertTokenizer.from_pretrained('distilbert-base-uncased')
model = DistilBertForSequenceClassification.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')

# for sentiments [POSITIVE,NEGATIVE]
analyzer = pipeline('sentiment-analysis',model = model,tokenizer = tokenizer)

# for emotions detection
emotion_analyzer = pipeline('text-classification',model = 'j-hartmann/emotion-english-distilroberta-base')

w1 = tk.Tk()
w1.title("Sentiment-Analyzer")
w1.geometry('400x250')
w1.resizable(False,False)
w1.config(background = '#d9d9d9')

# initating a textual list for not entry creating a window for same text
textual_content = []

# creating a label here
lb1 = tk.Label(w1,text = 'Sentiment Analyzer',font = ('Bitstream Charter',15,'bold'))
lb1.pack(padx = 2 ,pady = 5)

# creating an entry point here
e1 = tk.Entry(w1,width = 30,font = ('Bitstream Charter',12),border = None)
e1.pack(padx = 2,pady = 4)

# method in order to clear the entry box
def clear_entry():
    if e1.get() == '':
        mg.showwarning('Application Warning','The Entry Box is already cleared !')
    else:
        e1.delete(0,tk.END)

# creating a button to make the entry empty if the user wants to
btn = tk.Button(text = 'Clear All',font = ('Bitstream Charter',10),command = clear_entry,border = None)
btn.pack(padx = 2,pady = 3)

# building language detector for english language
detector = LanguageDetectorBuilder.from_languages(Language.ENGLISH,Language.GERMAN).build()

# method for closing the main window
def close_main():
    w1.destroy()

# function's or Method's Block to be used as a command afterwards
def doThis():

    # block for the duplication of sentiment data
    if e1.get() in textual_content:
        mg.showwarning('Application Warning','The Textual Sentiment line is already available in our Database')
        return

    # adding the data to the list if not available
    if e1.get() not in textual_content:
        textual_content.append(e1.get())

    # situation when the user wants his/her sentiment detail and forget to enter the text
    if e1.get() == '':
        mg.showwarning('Application Warning','You are trying to get the data without providing the textual data !')
        return

    elif detector.detect_language_of(e1.get()) == Language.ENGLISH:
        
        # initiating the second window
        w2 = tk.Tk()
        w2.title("Analysed Sentiment")
        w2.geometry('300x120')
        w2.resizable(False,False)

        # initiative label
        wlb1 = tk.Label(w2,text = "Analysed Sentiment",font = ('Bitstream Charter',13,'bold'))
        wlb1.pack(padx = 2,pady = 5)

        result = analyzer(e1.get())
        emotion = emotion_analyzer(e1.get())

        # final detailed label
        final_output = 'Your Sentiment Label : {0}\nYour Sentiment Score : {1}%\nYour emotion : {2}'.format(result[0]['label'],int(result[0]['score'] * 100),(emotion[0]['label'].capitalize()))

        wlb2 = tk.Label(w2,anchor = tk.CENTER,text = final_output,font = ('Bitstream Charter',10))
        wlb2.pack(padx = 2,pady = 2)

        # Dark Mode according to the initial window
        if var1.get() == 1:
            w2.config(background = '#292826')
            wlb1.config(bg = '#292826',fg = 'white')
            wlb2.config(bg = '#292826',fg = 'white')

        # method for closing the window after specific time
        def close_window():
            w2.destroy()

        # timer for reseting window from user interaction
        def reset_window(event = None):
            w2.after_cancel(timer[0])
            timer[0] = w2.after(10000,close_window)

        # making a time for this purpose
        timer = [w2.after(10000,close_window)]

        # binding events to reset when user interact again
        w2.bind('<Motion>',reset_window)
        w2.bind('<KeyPress>',reset_window)
        w2.bind('<Button>',reset_window)                

        # ending of the window
        w2.mainloop()

    else:
        mg.warning('Application Warning','Trying to use another language, only english is allowed !')

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
        btn.config(bg = '#292826',fg = 'white')
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
        btn.config(bg = '#d9d9d9',fg = 'black')
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

# timer for reseting window from user interaction
def reset_window_time(event = None):
    w1.after_cancel(timer[0])
    timer[0] = w1.after(20000,close_main)

# making a time for this purpose
timer = [w1.after(20000,close_main)]

# binding events to reset when user interact again
w1.bind('<Motion>',reset_window_time)
w1.bind('<KeyPress>',reset_window_time)
w1.bind('<Button>',reset_window_time)

w1.mainloop()