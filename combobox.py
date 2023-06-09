#create a tkinter application and start with import
import tkinter as tk
from tkinter import ttk

#Creating the function that is going to handle the event for when you click one something in the combobox
#When you click an item in the combobox it's going to trigger an event, need to write the function for the event 
def on_select(event):
    #Going to pass the event into the argumnet parameter, than obtain the value from the combobox
    #Creating an object called selected item than pass into to the print function for the event 
    #Going to get the item that the end user has choosen on the combobox 
     selected_item = event.widget.get() 
     #Create a print function the say selected item and the selected items intot the argument parameter
     print("Selected item", selected_item)

     #parent group root the window then take the widget object and put it in the widgeted window 
     root = tk.Tk()
     root.title("Combobox Exapmle")
     # Creating an array of items, declae the tiems into an array
     items = ["Item 1", "Item 2", "Item 3", "Item 4", "Item 5"]

     #Create combobox object
     #Going to bind events to the objects, using on_select
     combo_box = ttk.Combobox(root, values=items)
     combo_box.bind("<<ComboboxSelected>>", on_select)

     combo_box.pack()

    #Reoccuring window 
     root.mainloop()


      


