# import all classes / functions from the tkinter
from tkinter import *
from datetime import date

# Function for clearing the
# contents of all entry boxes
def clear_all():
    # whole content of entry boxes is deleted
    principle_field.delete(0, END)
    rate_field.delete(0, END)
    sdate_field.delete(0, END)
    smonth_field.delete(0, END)
    syear_field.delete(0, END)
    edate_field.delete(0, END)
    emonth_field.delete(0, END)
    eyear_field.delete(0, END)
    simple_field.delete(0, END)
    compound_field.delete(0, END)
    time_field.delete(0, END)
    timey_field.delete(0, END)


    # set focus on the principle_field entry box
    principle_field.focus_set()


# Function to find compound interest
def calculate_ci():
    # get a content from entry box
    principle = int(principle_field.get())

    rate=float(rate_field.get())
    syear = int(syear_field.get())
    smonth = int(smonth_field.get())
    sdate = int(sdate_field.get())
    ds=date(syear, smonth, sdate)

    eyear = int(eyear_field.get())
    emonth = int(emonth_field.get())
    edate = int(edate_field.get())
    de=date(eyear, emonth, edate)

    gap=de-ds
    nodates=gap
    timedays=gap.days
    years=timedays/365
    pers=100/rate
    SI = principle/pers * years

    # Calculates compound interest
    CI = principle * (pow((1 + rate / 100), years))
    TI=nodates
    TY=365/timedays
    # insert method inserting the
    # value in the text entry box.
    simple_field.insert(10, SI)
    compound_field.insert(10, CI)
    time_field.insert(10, TI)
    timey_field.insert(10, TY)


# Driver code
if __name__ == "__main__":
    # Create a GUI window
    root = Tk()

    # Set the background colour of GUI window
    root.configure(background='gray15')

    # Set the configuration of GUI window
    root.geometry("800x400")

    # set the name of tkinter GUI window
    root.title("interest calculator")

    # Create a Principle Amount : label
    label1 = Label(root, text="Principle Amount(Rs) : ",
                   fg='black', bg='grey64')

    # Create a Rate : label
    label2 = Label(root, text="Rate(%) : ",
                   fg='black', bg='grey64')

    # Create a Time : label
    label3 = Label(root, text="Time(years) : ",
                   fg='black', bg='grey64')

    label4 = Label(root, text="simple interest : ",
                   fg='black', bg='grey64')
    # Create a Compound Interest : label
    label5 = Label(root, text="Compound Interest : ",
                   fg='black', bg='grey64')

    label6 = Label(root, text="start dd : ",
                   fg='black', bg='grey64')
    label7 = Label(root, text=" mm : ",
                   fg='black', bg='grey64')
    label8 = Label(root, text=" yyyy : ",
                   fg='black', bg='grey64')
    label9 = Label(root, text="end dd : ",
                   fg='black', bg='grey64')
    label10 = Label(root, text=" mm : ",
                   fg='black', bg='grey64')
    label11 = Label(root, text=" yyyy : ",
                   fg='black', bg='grey64')


    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .

    # padx keyword argument used to set paading along x-axis .
    # pady keyword argument used to set paading along y-axis .
    label1.grid(row=1, column=0, padx=10, pady=10)
    label2.grid(row=2, column=0, padx=10, pady=10)
    label3.grid(row=3, column=0, padx=10, pady=10)
    label4.grid(row=4, column=0, padx=10, pady=10)
    label5.grid(row=5, column=0, padx=10, pady=10)
    label6.grid(row=6, column=0, padx=0, pady=1)
    label7.grid(row=6, column=1, padx=0, pady=1)
    label8.grid(row=6, column=2, padx=0, pady=1)
    label9.grid(row=7, column=0, padx=0, pady=1)
    label10.grid(row=7, column=1, padx=0, pady=1)
    label11.grid(row=7, column=2, padx=0, pady=1)


    # Create a entry box
    # for filling or typing the information.
    principle_field = Entry(root)
    rate_field = Entry(root)
    time_field = Entry(root)
    timey_field = Entry(root)
    sdate_field = Entry(root)
    smonth_field = Entry(root)
    syear_field = Entry(root)

    edate_field = Entry(root)
    emonth_field = Entry(root)
    eyear_field = Entry(root)
    simple_field= Entry(root)
    compound_field = Entry(root)


    # grid method is used for placing
    # the widgets at respective positions
    # in table like structure .

    # padx keyword argument used to set paading along x-axis .
    # pady keyword argument used to set paading along y-axis .
    principle_field.grid(row=1, column=1, padx=10, pady=10)
    rate_field.grid(row=2, column=1, padx=10, pady=10)
    time_field.grid(row=3, column=1, padx=10, pady=10)
    timey_field.grid(row=3, column=3, padx=10, pady=10)
    simple_field.grid(row=4, column=1, padx=10, pady=10)
    compound_field.grid(row=5, column=1, padx=10, pady=10)
    sdate_field.grid(row=6, column=3, padx=1, pady=0)
    smonth_field.grid(row=6, column=4, padx=1, pady=0)
    syear_field.grid(row=6, column=5, padx=1, pady=0)
    edate_field.grid(row=7, column=3, padx=1, pady=0)
    emonth_field.grid(row=7, column=4, padx=1, pady=0)
    eyear_field.grid(row=7, column=5, padx=1, pady=0)

    # Create a Submit Button and attached
    # to calculate_ci function
    button1 = Button(root, text="Submit", bg="green",
                     fg="black", command=calculate_ci)

    # Create a Clear Button and attached
    # to clear_all function
    button2 = Button(root, text="Clear", bg="blue",
                     fg="black", command=clear_all)

    button1.grid(row=8, column=1, pady=10)
    button2.grid(row=8, column=2, pady=10)

    # Start the GUI
    root.mainloop()




