from tkinter import *
from PIL import Image, ImageTk

# setting basic display window
root = Tk()
# Adjust size of display window
root.geometry("1000x500")
root.title("SolveCaseWeather")
# set minimum window size value
root.minsize(1000, 500)
# set maximum window size value
root.maxsize(1000, 500)
# set min/max window size for constant size of window

# final screen that will output solution based on input
def heatwave():
    destroy_widgets()
    # background frame
    frame4 = Frame(root, width=1000, height=500, bg = '#FF3747')
    frame4.place(x=0, y=0)
    
    heatwave_text = Label(root, text="Solutions: Staying hydrated,", bg='#FF3747', fg='white')
    heatwave_text.config(font=("Courier", 14))
    heatwave_text.place(relx=0.4, rely=0.3, anchor=CENTER)
    heatwave_text = Label(root, text=" staying indoors with air conditioning and blocking out the sun,", bg='#FF3747', fg='white')
    heatwave_text.config(font=("Courier", 14))
    heatwave_text.place(relx=0.5, rely=0.4, anchor=CENTER)
    heatwave_text = Label(root, text=" planting trees to provide shade.", bg='#FF3747', fg='white')
    heatwave_text.config(font=("Courier", 14))
    heatwave_text.place(relx=0.6, rely=0.5, anchor=CENTER)
    
    # button to go to go back to question
    backbutton1 = Button(frame4,text='Back', command=question_one_screen)
    backbutton1.place(x=10, y=10)
    
# Function to destroy previous widgets
def destroy_widgets():
    for widget in root.winfo_children():
        widget.destroy()

# question one screen that will display question one
def question_one_screen():
# Clear previous widgets
    destroy_widgets()
    # background frame
    frame2 = Frame(root, width=1000, height=500, bg = '#ECF7DD')
    frame2.place(x=0, y=0)
    
    # Create label
    questiononescreentext = Label(root, text = "What Summer Season Issue are you Facing?", bg = '#ECF7DD', fg = 'black')
    questiononescreentext.config(font =("Courier", 14))
    questiononescreentext.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    questiononescreentext.pack()
    
    # buttons for summer options 
    button2 = Button(frame2, text='Heat Wave', command=heatwave)
    button2.place(x = 290, y = 300)
    button3 = Button(frame2, text='Hot Temperature', command=hottemp)
    button3.place(x = 390, y = 300)
    button4 = Button(frame2, text='Drought', command=drought)
    button4.place(x = 540, y = 300)
    button5 = Button(frame2, text='Forest Fires', command=forestfire)
    button5.place(x = 640, y = 300)
    
def hottemp():
    destroy_widgets()
    # background frame
    frame5 = Frame(root, width=1000, height=500, bg = '#DDF5C2')
    frame5.place(x=0, y=0)
    
    hottemp_text = Label(root, text="Solution: Using air conditioning or a fan,", bg='#DDF5C2', fg='black')
    hottemp_text.config(font=("Courier", 14))
    hottemp_text.place(relx=0.4, rely=0.3, anchor=CENTER)
    hottemp_text = Label(root, text=" wearing loose-clothing,", bg='#DDF5C2', fg='black')
    hottemp_text.config(font=("Courier", 14))
    hottemp_text.place(relx=0.5, rely=0.4, anchor=CENTER)
    hottemp_text = Label(root, text=" taking a cold shower.", bg='#DDF5C2', fg='black')
    hottemp_text.config(font=("Courier", 14))
    hottemp_text.place(relx=0.6, rely=0.5, anchor=CENTER)
    
    # button to go to go back to question
    backbutton2 = Button(frame5,text='Back', command=question_one_screen)
    backbutton2.place(x=10, y=10)
    
# Function to destroy previous widgets
def destroy_widgets():
    for widget in root.winfo_children():
        widget.destroy()

# question one screen that will display question one
def question_one_screen():
# Clear previous widgets
    destroy_widgets()
    # background frame
    frame2 = Frame(root, width=1000, height=500, bg = '#ECF7DD')
    frame2.place(x=0, y=0)
    
    # Create label
    questiononescreentext = Label(root, text = "What Summer Season Issue are you Facing?", bg = '#ECF7DD', fg = 'black')
    questiononescreentext.config(font =("Courier", 14))
    questiononescreentext.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    questiononescreentext.pack()
    
    # buttons for summer options 
    button2 = Button(frame2, text='Heat Wave', command=heatwave)
    button2.place(x = 290, y = 300)
    button3 = Button(frame2, text='Hot Temperature', command=hottemp)
    button3.place(x = 390, y = 300)
    button4 = Button(frame2, text='Drought', command=drought)
    button4.place(x = 540, y = 300)
    button5 = Button(frame2, text='Forest Fires', command=forestfire)
    button5.place(x = 640, y = 300)
    
