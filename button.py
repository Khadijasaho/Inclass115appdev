#from curses import button
import tkinter as tk



#Define a fucntion (button click)
#Creating a function for an event, when the button is click it going to trigger
#Implement the print function, whcih will say "Button clicked"
#This is the funtion that output something to the screen when the button is clicked
def button_click():
    print("Button clicked!")

#Creating the root window, the parent window
#Name it "root" than define the class library, once the class library is called you can now rename the parent window
root = tk.Tk()
root.title("Button Me")

#Creating the button object, which is going to have 3 different arguments
#Call the button subclass and the argument parameter then we going to put the button in the root window
#then call then root window for the first argumnet
#Second argument is the text
#For the third argument you have to call the function
#Idenitfy the place for the widget
button= tk.Button(root,text="Click Me!", command=button_click)
button.pack()
#Create the mainloop is an event, method from the root object and will keep the root window open
root.mainloop()
