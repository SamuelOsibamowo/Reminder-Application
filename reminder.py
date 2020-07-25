from tkinter import *
import time
root = Tk()
root.title("Reminder Application")
root.geometry("600x200")
root.configure(bg = "papaya whip")


#Creates the window where the reminder will be displayed
def new_reminder():
    reminder_win = Tk()
    if the_reminder.get() != '' and the_time.get() != '':
        temp_rem = the_reminder.get()
        temp_time = int(the_time.get())

        
        root.destroy()
        time.sleep(temp_time)
        reminder = Label(reminder_win, text = temp_rem, font = ("Helvetica", 20) )
        reminder.pack()
        reminder_win.mainloop()
    
    
#Main Reminder Title
title = Label(root, text= " Reminder Application ", font = ("Helvetica", 25), fg = "cornflower blue", bg = "papaya whip")
title.grid(row = 0, column = 1)

#Reminder Entry Widget
reminder_label = Label(root, text= "The reminder", font = ("Helvetica", 20), fg = "cornflower blue", bg = "papaya whip") 
reminder_label.place(x = 10, y = 65)
the_reminder = Entry(root, width = 50, borderwidth = 5)
the_reminder.place(x = 10, y = 100)

#Time Entry Widget
time_label = Label(root, text= "Time (Seconds)", font = ("Helvetica", 20), fg = "cornflower blue", bg = "papaya whip") 
time_label.place(x = 375, y = 65)
the_time = Entry(root, width = 20, borderwidth = 5)
the_time.place(x = 400, y = 100)

#Creates the Reminder
add_reminder = Button(root, text = "Make the reminder", width = 50, command = new_reminder)
add_reminder.place(x = 10, y = 170)


root.mainloop()