def drought():
    destroy_widgets()
    # background frame
    frame6 = Frame(root, width=1000, height=500, bg = '#FFD600')
    frame6.place(x=0, y=0)
    drought_text = Label(root, text="Solution: Building aquifers that can provide water,", bg='#FFD600', fg='black')
    drought_text.config(font=("Courier", 14))
    drought_text.place(relx=0.4, rely=0.3, anchor=CENTER)
    drought_text = Label(root, text="increasing water storage capacity,", bg='#FFD600', fg='black')
    drought_text.config(font=("Courier", 14))
    drought_text.place(relx=0.5, rely=0.4, anchor=CENTER)
    drought_text = Label(root, text="installing dams and pool separations.", bg='#FFD600', fg='black')
    drought_text.config(font=("Courier", 14))
    drought_text.place(relx=0.6, rely=0.5, anchor=CENTER)
    
    # button to go to go back to question
    backbutton3 = Button(frame6,text='Back', command=question_one_screen)
    backbutton3.place(x=10, y=10)
    
# Function to destroy previous widgets
def destroy_widgets():
    for widget in root.winfo_children():
        widget.destroy()

# question one screen that will display question one
def question_one_screen():
# Clear previous widgets
    destroy_widgets()
    # background frame
    frame2 = Frame(root, width=1000, height=500, bg = '#ECF7DD')
    frame2.place(x=0, y=0)
    
    # Create label
    questiononescreentext = Label(root, text = "What Summer Season Issue are you Facing?", bg = '#ECF7DD', fg = 'black')
    questiononescreentext.config(font =("Courier", 14))
    questiononescreentext.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    questiononescreentext.pack()
    
    # buttons for summer options 
    button2 = Button(frame2, text='Heat Wave', command=heatwave)
    button2.place(x = 290, y = 300)
    button3 = Button(frame2, text='Hot Temperature', command=hottemp)
    button3.place(x = 390, y = 300)
    button4 = Button(frame2, text='Drought', command=drought)
    button4.place(x = 540, y = 300)
    button5 = Button(frame2, text='Forest Fires', command=forestfire)
    button5.place(x = 640, y = 300)

    
def forestfire():
    destroy_widgets()
    # background frame
    frame7 = Frame(root, width=1000, height=500, bg = '#EAE45F')
    frame7.place(x=0, y=0)
    
    forestfire_text = Label(root, text="Solution: Avoiding activities including fire or sparks when the weather is warm,", bg='#EAE45F', fg='black')
    forestfire_text.config(font=("Courier", 14))
    forestfire_text.place(relx=0.5, rely=0.3, anchor=CENTER)
    forestfire_text = Label(root, text=" putting out campfires after use.", bg='#EAE45F', fg='black')
    forestfire_text.config(font=("Courier", 14))
    forestfire_text.place(relx=0.4, rely=0.4, anchor=CENTER)
    forestfire_text.config(font=("Courier", 14))
    forestfire_text.place(relx=0.6, rely=0.5, anchor=CENTER)
    
    # button to go to go back to question
    backbutton4 = Button(frame7,text='Back', command=question_one_screen)
    backbutton4.place(x=10, y=10)
    
# Function to destroy previous widgets
def destroy_widgets():
    for widget in root.winfo_children():
        widget.destroy()
    
# question one screen that will display question one
def question_one_screen():
# Clear previous widgets
    destroy_widgets()
    # background frame
    frame2 = Frame(root, width=1000, height=500, bg = '#ECF7DD')
    frame2.place(x=0, y=0)
    
    # Create label
    questiononescreentext = Label(root, text = "What Summer Season Issue are you Facing?", bg = '#ECF7DD', fg = 'black')
    questiononescreentext.config(font =("Courier", 14))
    questiononescreentext.place(relx=0.5, rely=0.4, anchor=CENTER)
    
    questiononescreentext.pack()
    
    # buttons for summer options 
    button2 = Button(frame2, text='Heat Wave', command=heatwave)
    button2.place(x = 290, y = 300)
    button3 = Button(frame2, text='Hot Temperature', command=hottemp)
    button3.place(x = 390, y = 300)
    button4 = Button(frame2, text='Drought', command=drought)
    button4.place(x = 540, y = 300)
    button5 = Button(frame2, text='Forest Fires', command=forestfire)
    button5.place(x = 640, y = 300)


 
# menu screen 
def menuscreen():
    # background frame
    frame1 = Frame(root, width=1000, height=500, bg = '#ECF7DD')
    frame1.place(x=0, y=0)
 
    # menu welcome text + font
    menuscreentext = Label(root, text = "Welcome to SolveCaseWeather", bg = '#ECF7DD')
    menuscreentext.config(font =("Helvetica", 35))
    menuscreentext.pack()   
    
    # button to go to question one
    button1 = Button(frame1,text='Enter', command=question_one_screen)
    button1.place(x=10, y=10)
    
menuscreen()



# Execute tkinter
root.mainloop()


