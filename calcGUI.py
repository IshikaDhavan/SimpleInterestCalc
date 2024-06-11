from tkinter import * 

window = Tk()

window.title("Simple Interest")
window.geometry("500x500")
window.configure(bg="lightpink")

def CalculateResult():
    p = float(principalEntry.get())
    r = float(ROIEntry.get())
    t = float(TimeEntry.get())
    interest = (p * r * t)/100
    result = round(interest,2)
    ResultLabel.destroy()

    message = Label(ResultFrame,text="Interest on Rs. " + str(p) + " with the rate of interest of " + str(r) + " and year(s) " + str(t) + " is " + str(result), fg="black",bg = "gray", width= 55)
    message.place(x = 20, y = 40)
    message.pack()

heading = Label(window, text="Simple Interest Calculator", fg="black", bg="lightpink", font=("Times New Roman", 20), bd=5)
heading.place(x=10, y=10)

principalLabel = Label(window, text="Enter Principal", fg="black", bg="lightpink", font=("Arial", 12), bd=2)
principalLabel.place(x=20, y=75)

principalEntry = Entry(window, bd=2, width=15)
principalEntry.place(x=200, y=77)

ROILabel = Label(window, text="Enter Rate Of Interest", fg="black", bg="lightpink", font=("Arial", 12), bd=2)
ROILabel.place(x=20, y=110)

ROIEntry = Entry(window, bd=2, width=15)
ROIEntry.place(x=200, y=112)

TimeLabel = Label(window, text="Enter Time", fg="black", bg="lightpink", font=("Arial", 12), bd=2)
TimeLabel.place(x=20, y=145)

TimeEntry = Entry(window, bd=2, width=15)
TimeEntry.place(x=200, y=147)

CalculateButton = Button(window, text="Calculate SI", fg="black", bd=5, command=CalculateResult)
CalculateButton.place(x=20, y=190)

ResultFrame = LabelFrame(window, text="Result", bg="lightpink", font=("Calibri", 15), bd=2)
ResultFrame.pack(padx=20, pady=20)
ResultFrame.place(x=30, y=225)

ResultLabel = Label(ResultFrame,text=" ",bg="lightcyan",font=("calibri",12), width = 33)
ResultLabel.place(x=20,y=20)
ResultLabel.pack()

window.mainloop()
